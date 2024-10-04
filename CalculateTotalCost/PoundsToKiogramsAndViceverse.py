# Convert Pounds to kilograms.
def pounds_to_Kilograms(pounds):
    return pounds * 0.453592
# Convert kilograms to Pounds.
def kilograms_to_pounds(kilograms):
    return kilograms / 0.453592

# Prompt the user to input a weight value and return the value and unit,
def get_weight_input():
    while True:
        try:
            weight = float(input("Enter the weight value: "))
            unit = input("Enter the unit (P for Pounds, K for Kilograms): ").strip().upper()
            if unit not in ['P', 'K']:
                raise ValueError("Invalid unit, Please enter 'P' for Pounds or 'K' for Kilograms.")
            return weight, unit    
        except ValueError as e:
            print(F"Error: {e}. Please try again.")
# Main program loop to handle weight conversions.
def main():
    while True:
        weight, unit = get_weight_input()
        
        if unit == 'P':
            converted = pounds_to_Kilograms(weight)
            print(f"{weight} lbs is equal to {converted:.2f} kg")
        elif unit == 'K':
            converted = kilograms_to_pounds(weight) 
            print(f"{weight} kg is equal to {converted:.2f} lbs")
            
        # Check if the user wants to stop
        continue_choice = input("Do you want to enter Weight? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting the program.")
            break          
if __name__ == "__main__":
    main()         