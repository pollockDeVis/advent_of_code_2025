# Class of a ring buffer which taken a size as input and has a pointer to the current position
class RingBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [0] * size
        self.current_position = 0

        
    # Fill values in the ring buffer
    def fill(self, values):
        for i in range(min(len(values), self.size)):
            self.buffer[i] = values[i]

    def move(self, steps):
        # Takes a positive or negative integer and moves the steps accordingly in the ring buffer
        # an array holds all the visited positions
        visited_positions = []
        visited_positions.append(self.current_position)
        if steps < 0:
            for _ in range(-steps):
                self.current_position = (self.current_position - 1) # % self.size
                visited_positions.append(self.current_position)
        elif steps >= 0:
            for _ in range(steps):
                self.current_position = (self.current_position + 1) #% self.size
                visited_positions.append(self.current_position)
        return visited_positions
      





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

        # print(new_position)

    # Count the number of zeroes in visited_positions
    zero_count = visited_positions.count(0)
    print(f"Number of times position 0 was visited: {zero_count}")

    ring_buffer = RingBuffer(100)
    ring_buffer.current_position = 50


    # Fill the ring buffer such that index 0 to 99 contains values 0 to 99
    ring_buffer.fill(list(range(100)))

    visited_positions = []
    for move in parsed_instructions:
        positions = ring_buffer.move(move)
        visited_positions.extend(positions)    

    # Convert visited_positions to values in the buffer
    visited_positions = [ring_buffer.buffer[pos % ring_buffer.size] for pos in visited_positions]

    zero_count_2 = visited_positions.count(0)
    print(f"Number of times position 0 was visited using RingBuffer class: {zero_count_2}")

    number_of_zeros = zero_count_2 - zero_count
    print(f"Number of additional times position 0 was visited using RingBuffer class: {number_of_zeros}")
    print(f"Visited positions using RingBuffer class: {visited_positions}")




        
