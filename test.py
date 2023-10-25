from typing import get_args
from notes import NounVocab, Noun, AdjVocab, Adjective, VerbVocab, Verb, Tense, \
    Case, Number

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

def conjugation_table(verb: VerbVocab) -> None:
    tenses = list(Tense)
    width = max(len(str(Verb(person, number, tense, 'active', 'indicative', verb)))
                for person in (1, 2, 3) for number in get_args(Number) for tense in tenses)
    width = max(width, max(len(tense.value) for tense in tenses))
    width += 1 # add a space
    print('singular'.center(width * 3) + 'plural'.center(width * 3))
    for tense in (*tenses[:3], *tenses[:3]):
        print(tense.value.center(width), end='')
    print('\n' + '-' * (width * 6))
    for person in (1, 2, 3):
        for number in get_args(Number):
            for tense in tenses[:3]:
                print(str(Verb(person, number, tense,
                               'active', 'indicative', verb)).center(width), end='')
        print()

    print('singular'.center(width * 3) + 'plural'.center(width * 3))
    for tense in (*tenses[3:], *tenses[3:]):
        print(tense.value.center(width), end='')
    print('\n' + '-' * (width * 6))
    for person in (1, 2, 3):
        for number in get_args(Number):
            for tense in tenses[3:]:
                print(str(Verb(person, number, tense,
                               'active', 'indicative', verb)).center(width), end='')
        print()

def test_verbs() -> None:
    from vocab import incipiō, sentiō
    conjugation_table(incipiō)
    print()
    conjugation_table(sentiō)

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
