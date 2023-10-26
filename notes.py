from __future__ import annotations
from typing import Literal, LiteralString, ClassVar, \
    cast, assert_never
from dataclasses import dataclass
from enum import Enum

VOWELS = tuple('aeiouyāēīōū')

def lengthen(vowel: str) -> str:
    return {
        'a': 'ā',
        'e': 'ē',
        'i': 'ī',
        'o': 'ō',
        'u': 'ū',
    }.get(vowel, vowel)

def shorten(vowel: str) -> str:
    return {
        'ā': 'a',
        'ē': 'e',
        'ī': 'i',
        'ō': 'o',
        'ū': 'u',
    }.get(vowel, vowel)

Person = Literal[1, 2, 3]
Number = Literal['sg', 'pl']

class Tense(Enum):
    PRESENT = 'present'
    IMPERFECT = 'imperfect'
    FUTURE = 'future'
    PERFECT = 'perfect'
    PLUPERFECT = 'pluperfect'
    FUTURE_PERFECT = 'future perfect'

    @property
    def perfect(self) -> bool:
        return self in {
            Tense.PERFECT,
            Tense.PLUPERFECT,
            Tense.FUTURE_PERFECT,
        }

    @property
    def past(self) -> bool:
        return self in {
            Tense.IMPERFECT,
            Tense.PERFECT,
            Tense.PLUPERFECT,
        }

    @property
    def unpast(self) -> Tense:
        return {
            Tense.PERFECT: Tense.PRESENT,
            Tense.PLUPERFECT: Tense.IMPERFECT,
            Tense.FUTURE_PERFECT: Tense.FUTURE,
        }[self]

Voice = Literal['active', 'passive']
Mood = Literal['indicative', 'subjunctive', 'imperative']

@dataclass
class Verb:
    person: Person
    number: Number
    tense: Tense
    voice: Voice
    mood: Mood
    vocab: VerbVocab

    @property
    def personal_ending(self) -> LiteralString:
        if self.tense.value == 'perfect' and self.mood == 'indicative':
            perf_table: dict[Number, list[LiteralString]] = {
                'sg': ['ī', 'istī', 'it'],
                'pl': ['imus', 'istis', 'ērunt'],
            }
            # perfect passive handled separately
            return perf_table[self.number][self.person - 1]
        table: dict[Voice, dict[Number, list[LiteralString]]] = {
            'active': {
                'sg': ['ō', 's', 't'],
                'pl': ['mus', 'tis', 'nt'],
            },
            'passive': {
                'sg': ['or', 'ris', 'tur'],
                'pl': ['mur', 'minī', 'ntur'],
            }
        }
        if self.person == 1 and self.number == 'sg':
            if self.mood == 'indicative' \
                    and self.tense.past \
                    and self.voice == 'active' \
                    or self.mood != 'indicative':
                return 'm'
            if self.mood == 'indicative' \
                    and (self.tense.past or self.tense == Tense.FUTURE) \
                    and self.voice == 'passive':
                return 'r'
        return table[self.voice][self.number][self.person - 1]

    @property
    def tense_sign(self) -> LiteralString:
        match self.tense.value:
            case 'present' | 'perfect':
                return ''
            case 'imperfect':
                if self.vocab.i_stem:
                    return 'ēbā'
                return 'bā'
            case 'pluperfect':
                return 'erā'
            case 'future':
                if self.vocab.conjugation == 1 or self.vocab.conjugation == 2:
                    return 'bi'
                if self.vocab.conjugation == 3 or self.vocab.conjugation == 4:
                    return 'ē' if self.person != 1 or self.number == 'pl' else 'a'
                assert_never(self.vocab.conjugation)
            case 'future perfect':
                return 'eri'
            case x:
                assert_never(x)

    @property
    def stem(self) -> LiteralString:
        if self.tense.perfect:
            return self.vocab.perfect_stem
        return self.vocab.present_stem

    def __str__(self) -> str:
        """Render to string word."""
        match self.mood:
            case 'indicative':
                return self._conjg_indicative()
            case 'subjunctive':
                return self._conjg_subjunctive()
            case 'imperative':
                raise NotImplementedError
            case x:
                assert_never(x)

    def _add_personal_ending(self, result: str, person: str) -> str:
        # technically -or is the same as -r so it shortens the preceding vowel
        if person in {'m', 't', 'nt', 'or', 'r', 'ntur'}:
            result = result[:-1] + shorten(result[-1])
        if person == 'ō' and result.endswith(VOWELS):
            if self.vocab.i_stem:
                result = result[:-1] + shorten(result[-1]) + person
            else:
                result = result[:-1] + person
        elif person == 'nt' and result[-1] in {'i', 'ī'}:
            result = result[:-1]
            if self.mood == 'indicative' and self.tense.value != 'future perfect':
                if self.vocab.i_stem:
                    result += 'i' # restore removed i
                result += 'unt'
            else:
                result += 'int'
        else:
            result += person
        return result

    def _conjg_indicative(self) -> str:
        if self.vocab.is_be and not self.tense.perfect:
            result = {
                'present': {
                    'sg': ['su', 'e', 'es'],
                    'pl': ['su', 'es', 'su'],
                },
                'imperfect': {
                    'sg': ['erā', 'erā', 'erā'],
                    'pl': ['erā', 'erā', 'erā'],
                },
                'future': {
                    'sg': ['eri', 'eri', 'eri'],
                    'pl': ['eri', 'eri', 'eri'],
                }
            }[self.tense.value][self.number][self.person - 1]
        else:
            stem = self.stem
            tense = self.tense_sign
            if stem[-1] in VOWELS and tense and tense[0] in VOWELS:
                stem = stem[:-1] + shorten(stem[-1])
            result = stem + tense
        person = self.personal_ending
        if (
            person == 'ō'
            and (
                self.vocab.conjugation in {3, 4}
                if self.tense.value == 'future'
                else self.vocab.is_be
            )
        ):
            person = 'm'
        return self._add_personal_ending(result, person)

    def _conjg_subjunctive(self) -> str:
        match self.tense.value:
            case 'present':
                if self.vocab.is_be:
                    stem = 'sī'
                else:
                    subj_sign = {
                        1: 'ē',
                        2: 'eā',
                        3: 'ā',
                        4: 'iā',
                    }[self.vocab.conjugation]
                    if self.vocab.conjugation == 3 and self.vocab.i_stem:
                        subj_sign = 'i' + subj_sign
                    stem = self.stem[:-1] + subj_sign
                return self._add_personal_ending(
                    stem, self.personal_ending
                )
            case 'imperfect':
                stem = self.vocab.present_active_infinitive
                return self._add_personal_ending(
                    stem[:-1] + lengthen(stem[-1]),
                    self.personal_ending
                )
            case 'perfect':
                stem = self.stem
                return self._add_personal_ending(
                    stem + 'eri', self.personal_ending
                )
            case 'pluperfect':
                stem = self.stem
                return self._add_personal_ending(
                    stem + 'issē', self.personal_ending
                )
            case _:
                raise ValueError(self.tense.value)

