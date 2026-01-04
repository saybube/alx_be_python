FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    
    Parameters:
    fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
    float: Temperature in Celsius
    """
    # Use the global conversion factor to convert F to C
    # Formula: (F - 32) * 5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    float: Temperature in Fahrenheit
    """
    # Use the global conversion factor to convert C to F
    # Formula: C * 9/5 + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    """
    Main function to run the temperature conversion tool.
    """
    try:
        # Prompt user to enter a temperature
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform conversion based on the unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()