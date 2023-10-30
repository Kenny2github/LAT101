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
    print('\n' + ' 3rd conjugation '.center(79, '=') + '\n')
    full_conj_table(dūcō)
    print('\n' + ' 3rd conjugation, i-stem '.center(79, '=') + '\n')
    full_conj_table(incipiō)
    print('\n' + ' 4th conjugation '.center(79, '=') + '\n')
    full_conj_table(sentiō)

def test_nouns() -> None:
    from vocab import servus
    declension_table(servus)

def test_adjectives() -> None:
    from vocab import clārus
    modification_table(clārus)

def random_test() -> None:
    print()
    from vocab import (
        turba, magnus, rēgīna, bonus, gladius, terreō,
        prōvincia, īnsula, superō,
        littera, ā, pulcher, ad, honestus, mittō,
        moneō, bellum, gerō,
        oppidum, amīcus, malus,
    )
    print('Unit Three Exercises I.10')
    crowd = Noun('nominative', 'sg', turba)
    large = Adjective(magnus, crowd)
    queen = Noun('accusative', 'sg', rēgīna)
    good = Adjective(bonus, queen)
    with_swords = Noun('ablative', 'pl', gladius)
    frightened = Verb(3, 'sg', Tense.PERFECT, 'active', 'indicative', terreō)
    in_order_that = 'ut'
    both = 'et'
    province = Noun('accusative', 'sg', prōvincia)
    and_ = 'et'
    island = Noun('accusative', 'sg', īnsula)
    might_conquer = Verb(3, 'sg', Tense.IMPERFECT, 'active', 'subjunctive', superō)
    print(crowd, large, queen, good, with_swords, frightened,
          in_order_that, both, province, and_, island, might_conquer)
    print('The large crowd frightened the good queen with swords '
          'in order that she might conquer both the province and the island.')

    print('\nUnit Four Exercises I.5')
    if_ = 'sī'
    letters = Noun('nominative', 'pl', littera)
    by1 = ā.prep[0]
    queen = Noun(ā.case, 'sg', rēgīna)
    beautiful = Adjective(pulcher, queen)
    to = ad.prep
    honorable_men = Noun(ad.case, 'pl', honestus.as_noun('M'))
    had_been_sent = Verb(3, 'pl', Tense.PLUPERFECT, 'passive', 'subjunctive', mittō, letters.vocab.gender, letters.number)
    they_would_have_been_warned = Verb(3, 'pl', Tense.PLUPERFECT, 'passive', 'subjunctive', moneō, subj_number='pl')
    in_order_that = 'ut'
    war = Noun('accusative', 'sg', bellum)
    they_might_wage = Verb(3, 'pl', Tense.IMPERFECT, 'active', 'subjunctive', gerō)
    and_ = 'et'
    town = Noun('nominative', 'sg', oppidum)
    by2 = ā.prep[1]
    friends = Noun(ā.case, 'pl', amīcus.as_noun('M'))
    evil = Noun('genitive', 'pl', malus.as_noun('M'))
    not_ = 'nōn'
    have_been_conquered = Verb(3, 'sg', Tense.PLUPERFECT, 'passive', 'subjunctive', superō, town.vocab.gender, town.number)
    print(if_, letters, by1, queen, beautiful, to, honorable_men, had_been_sent,
          they_would_have_been_warned, in_order_that, war, they_might_wage,
          and_, town, by2, friends, evil, not_, have_been_conquered)
    print('If letters had been sent by the beautiful queen to honorable men, '
          'they would have been warned in order that they might wage a war, '
          'and the town would not have been conquered by friends of evil (men).')

def main():
    test_verbs()
    # print('=====')
    # test_nouns()
    # print('=====')
    # test_adjectives()
    # print('=====')
    random_test()

if __name__ == '__main__':
    main()
