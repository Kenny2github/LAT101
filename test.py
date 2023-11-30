from typing import get_args
from notes import NounVocab, Noun, AdjVocab, Adjective, VerbVocab, Verb, Tense, \
    Case, Number, Voice, Mood

def declension_table(noun: NounVocab) -> None:
    width = max(len(str(Noun(case, number, noun)))
                for case in get_args(Case) for number in get_args(Number))
    width = max(width, len('singular'), len('plural'))
    width += 1
    print('singular'.center(width) + 'plural'.center(width))
    print('-' * (width * 2))
    for case in get_args(Case):
        for number in get_args(Number):
            print(str(Noun(case, number, noun)).center(width), end='')
        print()

def modification_table(adj: AdjVocab) -> None:
    from vocab import campus, dextra, dōnum
    for gender, noun in {'masculine': campus, 'feminine': dextra, 'neuter': dōnum}.items():
        print(gender)
        print('=' * len(gender))
        width = max(len(str(Adjective(adj, Noun(case, number, noun))))
                    for case in get_args(Case) for number in get_args(Number))
        width = max(width, len('singular'), len('plural'))
        width += 1
        print('singular'.center(width) + 'plural'.center(width))
        print('-' * (width * 2))
        for case in get_args(Case):
            for number in get_args(Number):
                print(str(Adjective(adj, Noun(case, number, noun))).center(width), end='')
            print()

def conjugation_table(
    verb: VerbVocab, voice: Voice = 'active', mood: Mood = 'indicative'
) -> None:
    from vocab import Marcus
    # dummy subject, never displayed
    subject = Noun('nominative', 'sg', Marcus)

    tenses = list(Tense)
    if mood == 'subjunctive':
        del tenses[2], tenses[-1] # no future subjunctives
    elif mood == 'infinitive':
        del tenses[1], tenses[-2:] # only present, future, and perfect infinitives
        if voice == 'passive':
            del tenses[1] # future passive infinitive not implemented
    present_tenses = [tense for tense in tenses if not tense.perfect]
    perfect_tenses = [tense for tense in tenses if tense.perfect]
    width = max(len(str(Verb(person, number, tense, voice, mood, verb, subject)))
                for person in (1, 2, 3) for number in get_args(Number) for tense in tenses)
    width = max(width, max(len(tense.value) for tense in tenses))
    width += 1 # add a space
    print('singular'.center(width * len(present_tenses))
          + 'plural'.center(width * len(present_tenses)))
    for tense in (*present_tenses, *present_tenses):
        print(tense.value.center(width), end='')
    print('\n' + '-' * (width * len(present_tenses) * 2))
    for person in (1, 2, 3):
        for number in get_args(Number):
            for tense in present_tenses:
                print(str(Verb(person, number, tense,
                               voice, mood, verb, subject)).center(width), end='')
        print()

    print('singular'.center(width * len(perfect_tenses))
          + 'plural'.center(width * len(perfect_tenses)))
    for tense in (*perfect_tenses, *perfect_tenses):
        print(tense.value.center(width), end='')
    print('\n' + '-' * (width * len(perfect_tenses) * 2))
    for person in (1, 2, 3):
        for number in get_args(Number):
            for tense in perfect_tenses:
                print(str(Verb(person, number, tense,
                               voice, mood, verb, subject)).center(width), end='')
        print()

def full_conj_table(verb: VerbVocab) -> None:
    for voice in get_args(Voice):
        for mood in get_args(Mood):
            if mood == 'imperative':
                continue # not yet implemented
            print(voice.upper(), mood.upper())
            print('=' * (len(voice) + len(mood) + 1))
            conjugation_table(verb, voice, mood)

def test_verbs() -> None:
    from vocab import dūcō, incipiō, sentiō
    print('\n' + ' 3rd conjugation '.center(79, '=') + '\n')
    full_conj_table(dūcō)
    print('\n' + ' 3rd conjugation, i-stem '.center(79, '=') + '\n')
    full_conj_table(incipiō)
    print('\n' + ' 4th conjugation '.center(79, '=') + '\n')
    full_conj_table(sentiō)

def test_nouns() -> None:
    from vocab import urbs
    declension_table(urbs)

def test_adjectives() -> None:
    from vocab import clārus
    modification_table(clārus)

def random_test() -> None:
    from vocab import audiō, incipiō, ambulō, liber
    print(Adjective(
        Verb(1, 'sg', Tense.PRESENT, 'active', 'indicative', audiō),
        Noun('nominative', 'sg', liber)
    ), Adjective(
        Verb(1, 'sg', Tense.PERFECT, 'passive', 'indicative', incipiō),
        Noun('nominative', 'sg', liber)
    ), Adjective(
        Verb(1, 'sg', Tense.FUTURE, 'active', 'indicative', ambulō),
        Noun('nominative', 'sg', liber)
    ), Adjective(
        Verb(1, 'sg', Tense.FUTURE, 'passive', 'indicative', incipiō),
        Noun('nominative', 'sg', liber)
    ))

def main():
    # test_verbs()
    # print('=====')
    test_nouns()
    # print('=====')
    # test_adjectives()
    # print('=====')
    # random_test()

if __name__ == '__main__':
    main()
