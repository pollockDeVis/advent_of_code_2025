






if __name__ == "__main__":
    # Read the txt file which has lines strings separated by newlines
    with open("input_day6.txt", "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]


    # Last line contains the operators
    operators = lines[-1]
    data_lines = lines[:-1]

    # Get rid of white spaces in operators
    operators = operators.replace(" ", "")
    # Split operators into a list
    operators = list(operators)

    # convert data_lines into list of integers
    data_lines = [[int(value) for value in line.split()] for line in data_lines]

    print(len(data_lines[0] ), "data lines read.")
    print("Total lines including operators line:", len(operators))
    print("Operators:", operators)
    print("Data lines:", data_lines)

    # Each column in data_lines needs to be processed with the corresponding operator
    sum = 0
    for col_index in range(len(data_lines[0])):
        column_values = [line[col_index] for line in data_lines]
        print(f"Column {col_index} values:", column_values)

        operator = operators[col_index]

        if operator == "*":
            # Multiply all values in the column
            result = 1
            for value in column_values:
                result *= value
            print("result multi: ", result)
            sum += result
        elif operator == "+":
            result = 0
            # Sum the integer values in the column
            for value in column_values:
                result += value
            print("result add: ", result)
            sum += result

    print("Final sum after applying all operators:", sum)