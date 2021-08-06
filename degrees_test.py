"""
Regression tests for degrees.py

Make sure that you placed this file in the same directory as degrees.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from degrees import load_data, person_id_for_name, shortest_path

load_data("small")


def test_two_degrees():
    source = person_id_for_name("Jennifer Lawrence")
    target = person_id_for_name("Tom Hanks")
    assert shortest_path(source, target) == 2


def test_three_degrees():
    source = person_id_for_name("Emma Watson")
    target = person_id_for_name("Jennifer Lawrence")
    assert shortest_path(source, target) == 3
