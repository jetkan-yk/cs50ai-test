"""
Acceptance tests for tictactoe.py

Make sure that this file is in the same directory as tictactoe.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest as pt

import tictactoe as ttt

# Let the AI play against itself for 10 times. If the minimax function
# is implemented correctly, every round should resolve in a tie.


@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    return play_ai_vs_ai()


# Helper function


def play_ai_vs_ai():
    board = ttt.initial_state()
    game_over = False

    while not game_over:
        move = ttt.minimax(board)
        board = ttt.result(board, move)
        game_over = ttt.terminal(board)

    assert ttt.winner(board) is None
