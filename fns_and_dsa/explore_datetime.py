import datetime 

def display_current_datetime():
    current_date = datetime.datetime.now()
    formated = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formated

def calculate_future_date():
    days_number = int(input("Enter your number of days: "))
    future_date = datetime.date.today() + datetime.timedelta(days=days_number)
    return future_date

# Example usage
print("Current date and time:", display_current_datetime())
print("Future date:", calculate_future_date())


