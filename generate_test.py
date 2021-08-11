"""
Acceptance tests for generate.py

Make sure that this file is in the same directory as generate.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest

from generate import Crossword, CrosswordCreator

invalid_crossword = [(1, 0), (2, 0)]  # These 2 combinations will not work

# Pro tip: run `pytest --durations=10` to see the 10 slowest executions


@pytest.mark.parametrize("execution", range(10))
@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test(execution, i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()
    generate_output(creator, assignment, f"data/output{i}-{j}.png")

    if (i, j) in invalid_crossword:
        assert assignment is None
    else:
        assert len(assignment) == len(crossword.variables)


# Special test case written by Ricardo L. Thank you!
# If the backtracking search and inference algorithm are implemented correctly,
# this crossword should be solved in 5 seconds.

# source: https://edstem.org/us/courses/176/discussion/103609?answer=280445


def test_optimization():
    write_structure3()
    crossword = Crossword("data/structure3.txt", "data/words2.txt")
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()
    generate_output(creator, assignment, f"data/output3-2.png")

    assert len(assignment) == len(crossword.variables)


# helper function


def generate_output(creator, assignment, file):
    if assignment is None:
        print("No solution")
    else:
        creator.print(assignment)
        creator.save(assignment, file)


def generate_crossword(i, j):
    structure = f"data/structure{i}.txt"
    words = f"data/words{j}.txt"
    print(f"\nTesting structure{i} words{j}")
    return Crossword(structure, words)


def write_structure3():
    structure = """\
#########################
#########################
#########################
#_____________##_______##
#_##_##_#_#_#_###_#_#_###
#_##_##_#_#_#_##_______##
#_____________###_#_#_###
#_##_##_##_##_##_______##
#_##_##_##_##_###_#_#_###
#_____________##_______##
#####__#####_###_########
#####__#####_____########
####_##_######_##########
####____######_##########
####_##_######_##########
####_##_######_##########
####_##_####_____########
#########################
#########################
#########################"""
    f = open("data/structure3.txt", "w")
    f.write(structure)
    f.close
