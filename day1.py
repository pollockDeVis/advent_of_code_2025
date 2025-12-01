# Example usage
if __name__ == "__main__":


    # Read the input_day1.txt file for instructions and put it in an array. Each element ends with a newline.
    with open("input_day1.txt", "r") as file:
        instructions = file.readlines()
        # print(instructions)

    # Each instruction contains a direction (L, R) and a number of steps. Parse these instructions and convert to either - (for L) or + (for R) followed by the number of steps.
    parsed_instructions = []
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:].strip())
        if direction == 'L':
            parsed_instructions.append(-steps)
        elif direction == 'R':
            parsed_instructions.append(steps)


    current_position = 50 # Starting position in the ring buffer
    

    # a list to keep track of visited positions
    visited_positions = []
    # The ring buffer starts at 50. Use the parsed instructions to move around the ring buffer, updating the current position accordingly. Print the final position in the ring buffer after executing all instructions.    current_position = 50
    for i, move in enumerate(parsed_instructions):

        move = move % 100  # Ensure the move is within the bounds of the ring buffer size

        # Calculate the new index
        new_position = (current_position + move) % 100
        current_position = new_position
        visited_positions.append(new_position)

        print(new_position)

    # Count the number of zeroes in visited_positions
    zero_count = visited_positions.count(0)
    print(f"Number of times position 0 was visited: {zero_count}")




        
