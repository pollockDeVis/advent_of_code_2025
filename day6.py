






if __name__ == "__main__":
    # Read the txt file which has lines strings separated by newlines
    with open("input_day6.txt", "r") as file:
        lines = file.readlines()
        # lines = [line.strip() for line in lines] # 

    # print("Data lines before processing:", lines)
    # Length of data lines

    print("Length of data lines:", len(lines), len(lines[0]))

    print("Length of LAST data lines:", len(lines), len(lines[-1]))

    combined_number_list = []
    operation_flag = False
    operator = ""
    results = []
    for colidx in range(len(lines[-1]), 0, -1):
        # print("Column index:", colidx)
        numbers = []
        
        for rowidx in range(len(lines)):
            # print("Row index:", rowidx, "Value:", lines[rowidx][colidx-1])
            
            # Print the type of the character
            # print("Type of character:", type(lines[rowidx][colidx-1]))

            if lines[rowidx][colidx-1] != " " and lines[rowidx][colidx-1] != "\n":
                if lines[rowidx][colidx-1].isdigit():
                    numbers.append(int(lines[rowidx][colidx-1]))

            if lines[rowidx][colidx-1] == "*" or lines[rowidx][colidx-1] == "+":
                # print("Found operator: ", lines[rowidx][colidx-1])
                operation_flag = True
                operator = lines[rowidx][colidx-1]
                # print("Numbers collected so far for column", colidx, "are:", combined_number_list)

            

        # if numbers list is not empty, combine the digits to form a number
        if numbers:
            combined_number = 0
            for digit in numbers:
                combined_number = combined_number * 10 + digit
            # print("Combined number for column", colidx, "is:", combined_number)
            combined_number_list.append(combined_number)
            # print("Combined number list for column", colidx, "is:", combined_number_list)

        if operation_flag:
            # print("Performing operation:", operator, "on combined number list:", combined_number_list)
            if operator == "+":
                result = sum(combined_number_list)
                results.append(result)
            elif operator == "*":
                result = 1
                for num in combined_number_list:
                    result *= num
                # print("Result of multiplication:", result)
                results.append(result)
            # Reset for next operation
            combined_number_list = []
            operation_flag = False
            operator = ""


    print("Final results after all operations:", results)
    print("Final results sum:", sum(results))

        




