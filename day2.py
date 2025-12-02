
def symmetric_check(digit):
    # Tokenize the digits
    digits = [int(d) for d in str(digit)]
    
    # Compare half of the digits to the other half
    length = len(digits)

    # Check if length is even
    if length % 2 != 0:
        return False
    
    half_length = length // 2

    first_half = digits[:half_length]
    second_half = digits[half_length:]

    # See if the first half matches the second half
    for i in range(half_length):
        if first_half[i] != second_half[i]:
            return False
    return True


def id_range_parser(id_range):
    start, end = map(int, id_range.split('-'))
    return list(range(start, end + 1))



if __name__ == "__main__":


    digit = 23232323


    id_range = "24-78"
    id_list = id_range_parser(id_range)
    print(f"ID List: {id_list}")


    # Read range from input_day2.txt #Example ranges 959516-995437,389276443-389465477,683-1336, ...
    id_ranges = []
    with open("input_day2.txt", "r") as file:
        # ranges are comma separated
        ranges = file.read().strip().split(',')
        for r in ranges:
            id_list = id_range_parser(r)
            id_ranges.extend(id_list)


    symmetric_ids = []
    for id in id_ranges:
        
        if symmetric_check(id):
            print(f"ID {id} has symmetric halves.")
            # Convert the id to an integer and add to the list
            id = int(id)
            
            # Append to symmetric_ids
            symmetric_ids.append(id)
            
            

    print(f"Symmetric IDs: {symmetric_ids}")
    # Sum of symmetric IDs
    sum_symmetric_ids = sum(symmetric_ids)
    print(f"Sum of Symmetric IDs: {sum_symmetric_ids}")
