"""
Acceptance tests for degrees.py

Make sure that this file is in the same directory as degrees.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from degrees import load_data, person_id_for_name, shortest_path

load_data("large")

# Most test cases provided by Ken Walker. Thank you!
# source: https://edstem.org/us/courses/176/discussion/226814?answer=546980


def test0():
    source = person_id_for_name("Jennifer Lawrence")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2


def test1():
    source = person_id_for_name("Emma Watson")
    target = person_id_for_name("Jennifer Lawrence")
    assert len(shortest_path(source, target)) == 3


def test_zero_degree():
    source = person_id_for_name("Tim Zinnemann")
    target = person_id_for_name("Lahcen Zinoun")
    assert shortest_path(source, target) is None


def test_one_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Lea Thompson")
    assert len(shortest_path(source, target)) == 1


def test_two_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2


def test_three_degree():
    source = person_id_for_name("Emma Watson")
    target = person_id_for_name("Jennifer Lawrence")
    assert len(shortest_path(source, target)) == 3


def test_four_degree():
    source = person_id_for_name("Fred Astaire")
    target = person_id_for_name("Mohamed Zinet")
    assert len(shortest_path(source, target)) == 4


def test_six_degree():
    source = person_id_for_name("Juliane Banse")
    target = person_id_for_name("Bruce Davison")
    assert len(shortest_path(source, target)) == 6


def test_eight_degree():
    source = person_id_for_name("Juliane Banse")
    target = person_id_for_name("Julian Acosta")
    assert len(shortest_path(source, target)) == 8
