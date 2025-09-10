print("*******Monthly Expenses and Savings Tracker*******")

def salary():
    income = float(input("Enter your monthly salary: Rs"))
    return income

def expense():
    expense_categories = ['Rent', 'Tution Fees', 'Transport', 'Trip', 'Others']
    expenses = {}
    total = 0
    print("\nEnter your monthly expenses: ")
    for category in expense_categories:
        amount = float(input(f"{category}: Rs"))
        expenses[category] = amount
        total += amount
    return expenses, total

def give_advice(income, total_expense):
    savings = income - total_expense
    print(f"\nYour total expenses is : Rs{total_expense}")
    print(f"Your savings in this month is : Rs{savings}")

    if savings > 0.5 * income:
        print("Your's savings are excellent. Keep doing!!")
    elif savings > 0.2 * income:
        print("Your's savings is good but need to save more.")
    elif savings >= 0:
        print("Your's savings are nil. Reduce your expenses.")
    else:
        print("You are spending more than your salary.")
    return savings

def save_to_file(income, expenses, total_expense, savings):
    with open("monthly_summary.txt", "w") as file:
        file.write("Monthly Income and Expense Summary\n")
        file.write("-" * 40 + "\n")
        file.write(f"Income: Rs{income}\n")
        file.write("Expenses:\n")
        for category, amount in expenses.items():
            file.write(f"  {category}: Rs{amount}\n")
        file.write(f"Total Expenses: Rs{total_expense}\n")
        file.write(f"Savings: Rs{savings}\n")

    print("\nSummary saved to 'monthly_summary.txt'.")

income = salary()
expenses, total_expense = expense()
savings = give_advice(income, total_expense)
save_to_file(income, expenses, total_expense, savings)

