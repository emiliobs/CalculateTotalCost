# Function to calculate the total cost of items from a list of item names and prices
def calculate_total_cost(my_list):
    # Initialize total_cost to 0, which will hold the sum of all the prices
    total_cost = 0

    # Loop through the list and add only the prices (which are at odd indices)
    # We use 'range(1, len(my_list), 2)' to start at index 1 (first price) and skip every other index.
    # This ensures that only prices (which are at odd indices) are added to total_cost.
    for i in range(1, len(my_list), 2):  # start from index 1 and jump by 2 steps (i.e., 1, 3, 5, ...)
        total_cost += my_list[i]  # Add the price at index 'i' to the total cost

    # Output a message based on the total cost
    # If the total cost is greater than 150, print a warning that the cost is too high
    if total_cost > 150:
        print("The cost is too high.")
    # If the total cost is greater than 50 but less than or equal to 150, print that the price is reasonable
    elif total_cost > 50:
        print("The price is reasonable.")
    # If the total cost is less than or equal to 50, print a warning that the price is too low
    else:
        print("The price is too low, check the costing again.")
    
    # Return the total cost so it can be used outside the function
    return total_cost

# Example usage
# This list contains alternating item names and their prices
my_list = ['Laptop', 1.50, 'Screen', 0, 'Prints', 0, 'Mobile', 0, 'Motor', 200]

# Call the function with 'my_list' and store the returned total cost in the variable 'total'
total = calculate_total_cost(my_list)

# Print the total cost to the console
print(f"Total Cost: {total}")