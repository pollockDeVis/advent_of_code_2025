"""Tests for Day 1 solution."""

import pytest
from day01.solution import parse_input, solve_part1, solve_part2, solve


EXAMPLE_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3
"""


class TestParsing:
    def test_parse_example(self):
        left, right = parse_input(EXAMPLE_INPUT)
        assert left == [3, 4, 2, 1, 3, 3]
        assert right == [4, 3, 5, 3, 9, 3]

    def test_parse_empty_lines(self):
        input_text = """1   2

3   4
"""
        left, right = parse_input(input_text)
        assert left == [1, 3]
        assert right == [2, 4]


class TestPart1:
    def test_example(self):
        left, right = parse_input(EXAMPLE_INPUT)
        assert solve_part1(left, right) == 11

    def test_single_pair(self):
        assert solve_part1([5], [3]) == 2

    def test_identical_lists(self):
        left = [1, 2, 3]
        right = [1, 2, 3]
        assert solve_part1(left, right) == 0


class TestPart2:
    def test_example(self):
        left, right = parse_input(EXAMPLE_INPUT)
        assert solve_part2(left, right) == 31

    def test_no_matches(self):
        left = [1, 2, 3]
        right = [4, 5, 6]
        assert solve_part2(left, right) == 0

    def test_all_matches(self):
        left = [2, 2]
        right = [2, 2, 2]
        # 2 appears 3 times: 2*3 + 2*3 = 12
        assert solve_part2(left, right) == 12


class TestSolve:
    def test_example(self):
        part1, part2 = solve(EXAMPLE_INPUT)
        assert part1 == 11
        assert part2 == 31
