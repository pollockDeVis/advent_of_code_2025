# Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) puzzles in Python.

## Project Structure

```
advent_of_code_2025/
├── day01/
│   ├── __init__.py
│   ├── solution.py      # Solution for Day 1
│   ├── example.txt      # Example input
│   └── test_solution.py # Tests
├── README.md
└── .gitignore
```

## Running Solutions

Each day's solution can be run as a module:

```bash
# Run with file input
python -m day01.solution day01/input.txt

# Run with stdin
cat day01/input.txt | python -m day01.solution
```

## Running Tests

```bash
# Install pytest
pip install pytest

# Run all tests
python -m pytest

# Run specific day's tests
python -m pytest day01/test_solution.py -v
```

## Days Completed

- [x] Day 1: Historian Hysteria