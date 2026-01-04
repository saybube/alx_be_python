from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Calculate and display a future date based on user input.
    """
    # Prompt the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in YYYY-MM-DD format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    """
    Main function to run the datetime exploration script.
    """
    # Part 1: Display the current date and time
    display_current_datetime()
    
    # Part 2: Calculate and display a future date
    calculate_future_date()

if __name__ == "__main__":
    main()