import random
from collections import deque

import vocab
from notes import *

def do_flashcards() -> None:
    words = [(word, item) for word in dir(vocab) if isinstance(item := getattr(vocab, word), Vocab)]
    history = deque(maxlen=20)
    while 1:
        word, item = random.choice(words)
        if word in history:
            continue
        history.append(word)
        parts = item.principal_parts or [word]
        definition = item.definition
        if random.randint(0, 1):
            print(', '.join(parts))
            answer = input('Definition  (yours): '):
            print('Definition (actual):', definition)
        else:
            print(definition)
            print(', '.join(['_' * max(map(len, parts))] * len(parts)))
            answer = input():
            print(', '.join(parts))
        if not answer:
            return
        print('-' * 20)

if __name__ == '__main__':
    do_flashcards()
