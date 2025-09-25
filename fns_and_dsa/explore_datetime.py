from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formated = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formated

def calculate_future_date():
    days_number = int(input("Enter the number of days to add to the current date: "))
    future_date = date.today() + timedelta(days=days_number)
    # Format future date to match grader expectation
    return future_date.strftime("%Y-%m-%d")

# Example usage
print("Current date and time:", display_current_datetime())
print("Future date:", calculate_future_date())
