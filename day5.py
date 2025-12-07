



if __name__ == "__main__":
    # Read the txt file which has lines strings separated by newlines
    with open("input_day5.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    # Lines contain ranges and numbers separated by blank space in one element
    ranges = []
    numbers = []

    # Find the empty line index
    empty_line_index = lines.index("")

    ranges = lines[:empty_line_index]
    numbers = lines[empty_line_index + 1 :]

        
    # print("Ranges:", ranges)
    # print("Numbers:", numbers)

    # Convert numbers to a set of integers for quick lookup
    number_set = set(int(num) for num in numbers)

    # Convert ranges to tuples of upper and lower bounds
    all_numbers_in_ranges = []
    for range_str in ranges:
        start_str, end_str = range_str.split("-")
        start = int(start_str)
        end = int(end_str)
        tuple_of_range = (start, end)
        all_numbers_in_ranges.append(tuple_of_range)


    print("All numbers in ranges as tuples:", all_numbers_in_ranges)

    # Check if the numbers fall within any of the given ranges
    valid_numbers = []
    for number in number_set:
        for (start, end) in all_numbers_in_ranges:
            if start <= number <= end:
                valid_numbers.append(number)
                break  # No need to check other ranges once a match is found

    print("Valid numbers within the given ranges:", len(valid_numbers))

    total_numbers_in_range = 0
    # Count total numbers covered by all ranges with overlaps
    # First sort the ranges by their start values
    all_numbers_in_ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    for current_range in all_numbers_in_ranges:
        if not merged_ranges:
            merged_ranges.append(current_range)
        else:
            last_range = merged_ranges[-1]
            if current_range[0] <= last_range[1]:  # Overlap detected
                # Merge the ranges
                merged_ranges[-1] = (last_range[0], max(last_range[1], current_range[1]))
            else:
                merged_ranges.append(current_range)


    for (start, end) in merged_ranges:
        total_numbers_in_range += (end - start + 1)

    print("Total numbers covered by all ranges (merged):", total_numbers_in_range)