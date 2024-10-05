def monitor_water_level(current_level, tank_depth):
    """Monitor the water level in the tank every 10 seconds for 2 minutes."""
    duration = 120  # 2 minutes in seconds
    interval = 10  # 10 seconds
    steps = duration // interval  # Number of checks (2 minutes / 10 seconds)

    for step in range(steps):
        # Calculate percentage of water level
        percentage = (current_level / tank_depth) * 100
        print(f"Current water level: {percentage:.2f}%")

        # Check conditions
        if percentage < 20:
            print("The tank needs to be filled.")
        elif percentage >= 100:
            print("The tank is full, please switch off the water pump.")
            break
        
        # Simulate waiting for the next reading
        # Instead of sleeping, we simply simulate time passing
        for _ in range(interval):  # Simulating the passage of time
            pass  # This loop does nothing but simulates time
        
        # Simulate changing water level for demonstration purposes
        # In a real scenario, this would come from an actual sensor reading
        current_level += 5  # Simulating an increase in water level

# Example usage
if __name__ == "__main__":
    tank_depth = 100  # Example tank depth in liters (or any other unit)
    initial_water_level = 10  # Starting water level in liters (or any other unit)
    monitor_water_level(initial_water_level, tank_depth)
