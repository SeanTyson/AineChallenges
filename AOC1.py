def find_floor(instructions):
    # Initialize the starting floor
    floor = 0
    
    # Iterate over each character in the instructions
    for char in instructions:
        if char == '(':
            floor += 1  # Move up one floor
        elif char == ')':
            floor -= 1  # Move down one floor
    
    return floor

# Example usage
instructions = input("Enter the instructions: ")
resulting_floor = find_floor(instructions)
print(f"Santa ends up on floor {resulting_floor}.")
