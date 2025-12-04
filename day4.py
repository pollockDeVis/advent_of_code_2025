

def get_indices_with_few_neighbors(data, threshold=4):
    rows = len(data)
    cols = len(data[0])
    neighbour_count_per_element = {}
    for row in range(rows):
        for col in range(cols):
            element = data[row][col]
            neighbour_count = 0
            if element == "@":
                for r in range(max(0, row-1), min(rows, row+2)):
                    for c in range(max(0, col-1), min(cols, col+2)):
                        if (r, c) != (row, col):
                            neighbor = data[r][c]
                            if neighbor == "@":
                                neighbour_count += 1
                neighbour_count_per_element[(row, col)] = neighbour_count
    indices_less_than_threshold = [index for index, count in neighbour_count_per_element.items() if count < threshold]
    return indices_less_than_threshold
    


if __name__ == "__main__":



    # Read the txt file which has lines strings separated by newlines
    with open("input_day4.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    # Put the data in a 2D matrix accessible by lines[row][col]
    data = [list(line) for line in lines]


    indices_less_than_4 = [(0, 2), (0, 3), (0, 5), (0, 6), (0, 8), (1, 0), (2, 6), (4, 0), (4, 9), (7, 0), (9, 0), (9, 2), (9, 8)]
    total_length = 0
    while indices_less_than_4 != []:

        indices_less_than_4 = get_indices_with_few_neighbors(data, threshold=4)
        # print("Length of indices with less than 4 neighbors:", len(indices_less_than_4))
        # print(f"Indices of elements with less than 4 '@' neighbors: {indices_less_than_4}")

        total_length += len(indices_less_than_4)

        # Use this indices to change the original data matrix from "@" to "."
        for index in indices_less_than_4:
            row, col = index
            data[row][col] = "."

    print("FINAL Length of indices with less than 4 neighbors:", len(indices_less_than_4))
    print("TOTAL Length accumulated:", total_length)

    