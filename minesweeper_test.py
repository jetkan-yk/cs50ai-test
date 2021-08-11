"""
Acceptance tests for minesweeper.py

Make sure that this file is in the same directory as minesweeper.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest as pt

from minesweeper import Minesweeper, MinesweeperAI

# Feel free to change these numbers for different expectation
HEIGHT = 12
WIDTH = 12
MINES = 8
expectedWinPercent = 85

# Run the AI test for 10 times. Each test consists of letting the AI play
# minesweeper for 1000 rounds. If the inference function is implemented correctly,
# each test should have a very high win rate (≈90%) in most of the iterations.
# Use `pytest -s` to see win rate.


@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    return play1000()


# Helper functions


def play1000():
    totalWon = 0
    for _ in range(1000):
        totalWon += play()

    print(f"\nWin rate:{totalWon // 10}%")

    assert totalWon >= expectedWinPercent * 10


def play():
    game = Minesweeper(height=HEIGHT, width=WIDTH, mines=MINES)
    ai = MinesweeperAI(height=HEIGHT, width=WIDTH)

    won = lost = False
    while not (won or lost):
        # AI choose a move
        move = ai.make_safe_move() or ai.make_random_move()
        if move is None:
            won = True
            break

        # Make move and update AI
        if game.is_mine(move):
            lost = True
        else:
            nearby = game.nearby_mines(move)
            ai.add_knowledge(move, nearby)

    return won
