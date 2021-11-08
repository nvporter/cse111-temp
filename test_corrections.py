import random
from corrections import get_determiner, get_noun, get_verb
import pytest




def test_get_determiner():
    single_determiners = ['the', 'one']
    for _ in range(4):
        word = get_determiner(1)

        assert word in single_determiners
    plural_determiners = ['some', 'many']

    for _ in range(4):
        word = get_determiner(2)
        assert word in plural_determiners