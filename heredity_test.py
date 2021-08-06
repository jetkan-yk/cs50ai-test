"""
Regression tests for heredity.py

Make sure that this file is in the same directory as heredity.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest as pt

from heredity import joint_probability, load_data, normalize, powerset, update

PRECISION = 1e-4


def test_family0():
    expected = {
        "Harry": {
            "gene": {2: 0.0092, 1: 0.4557, 0: 0.5351},
            "trait": {True: 0.2665, False: 0.7335},
        },
        "James": {
            "gene": {2: 0.1976, 1: 0.5106, 0: 0.2918},
            "trait": {True: 1.0000, False: 0.0000},
        },
        "Lily": {
            "gene": {2: 0.0036, 1: 0.0136, 0: 0.9827},
            "trait": {True: 0.0000, False: 1.0000},
        },
    }

    predicted = predict_family(0)

    compare(predicted, expected)


# Helper functions


def predict_family(n):
    people = load_data(f"data/family{n}.csv")

    probabilities = {
        person: {"gene": {2: 0, 1: 0, 0: 0}, "trait": {True: 0, False: 0}}
        for person in people
    }

    names = set(people)
    for have_trait in powerset(names):
        fails_evidence = any(
            (
                people[person]["trait"] is not None
                and people[person]["trait"] != (person in have_trait)
            )
            for person in names
        )
        if fails_evidence:
            continue

        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    normalize(probabilities)

    return probabilities


def compare(predicted, expected):
    for kPerson, vPerson in predicted.items():
        for kVariable, vVariable in vPerson.items():
            assert vVariable == pt.approx(expected[kPerson][kVariable], abs=PRECISION)
