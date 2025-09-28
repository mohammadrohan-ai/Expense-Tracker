"""
Expense Tracker Project
-----------------------
A simple command-line application to record, view and summarize
your personal expenses. Data is stored in a local JSON text file.

Features:
1. Add expenses with description, category and amount.
2. Remove any existing expense by its number.
3. View all recorded expenses.
4. View a monthly expense summary.
"""

from datetime import datetime
import json

# ---------------------------
# Global list to hold all expense records in memory
# Each expense is a dictionary with:
#   Date (string dd-mm-yyyy)
#   Description (string)
#   Category (string)
#   Amount (float)
# ---------------------------
expenses = []


# ---------- File Operations ----------
def load_expenses():
    """
    Load expenses from expenses.txt (JSON format) into the global list.
    If the file does not exist or is corrupted, start with an empty list.
    """
    global expenses
    try:
        with open("expenses.txt", "r") as f:
            expenses = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []   # start fresh if file missing or unreadable


def save_expenses():
    """
    Save the current expenses list to expenses.txt in JSON format.
    """
    with open("expenses.txt", "w") as f:
        json.dump(expenses, f, indent=4)


# Load any existing expenses at program start
load_expenses()


# ---------- Helper Functions ----------
def ask_again(prompt):
    """
    Keep asking until the user types 'yes' or 'no'.
    Returns the lowercase answer ('yes' or 'no').
    """
    while True:
        answer = input(prompt).lower().strip()
        if answer in ("yes", "no"):
            return answer
        print("Please respond with 'yes' or 'no'\n")


# ---------- Core Features ----------
def view_expenses():
    """
    Display all recorded expenses in a formatted list.
    """
    print("-" * 40)
    if not expenses:
        print("No Expenses Yet.\n")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. Date : {expense['Date']} | "
                f"Description : {expense['Description']} | "
                f"Category : {expense['Category']} | "
                f"Amount : ${expense['Amount']:.2f}"
            )
    print("-" * 40)


def add_expense():
    """
    Prompt the user to add one or more expenses.
    Performs basic input validation before saving.
    """
    print("-" * 40)
    while True:
        try:
            date_today = datetime.now().strftime("%d-%m-%Y")

            # --- Description ---
            desc = input("Enter short description of your expense: \n").strip().capitalize()
            while not desc:
                desc = input("Description cannot be empty, enter description again: \n")

            # --- Category ---
            category = input("Enter category of your expense (ex: food, travel, groceries): \n").strip().capitalize()
            while not category:
                category = input("Category cannot be empty, enter category again: \n")

            # --- Amount ---
            while True:
                amount = float(input("Enter amount of your expense: \n").strip())
                if amount < 0:
                    print("Amount must be a positive number\n")
                    continue
                else:
                    break

            # --- Save the expense ---
            expense = {
                "Date": date_today,
                "Description": desc,
                "Category": category,
                "Amount": amount,
            }
            expenses.append(expense)
            save_expenses()
            print("Your expense has been added.\n")

            # Ask if user wants to add more
            if ask_again("Do you want to add another expense? (yes/no): \n") != "yes":
                print("Thank you for adding your expense.\n")
                print("Here's your updated expense details:\n")
                view_expenses()
                break

        except ValueError:
            # Handles invalid number input for amount
            print("Please enter a valid input\n")
            continue
    print("-" * 40)


def remove_expense():
    """
    Allow the user to remove an expense by its list number.
    """
    print("-" * 40)
    while True:
        print("Here's your expense details:\n")
        view_expenses()
        print("\n")
        try:
            remove = int(input("Enter number of expense you want to remove: \n").strip())

            # Validate selection
            if remove <= 0 or remove > len(expenses):
                print("Enter a valid number\n")
                continue

            # Remove the chosen expense
            remove -= 1
            expenses.pop(remove)
            save_expenses()
            print("Your expense has been removed.\n")

            if ask_again("Do you want to remove another expense? (yes/no): \n") != "yes":
                print("Thank you for removing your expense.\n")
                print("Here's your updated expense details:\n")
                view_expenses()
                break

        except ValueError:
            # Handles non-integer input for expense number
            print("Please enter a valid input\n")
            continue
    print("-" * 40)


def monthly_summary():
    """
    Show total expenses for each month (format: MM-YYYY).
    """
    print("-" * 40)
    if not expenses:
        print("No Expenses Yet.\n")
        return

    monthly_totals = {}

    # Group amounts by month-year key
    for expense in expenses:
        month = datetime.strptime(expense['Date'], "%d-%m-%Y").strftime("%m-%Y")
        monthly_totals[month] = monthly_totals.get(month, 0) + expense['Amount']

    print("Here's your monthly expense summary:\n")
    for i, (month, total) in enumerate(monthly_totals.items(), start=1):
        print(f"{i}. {month} => ${total:.2f}")
    print("-" * 40)


# ---------- Main Program ----------
def main():
    """
    Display menu and respond to user choices.
    """
    print("-" * 40)
    print("Welcome to Expense Tracker!\n")

    menu = """
    1. Add Expenses
    2. Remove Expenses
    3. View Expenses
    4. View Monthly Summary
    5. Exit
    """

    while True:
        print(menu)
        try:
            option = int(input("Which option do you want to use? (1-5): \n").strip())
            if option == 1:
                add_expense()
            elif option == 2:
                remove_expense()
            elif option == 3:
                view_expenses()
            elif option == 4:
                monthly_summary()
            elif option == 5:
                print("Thanks for using Expense Tracker!\n")
                break
            else:
                print("Please choose between 1 and 5\n")
                continue
        except ValueError:
            print("Please enter a valid integer\n")
            continue
    print("-" * 40)


if __name__ == "__main__":
    main()
