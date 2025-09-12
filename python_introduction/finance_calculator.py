# finance_calculator.py


# ask user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# ask user for total expenses in the month
total_monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating the monthly savings
monthly_savings = monthly_income - total_monthly_expenses
print(f"Your monthly savings are ${int(monthly_savings)}.")

# Projecting the annual savings of the user
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
