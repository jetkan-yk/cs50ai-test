"""
Regression tests for pagerank.py

Make sure that this file is in the same directory as pagerank.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import random as rd

import pytest as pt

from pagerank import DAMPING, SAMPLES, crawl, iterate_pagerank, sample_pagerank

PRECISION = 1e-2  # Absolute error tolerance = ±0.01

corpus0 = crawl("corpus0")


def test_crawl0():
    assert len(corpus0) == 4


def test_sample0():
    expected = {"1.html": 0.2223, "2.html": 0.4303, "3.html": 0.2145, "4.html": 0.1329}
    sample = sample_pagerank(corpus0, damping_factor=DAMPING, n=SAMPLES)
    return compare(sample, expected)


def test_iterate0():
    expected = {"1.html": 0.2202, "2.html": 0.4289, "3.html": 0.2202, "4.html": 0.1307}
    iterate = iterate_pagerank(corpus0, damping_factor=DAMPING)
    return compare(iterate, expected)


@pt.mark.parametrize("execution_number", range(10))
def test_sample_vs_iterate(execution_number):
    return run_sample_vs_iterate()


# helper function


def run_sample_vs_iterate():
    corpus, _ = generate_random_data()

    sample = sample_pagerank(corpus, damping_factor=DAMPING, n=SAMPLES)
    iterate = iterate_pagerank(corpus, damping_factor=DAMPING)

    return compare(sample, iterate)


def compare(prob1, prob2):
    for page in prob1.keys():
        assert prob1[page] == pt.approx(prob2[page], abs=PRECISION)


def generate_random_data():
    links = [f"{i}.html" for i in range(rd.randint(1, 10))]
    page = rd.choice(links)
    corpus = {
        link: set(rd.choices(links, k=rd.randint(0, len(links)))) - set([link])
        for link in links
    }
    return corpus, page
