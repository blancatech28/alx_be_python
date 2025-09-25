FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid Temperature. Please enter a numerical value")

temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius(fahrenheit):
    if temp_unit == "F":
        temp_celsius = round((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR, 1)
        print(f"{fahrenheit}°F is {temp_celsius}°C")
        return temp_celsius

def convert_to_fahrenheit(celsius):
    if temp_unit == "C":
        temp_fahrenheit = round(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32, 1)
        print(f"{celsius}°C is {temp_fahrenheit}°F")
        return temp_fahrenheit



if temp_unit == "F":
    convert_to_celsius(temp)
elif temp_unit == "C":
    convert_to_fahrenheit(temp)
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
