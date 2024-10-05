import time  # Import the time module to use its timing functions
def monitor_water_level(current_level, tank_depth):
    """Monitor the water level in the tank every 10 seconds for 2 minutes."""
    start_time = time.time()  # Record the current time to track monitoring duration
    duration = 120  # Set the total monitoring duration to 120 seconds (2 minutes)
    interval = 10  # Set the interval for checking the water level to 10 seconds

    # Begin a loop that runs for the specified duration
    while time.time() - start_time < duration:
        # Calculate the current water level as a percentage of the tank's total depth
        percentage = (current_level / tank_depth) * 100
        
        # Print the current water level percentage to the console, formatted to 2 decimal places
        print(f"Current water level: {percentage:.2f}%")

        # Check if the water level is below 20%
        if percentage < 20:
            # Print a message indicating that the tank needs to be filled
            print("The tank needs to be filled.")
        # Check if the water level is at or above 100%
        elif percentage >= 100:
            # Print a message indicating that the tank is full and to switch off the pump
            print("The tank is full, please switch off the water pump.")
            break  # Exit the loop early if the tank is full
        # Simulate waiting for the next reading
        time.sleep(interval)  # Pause execution for the specified interval (10 seconds)
        # Simulate an increase in the water level for demonstration purposes
        # In a real application, this would come from a water level sensor reading
        current_level += 10  # Increase the current water level by 5 units (liters)
# Example usage of the function
if __name__ == "__main__":  # Check if the script is being run directly
    tank_depth = 100  # Define the tank depth (maximum capacity) in liters (or other units)
    initial_water_level = 10  # Define the initial water level in liters (or other units)    
    # Call the function to start monitoring the water level with the initial values
    monitor_water_level(initial_water_level, tank_depth)