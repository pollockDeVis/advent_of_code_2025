"""
Advent of Code 2025 - Day 1: Historian Hysteria

This puzzle involves comparing two lists of location IDs.

Part 1: Calculate the total distance between sorted pairs of numbers.
Part 2: Calculate a similarity score based on how often each number
        from the left list appears in the right list.
"""


def parse_input(input_text: str) -> tuple[list[int], list[int]]:
    """Parse the input text into two lists of integers."""
    left_list = []
    right_list = []
    
    for line in input_text.strip().split('\n'):
        if line.strip():
            parts = line.split()
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
    
    return left_list, right_list


def solve_part1(left_list: list[int], right_list: list[int]) -> int:
    """
    Calculate the total distance between sorted pairs.
    
    Sort both lists and sum the absolute differences between
    corresponding elements.
    """
    sorted_left = sorted(left_list)
    sorted_right = sorted(right_list)
    
    total_distance = sum(
        abs(left - right) 
        for left, right in zip(sorted_left, sorted_right)
    )
    
    return total_distance


def solve_part2(left_list: list[int], right_list: list[int]) -> int:
    """
    Calculate the similarity score.
    
    For each number in the left list, multiply it by the number of times
    it appears in the right list. Sum all these products.
    """
    from collections import Counter
    
    right_counts = Counter(right_list)
    
    similarity_score = sum(
        num * right_counts.get(num, 0)
        for num in left_list
    )
    
    return similarity_score


def solve(input_text: str) -> tuple[int, int]:
    """Solve both parts of the puzzle."""
    left_list, right_list = parse_input(input_text)
    
    part1 = solve_part1(left_list, right_list)
    part2 = solve_part2(left_list, right_list)
    
    return part1, part2


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    part1, part2 = solve(input_text)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
