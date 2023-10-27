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
    tenses = list(Tense)
    if mood == 'subjunctive':
        del tenses[2], tenses[-1] # no future subjunctives
    present_tenses = tenses[:len(tenses)//2]
    perfect_tenses = tenses[len(tenses)//2:]
    width = max(len(str(Verb(person, number, tense, voice, mood, verb)))
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
                               voice, mood, verb)).center(width), end='')
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
                               voice, mood, verb)).center(width), end='')
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
    full_conj_table(dūcō)
    print()
    full_conj_table(incipiō)
    print()
    full_conj_table(sentiō)

def test_nouns() -> None:
    from vocab import servus
    declension_table(servus)

def test_adjectives() -> None:
    from vocab import clārus
    modification_table(clārus)

def random_test() -> None:
    from vocab import capiō, Rōmānus, dexter
    noun = Noun('genitive', 'pl', Rōmānus.as_noun('M'))
    adj = Adjective(dexter, noun)
    print(adj, noun)
    verb = Verb(1, 'sg', Tense.PRESENT, 'active', 'subjunctive', capiō)
    print(verb)

def main():
    test_verbs()
    # print('=====')
    # test_nouns()
    # print('=====')
    # test_adjectives()
    # print('=====')
    # random_test()

if __name__ == '__main__':
    main()
