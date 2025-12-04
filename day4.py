

if __name__ == "__main__":



    # Read the txt file which has lines strings separated by newlines
    with open("input_day4.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    # Put the data in a 2D matrix accessible by lines[row][col]
    data = [list(line) for line in lines]

    # Print the rows and columns length
    rows = len(data)
    cols = len(data[0])
    # print(f"Rows: {rows}, Cols: {cols}")

    neighbour_count_per_element = {}
    global_neighbour_count = {}
    # Loop through the matrix and assess each element
    for row in range(rows):
        for col in range(cols):
            element = data[row][col]
            # Do something with each element
            neighbour_count = 0
            global_neighbour_count = 0
            if element == "@":
                # print(f"Found '@' at ({row},{col})")
                # Now check the surrounding 8 elements
                for r in range(max(0, row-1), min(rows, row+2)):
                    for c in range(max(0, col-1), min(cols, col+2)):
                        if (r, c) != (row, col):
                            neighbor = data[r][c]
                            print(f"  Neighbor at ({r},{c}): {neighbor}")
                            # Increment if neighbor is "@"
                            if neighbor == "@":
                                neighbour_count += 1

                neighbour_count_per_element[(row, col)] = neighbour_count
            global_neighbour_count[(row, col)] = neighbour_count
    
    # Get the number of elements that have count less than 4
    count_less_than_4 = sum(1 for count in neighbour_count_per_element.values() if count < 4)
    global_count_less_than_4 = sum(1 for count in global_neighbour_count.values() if count < 4)
    print(f"Number of elements with less than 4 '@' neighbors: {count_less_than_4}")
    print(f"Global number of elements with less than 4 '@' neighbors: {global_count_less_than_4}")