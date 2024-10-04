
def celsius_to_fhrenheit(celsius):
 # Convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
 # Convert Fahrenheit To Celsius
    return(fahrenheit - 32) * 5/9


def get_temperature_input():
 # Prompt the user to input a temperature value and return the values and unit.
    while True:
        try:
            temperature = float(input("Enter the Temperature value: "))
            unit = input("Enter the unit. Please enter 'C' for Celsius or 'F' for Fahrenheit: ").strip().upper()
            if unit not in['C','F']:
                raise ValueError("Invalid unit, Please enter 'C' for Celsius or 'F' for Fahrenheit." )
            return temperature, unit
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
def main():
    # Main program loop to handle temperature conversion
    while True:
    
        temperature, unit = get_temperature_input()
    
        if unit == 'C':
            converted = celsius_to_fhrenheit(temperature)
            print(f"{temperature}℃ is equal to {converted:.2f} ℉") 
        elif unit == 'F':
            converted = fahrenheit_to_celsius(temperature)
            print(f"{temperature}℉ is equal to {converted:.2f} ℃")  
    
        # Check id the user wants to stop
        continue_choice = input("Do yoy want to enter another temperature? (yes/no): ").strip().lower()    
        if continue_choice != 'yes':
            print("Exiting the programa! :)")
            break
        
if __name__ == "__main__":
    main()                     