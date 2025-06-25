# Новіцький КП-41мп
# Renju

This project implements a Python program to determine the winner of a **Renju** game based on a given board configuration.

## Game Description

Renju is a strategic two-player board game played on a **19×19 grid**. One player places **black stones** (`1`) and the other places **white stones** (`2`). Players alternate turns, starting with black.

The goal is to place **exactly five consecutive stones** of the same color in a row — **horizontally**, **vertically**, or **diagonally**. If more than five are placed, it does **not** count as a win.

There will be no cases where both players win or a player wins in multiple locations.

## Input Format

- The input is taken from `input.txt`.
- The first line contains a single integer `x` (1 ≤ x ≤ 11) — the number of test cases.
- Each test case consists of **19 lines**, each containing **19 integers**:
  - `1` for black stone
  - `2` for white stone
  - `0` for an empty intersection

## Output Format

- The output is written to `output.txt`.
- For each test case:
  - First line: `1` if black wins, `2` if white wins, or `0` if nobody wins.
  - If someone wins, second line: the **row** and **column** of the **leftmost (or topmost)** stone among the five consecutive.
