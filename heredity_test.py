"""
Acceptance tests for heredity.py

Make sure that this file is in the same directory as heredity.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from heredity import joint_probability, load_data, normalize, powerset, update

PRECISION = 4


# Test cases provided by Naveena A S. Thank you!
# source: https://edstem.org/us/courses/176/discussion/488564?answer=1263763


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

    return compare(predicted, expected)


def test_family1():
    expected = {
        "Arthur": {
            "gene": {2: 0.0329, 1: 0.1035, 0: 0.8636},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Charlie": {
            "gene": {2: 0.0018, 1: 0.1331, 0: 0.8651},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Fred": {
            "gene": {2: 0.0065, 1: 0.6486, 0: 0.3449},
            "trait": {True: 1.0000, False: 0.0000},
        },
        "Ginny": {
            "gene": {2: 0.0027, 1: 0.1805, 0: 0.8168},
            "trait": {True: 0.1110, False: 0.8890},
        },
        "Molly": {
            "gene": {2: 0.0329, 1: 0.1035, 0: 0.8636},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Ron": {
            "gene": {2: 0.0027, 1: 0.1805, 0: 0.8168},
            "trait": {True: 0.1110, False: 0.8890},
        },
    }

    predicted = predict_family(1)

    return compare(predicted, expected)


def test_family2():
    expected = {
        "Arthur": {
            "gene": {2: 0.0147, 1: 0.0344, 0: 0.9509},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Hermione": {
            "gene": {2: 0.0608, 1: 0.1203, 0: 0.8189},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Molly": {
            "gene": {2: 0.0404, 1: 0.0744, 0: 0.8852},
            "trait": {True: 0.0768, False: 0.9232},
        },
        "Ron": {
            "gene": {2: 0.0043, 1: 0.2149, 0: 0.7808},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Rose": {
            "gene": {2: 0.0088, 1: 0.7022, 0: 0.2890},
            "trait": {True: 1.0000, False: 0.0000},
        },
    }

    predicted = predict_family(2)

    return compare(predicted, expected)


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
            for kOutcome, vOutcome in vVariable.items():
                assert (
                    round(vOutcome, PRECISION) == expected[kPerson][kVariable][kOutcome]
                )
