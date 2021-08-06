# CS50's Introduction to Artificial Intelligence with Python Test Script

## 🤷‍♂️ What's this? 🤷‍♀️

This repository contains Python scripts to automate tests for most of the CS50 AI projects. It **does not** contain *solution*/*spoiler* to the projects, as per the course's [Academic Honesty policy](https://cs50.harvard.edu/ai/2020/honesty/). Students who are taking this course are allowed to use these Python script to test their code before (re-)submission.

## :trollface: Disclaimer

This is a student-initiated project. Passing these test cases **does not** guarantee that you will receive a full grade from the HavardX teaching team.

## 📖 Table of Contents

| Week                                           | Lecture                                     | Concept                                                                                  | Name                                                                    | Test Case                                  |
| ---------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------ |
| [0](https://cs50.harvard.edu/ai/2020/weeks/0/) | [Search](https://youtu.be/WbzNRTTrX0g)      | [BFS](https://cs50.harvard.edu/ai/2020/notes/0/#breadth-first-search)                    | [Degrees](https://cs50.harvard.edu/ai/2020/projects/0/degrees/)         | [degrees_test.py](degrees_test.py)         |
| [0](https://cs50.harvard.edu/ai/2020/weeks/0/) | [Search](https://youtu.be/WbzNRTTrX0g)      | [Minimax](https://cs50.harvard.edu/ai/2020/notes/0/#minimax)                             | [Tic-Tac-Toe](https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/)   | [tictactoe_test.py](tictactoe_test.py)     |
| [1](https://cs50.harvard.edu/ai/2020/weeks/1/) | [Knowledge](https://youtu.be/HWQLez87vqM)   | [Model Checking](https://cs50.harvard.edu/ai/2020/notes/1/#inference)                    | [Knights](https://cs50.harvard.edu/ai/2020/projects/1/knights/)         | [puzzle_test.py](puzzle_test.py)           |
| [1](https://cs50.harvard.edu/ai/2020/weeks/1/) | [Knowledge](https://youtu.be/HWQLez87vqM)   | [Knowledge Engineering](https://cs50.harvard.edu/ai/2020/notes/1/#knowledge-engineering) | [Minesweeper](https://cs50.harvard.edu/ai/2020/projects/1/minesweeper/) | [minesweeper_test.py](minesweeper_test.py) |
| [2](https://cs50.harvard.edu/ai/2020/weeks/2/) | [Uncertainty](https://youtu.be/D8RRq3TbtHU) | [Bayesian Networks](https://cs50.harvard.edu/ai/2020/notes/2/#bayesian-networks)         | [Heredity](https://cs50.harvard.edu/ai/2020/projects/2/heredity/)       | [heredity_test.py](heredity_test.py)       |
| [2](https://cs50.harvard.edu/ai/2020/weeks/2/) | [Uncertainty](https://youtu.be/D8RRq3TbtHU) | [Markov Models](https://cs50.harvard.edu/ai/2020/notes/2/#markov-models)                 | [PageRank](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/)       |

## 🛠️ How to Run Tests

1. Make sure you have [Python3](https://www.python.org/downloads/) installed in your machine. Anything above `Python 3.4` should work.
2. Install `pytest` by running `pip install pytest` in a terminal. More information about `pip` [here](https://realpython.com/what-is-pip/).
3. Make a copy of the test file and paste it in the **same folder** as the project that you want to test.
    > For example, if you want to test your code for `degrees.py`, make a copy of `degrees_test.py` in the **same folder** as your `degrees.py` and other files that came along with the project, like `util.py`, `large/` and `small/`.
4. Navigate to the project folder and run `pytest` or `pytest <project>_test.py` in a terminal.
    > For example, navigate to `degrees/` and run `pytest` or `pytest degrees_test.py`.

## 🚩 Useful pytest Flags

- Run `pytest -s` to show print statements in the console
- Run `pytest -vv` for verbose mode
- Install `pyrepeat` with `pip` and then run `pytest --count n` to repeat the test for *n* times

## 💻 My Setup

Each test case should take less than 30 seconds, depending on Python's I/O and your code efficiency.

- Windows 10 Home Build 19042
- Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
- Python 3.9.5 64-bit
- Visual Studio Code w/Pylance (latest release)

## 🤹 Improvement

I am currently auditing this course (no certificate bearing, just interested in AI and Brian's teaching style), more solutions and test cases will be added in the near future!
