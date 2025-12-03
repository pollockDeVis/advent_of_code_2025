# Method that inputs a list of digits, and window size, selects the maximum number and then looks for the second maximum number in the list by sliding the window across the list of digits, ensuring that the remaining digit falls within the window and doesn't exceed list length.
def recursive_number_extractor(number_list, window_size):
    length = len(number_list)

    max_list = []
    def find_max_recursive(start_index, max_list):
        if len(max_list) >= window_size:
            return
        max_number = -1
        max_index = -1
        for i in range(start_index, length):
            # print("Start Index:", start_index, "Current Index:", i, "Max List:", max_list)
            # Adjust window size once the list is not empty
            current_window_size = window_size - len(max_list)



            if number_list[i] > max_number and (i + current_window_size) <= length:
                max_number = number_list[i]
                max_index = i
            # Edge condition, when the first number is the last possible maximum
            elif i == (length - window_size) + 1 and max_number == -1:
                max_number = number_list[i]
                max_index = i
        
        if max_index != -1:
            max_list.append(max_number)
            # Recursively call starting from max_index + 1
            find_max_recursive(max_index + 1, max_list)

        

    find_max_recursive(0, max_list) # 
    # print(f"Current max_list: {max_list}")


    return max_list

  




if __name__ == "__main__":
    # Read the txt file which has digits separated by newlines
    
    with open("input_day3.txt", "r") as file:
        digits = file.readlines()
        digits = [line.strip() for line in digits]

    # Create an empty list to hold the results
    results = []
    for digit in digits:
        #Tokenize the digit into individual numbers
        numbers = [int(d) for d in digit]
        # print(f"Digit: {digit}, Numbers: {numbers}")

        # Call the recursive_number_extractor with window size of 2
        result = recursive_number_extractor(numbers, 2)

        # Detokenize the result into a single number
        result = ''.join([str(num) for num in result])
        # print("Resulting maximum numbers with window size 2: ", int(result))
        results.append(int(result))

    print(f"Final numbers list: {results}")
    # Sum all the resulting numbers
    total_sum = sum(results)
    print(f"Total sum of all resulting numbers: {total_sum}")