# CS50's Introduction to Artificial Intelligence Test Scripts

## 🤷‍♂️ What's this? 🤷‍♀️

This repository contains Python scripts to automate tests for most of the [CS50’s Introduction to Artificial Intelligence with Python projects](https://github.com/jetkan-yk/cs50ai).</br>

It **does not** contain any project *solution*/*spoiler*, as per the course's [Academic Honesty policy](https://cs50.harvard.edu/ai/2020/honesty/).

## ⛔ Disclaimer

This is a student-initiated project. Passing these test cases **does not** guarantee that you will receive a full grade from the official CS50 AI's teaching team.

## 📖 Table of Contents

| Lecture                                                   | Concept                                                                                                      | Project                                                                 | Test Script                                | Description                                                                                                                                                                               |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Search](https://cs50.harvard.edu/ai/2020/weeks/0/)       | [Breadth First Search](https://cs50.harvard.edu/ai/2020/notes/0/#breadth-first-search)                       | [Degrees](https://cs50.harvard.edu/ai/2020/projects/0/degrees/)         | [degrees_test.py](degrees_test.py)         | Run test cases given by problem description and [this discussion](https://edstem.org/us/courses/176/discussion/226814?answer=546980)                                                      |
| [Search](https://cs50.harvard.edu/ai/2020/weeks/0/)       | [Minimax](https://cs50.harvard.edu/ai/2020/notes/0/#minimax)                                                 | [Tic-Tac-Toe](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)   | [tictactoe_test.py](tictactoe_test.py)     | Let your AI play against itself for 10 rounds                                                                                                                                             |
| [Knowledge](https://cs50.harvard.edu/ai/2020/weeks/1/)    | [Model Checking](https://cs50.harvard.edu/ai/2020/notes/1/#inference)                                        | [Knights](https://cs50.harvard.edu/ai/2020/projects/1/knights/)         | [puzzle_test.py](puzzle_test.py)           | Check the correctness of the 4 puzzle results                                                                                                                                             |
| [Knowledge](https://cs50.harvard.edu/ai/2020/weeks/1/)    | [Knowledge Engineering](https://cs50.harvard.edu/ai/2020/notes/1/#knowledge-engineering)                     | [Minesweeper](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/) | [minesweeper_test.py](minesweeper_test.py) | Check if your AI has ≈90% win rate over 1000 simulations                                                                                                                                  |
| [Uncertainty](https://cs50.harvard.edu/ai/2020/weeks/2/)  | [Bayesian Networks](https://cs50.harvard.edu/ai/2020/notes/2/#bayesian-networks)                             | [Heredity](https://cs50.harvard.edu/ai/2020/projects/2/heredity/)       | [heredity_test.py](heredity_test.py)       | Run test cases given by problem description and [this discussion](https://edstem.org/us/courses/176/discussion/488564?answer=1263763)                                                     |
| [Uncertainty](https://cs50.harvard.edu/ai/2020/weeks/2/)  | [Markov Models](https://cs50.harvard.edu/ai/2020/notes/2/#markov-models)                                     | [PageRank](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/)       | [pagerank_test.py](pagerank_test.py)       | Compare the output of the 2 implemented functions                                                                                                                                         |
| [Optimization](https://cs50.harvard.edu/ai/2020/weeks/3/) | [Constraint Satisfaction](https://cs50.harvard.edu/ai/2020/notes/3/#constraint-satisfaction)                 | [Crossword](https://cs50.harvard.edu/ai/2020/projects/3/crossword/)     | [generate_test.py](generate_test.py)       | Generate crosswords using all 9 different structure + words combination and a special test case from [this discussion](https://edstem.org/us/courses/176/discussion/103609?answer=280445) |
| [Learning](https://cs50.harvard.edu/ai/2020/weeks/4/)     | [Nearest-Neighbor Classification](https://cs50.harvard.edu/ai/2020/notes/4/#nearest-neighbor-classification) | [Shopping](https://cs50.harvard.edu/ai/2020/projects/4/shopping/)       | [shopping_test.py](shopping_test.py)       | Check the information is parsed correctly and result is within a reasonable range                                                                                                         |
| [Learning](https://cs50.harvard.edu/ai/2020/weeks/4/)     | [Reinforcement Learning](https://cs50.harvard.edu/ai/2020/notes/4/#reinforcement-learning)                   | [Nim](https://cs50.harvard.edu/ai/2020/projects/4/nim/)                 | [nim_test.py](nim_test.py)                 | Check if the AI which moves second has a 100% win rate                                                                                                                                    |

## 🛠️ How to Run Tests

### Guide

1. Make sure you have [Python3](https://www.python.org/downloads/) installed in your machine. Anything above `Python 3.4+` should work.
2. Install `pytest` by running `pip install pytest` in a terminal. More information about `pip` [here](https://realpython.com/what-is-pip/).
3. Make a copy of the test file and paste it in the **same folder** as the project that you want to test.
    > For example, if you want to test your code for `degrees.py`, make a copy of `degrees_test.py` in the **same folder** as your `degrees.py` and other files that came along with the project, like `util.py`, `large/` and `small/`.
4. Navigate to the project folder and run `pytest` or `pytest <project>_test.py` in a terminal.
    > For example, navigate to `degrees/` and run `pytest` or `pytest degrees_test.py`.

### Example

![example](https://user-images.githubusercontent.com/36299141/128583985-a56b4371-a092-430a-8c08-4483137367d6.png)

## 🚩 Useful pytest Flags

- Run `pytest -s` to show print statements in the console
- Run `pytest -vv` for verbose mode
- Combine both flags `pytest -s -vv` for extra verbose mode
- Run `pytest --durations=n` to see the `n` slowest execution time
- Install `pytest-repeat` with `pip` and then run `pytest --count n` to repeat the test for *n* times

## 💻 My Setup

Each test should take less than 30 seconds, depending on Python's I/O and your code efficiency.

- Windows 10 Home Build 19042
- Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- Python 3.9.5 64-bit
- Visual Studio Code w/Pylance (latest release)

## 🏆 Acknowledgement

Special thanks to these fellow CS50AI classmates who contributed some of the test cases on the [Ed discussion site](https://edstem.org/us/courses/176/discussion/)!

- Ken Walker
- Naveena A S
- Ricardo L
