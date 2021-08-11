"""
Acceptance tests for puzzle.py

Make sure that this file is in the same directory as puzzle.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from puzzle import *


def test_puzzle0():
    # AKnave
    assert model_check(knowledge0, AKnave) is True

    assert model_check(knowledge0, AKnight) is False
    assert model_check(knowledge0, BKnight) is False
    assert model_check(knowledge0, BKnave) is False
    assert model_check(knowledge0, CKnight) is False
    assert model_check(knowledge0, CKnave) is False


def test_puzzle1():
    # AKnave, BKnight
    assert model_check(knowledge1, AKnave) is True
    assert model_check(knowledge1, BKnight) is True

    assert model_check(knowledge1, AKnight) is False
    assert model_check(knowledge1, BKnave) is False
    assert model_check(knowledge1, CKnight) is False
    assert model_check(knowledge1, CKnave) is False


def test_puzzle2():
    # AKnave, BKnight
    assert model_check(knowledge2, AKnave) is True
    assert model_check(knowledge2, BKnight) is True

    assert model_check(knowledge2, AKnight) is False
    assert model_check(knowledge2, BKnave) is False
    assert model_check(knowledge2, CKnight) is False
    assert model_check(knowledge2, CKnave) is False


def test_puzzle3():
    # AKnight, BKnave, CKnight
    assert model_check(knowledge3, AKnight) is True
    assert model_check(knowledge3, BKnave) is True
    assert model_check(knowledge3, CKnight) is True

    assert model_check(knowledge3, AKnave) is False
    assert model_check(knowledge3, BKnight) is False
    assert model_check(knowledge3, CKnave) is False