@dataclass
class VerbVocab:
    present_active_indicative_1p_s: LiteralString
    present_active_infinitive: LiteralString
    perfect_active_indicative_1p_s: LiteralString
    perfect_passive_participle: LiteralString

    def __post_init__(self) -> None:
        pai = self.present_active_indicative_1p_s.rstrip('iō')

        item = self.present_active_infinitive
        if item.startswith('-'):
            self.present_active_infinitive = pai + item.lstrip('-')

        item = self.perfect_active_indicative_1p_s
        if item.startswith('-'):
            self.perfect_active_indicative_1p_s = pai + item.lstrip('-')

        item = self.perfect_passive_participle
        if item.startswith('-'):
            self.perfect_passive_participle = pai + item.lstrip('-')

    @classmethod
    def first_conj(cls, present_active_indicative_1p_s: LiteralString) -> VerbVocab:
        return cls(
            present_active_indicative_1p_s,
            '-āre', '-āvī', '-ātus'
        )

    @property
    def conjugation(self) -> Literal[1, 2, 3, 4]:
        pai = self.present_active_infinitive
        if pai.endswith('āre'):
            return 1
        if pai.endswith('ēre'):
            return 2
        if pai.endswith('ere'):
            return 3
        if pai.endswith('īre'):
            return 4
        # hardcoded special cases
        if pai == 'dare':
            return 1
        if pai == 'esse':
            return 2 # arbitrary, esse doesn't belong
        raise ValueError(pai)

    @property
    def present_stem(self) -> LiteralString:
        stem = self.present_active_infinitive.removesuffix('re')
        if self.i_stem and self.conjugation == 3:
            return stem.removesuffix('e') + 'i'
        return stem

    @property
    def perfect_stem(self) -> LiteralString:
        return self.perfect_active_indicative_1p_s.removesuffix('ī')

    @property
    def is_be(self) -> bool:
        return self.present_active_infinitive == 'esse'

    @property
    def i_stem(self) -> bool:
        if self.conjugation == 4:
            return True
        if self.conjugation != 3:
            return False
        return self.present_active_indicative_1p_s.endswith('iō')

