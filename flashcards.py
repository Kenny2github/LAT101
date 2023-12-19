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
            if not input('Definition  (yours): '):
                return
            print('Definition (actual):', definition)
        else:
            print(definition)
            if not input('Principal parts  (yours): '):
                return
            print('Principal parts (actual):', ', '.join(parts))
        print('-' * 20)

if __name__ == '__main__':
    do_flashcards()
