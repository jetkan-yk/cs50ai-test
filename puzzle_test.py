"""
Regression tests for puzzle.py

Make sure that this file is in the same directory as puzzle.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from puzzle import *

# source: https://edstem.org/us/courses/176/discussion/107478


def test_puzzle0():
    # AKnave
    assert model_check(knowledge0, AKnave) == True

    assert model_check(knowledge0, AKnight) == False
    assert model_check(knowledge0, BKnight) == False
    assert model_check(knowledge0, BKnave) == False
    assert model_check(knowledge0, CKnight) == False
    assert model_check(knowledge0, CKnave) == False


def test_puzzle1():
    # AKnave, BKnight
    assert model_check(knowledge1, AKnave) == True
    assert model_check(knowledge1, BKnight) == True

    assert model_check(knowledge1, AKnight) == False
    assert model_check(knowledge1, BKnave) == False
    assert model_check(knowledge1, CKnight) == False
    assert model_check(knowledge1, CKnave) == False


def test_puzzle2():
    # AKnave, BKnight
    assert model_check(knowledge2, AKnave) == True
    assert model_check(knowledge2, BKnight) == True

    assert model_check(knowledge2, AKnight) == False
    assert model_check(knowledge2, BKnave) == False
    assert model_check(knowledge2, CKnight) == False
    assert model_check(knowledge2, CKnave) == False


def test_puzzle3():
    # AKnight, BKnave, CKnight
    assert model_check(knowledge3, AKnight) == True
    assert model_check(knowledge3, BKnave) == True
    assert model_check(knowledge3, CKnight) == True

    assert model_check(knowledge3, AKnave) == False
    assert model_check(knowledge3, BKnight) == False
    assert model_check(knowledge3, CKnave) == False