@dataclass
class Noun:
    case: Case
    number: Number
    vocab: NounVocab

    @property
    def declension_ending(self) -> LiteralString:
        match self.vocab.declension:
            case 1:
                table1: dict[Number, dict[Case, LiteralString]] = {
                    'sg': {
                        'nominative': 'a',
                        'genitive': 'ae',
                        'dative': 'ae',
                        'accusative': 'am',
                        'ablative': 'ā',
                        'vocative': 'a',
                    },
                    'pl': {
                        'nominative': 'ae',
                        'genitive': 'ārum',
                        'dative': 'īs',
                        'accusative': 'ās',
                        'ablative': 'īs',
                        'vocative': 'ae',
                    }
                }
                return table1[self.number][self.case]
            case 2:
                table2: dict[Number, dict[Gender, dict[Case, LiteralString]]] = {
                    'sg': {
                        'M': {
                            'nominative': 'us',
                            'genitive': 'ī',
                            'dative': 'ō',
                            'accusative': 'um',
                            'ablative': 'ō',
                            'vocative': 'us',
                        },
                        'N': {
                            'nominative': 'um',
                            'genitive': 'ī',
                            'dative': 'ō',
                            'accusative': 'um',
                            'ablative': 'ō',
                            'vocative': 'um',
                        }
                    },
                    'pl': {
                        'M': {
                            'nominative': 'ī',
                            'genitive': 'ōrum',
                            'dative': 'īs',
                            'accusative': 'ōs',
                            'ablative': 'īs',
                            'vocative': 'ī',
                        },
                        'N': {
                            'nominative': 'a',
                            'genitive': 'ōrum',
                            'dative': 'īs',
                            'accusative': 'a',
                            'ablative': 'īs',
                            'vocative': 'a',
                        }
                    }
                }
                if self.vocab.gender == 'M' and self.case == 'nominative' and self.number == 'sg':
                    if self.vocab.nominative_singular.endswith('er'):
                        return 'er'
                    if self.vocab.nominative_singular.endswith('r'):
                        return 'r'
                return table2[self.number][self.vocab.gender][self.case]
            case _:
                raise ValueError(self.vocab.declension)

    def __str__(self) -> str:
        """Render to string word"""
        return self.vocab.stem + self.declension_ending

@dataclass
class Adjective:
    vocab: AdjVocab
    target: Noun | Adjective # noun (or its modifying adjective) being modified

    @property
    def noun(self) -> Noun:
        if isinstance(self.target, Noun):
            return self.target
        return self.target.noun

    def __str__(self) -> str:
        """Render to string word"""
        pseudo_nv = self.vocab.as_noun(self.noun.vocab.gender)
        pseudo_noun = Noun(self.noun.case, self.noun.number, pseudo_nv)
        return str(pseudo_noun)

Case = Literal[
    'nominative',
    'genitive',
    'dative',
    'accusative',
    'ablative',
    'vocative',
]

Gender = Literal[
    'M', 'F', 'N'
]

@dataclass
class NounVocab:
    declension_endings: ClassVar[list[LiteralString]] = [
        'ae', 'ī', 'is', 'ūs', 'eī'
    ]
    nominative_singular: LiteralString
    genitive_singular: LiteralString
    gender: Gender

    def __post_init__(self) -> None:
        match self.declension, self.gender:
            case 1, _:
                ns = self.nominative_singular.removesuffix('a')
            case 2, 'M':
                ns = self.nominative_singular.removesuffix('us')
            case 2, 'N':
                ns = self.nominative_singular.removesuffix('um')
            case _:
                raise ValueError(self.declension)

        item = self.genitive_singular
        if item.startswith('-'):
            self.genitive_singular = ns + item.lstrip('-')

    @property
    def declension(self) -> Literal[1, 2, 3, 4, 5]:
        gs = self.genitive_singular
        for i, ending in enumerate(self.declension_endings, start=1):
            if gs.endswith(ending):
                return cast(Literal[1, 2, 3, 4, 5], i)
        if gs == '--' or gs == '':
            return 1 # no genitive singular = 1st declension by default
        raise ValueError(gs)

    @property
    def stem(self) -> LiteralString:
        return self.genitive_singular.removesuffix(
            self.declension_endings[self.declension - 1])

@dataclass
class AdjVocab:
    masculine: LiteralString
    feminine: LiteralString
    neuter: LiteralString

    def __post_init__(self) -> None:
        stem = self.masculine.removesuffix('us')

        item = self.feminine
        if item.startswith('-'):
            self.feminine = stem + item.lstrip('-')

        item = self.neuter
        if item.startswith('-'):
            self.neuter = stem + item.lstrip('-')

    def as_noun(self, gender: Gender) -> NounVocab:
        match gender:
            case 'M':
                return NounVocab(self.masculine, '-ī', 'M')
            case 'F':
                return NounVocab(self.feminine, '-ae', 'F')
            case 'N':
                return NounVocab(self.neuter, '-ī', 'N')
            case x:
                assert_never(x)

@dataclass
class PrepVocab:
    prep: LiteralString | list[LiteralString]
    case: Case

if __name__ == '__main__':
    from test import main
    main()
