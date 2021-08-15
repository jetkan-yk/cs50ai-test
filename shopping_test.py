"""
Acceptance tests for shopping.py

Make sure that this file is in the same directory as shopping.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""

import csv

import numpy as np

from shopping import TEST_SIZE, evaluate, load_data, train_model, train_test_split

FILENAME = "shopping.csv"

expected0 = [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]


def test():
    with open(FILENAME) as f:
        reader = csv.reader(f)
        next(reader)

        N = p = f = 0
        for row in reader:
            N += 1
            if row[-1] == "TRUE":
                p += 1
            elif row[-1] == "FALSE":
                f += 1
            else:
                raise KeyError("DO NOT EDIT shopping.csv FILE!!!")

    evidence, labels = load_data(FILENAME)
    assert len(evidence) == len(labels) == N
    if type(evidence).__module__ == np.__name__:
        assert (evidence[0] == expected0).all()
    else:
        assert evidence[0] == expected0
    assert labels[0] == 0

    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    assert y_test.size == N * TEST_SIZE
    assert 0.35 <= sensitivity <= 0.45
    assert 0.85 <= specificity <= 0.95
