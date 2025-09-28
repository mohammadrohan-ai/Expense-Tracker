💰 Expense Tracker (Python CLI)

A simple command-line Expense Tracker 📝 built in Python to help you record, view, and manage your daily expenses.

✨ Features

➕ Add Expenses: Record expense with Date, Description, Category, and Amount.

➖ Remove Expenses: Delete any previously saved expense.

👀 View Expenses: See all your expenses in a neat list with formatted amounts.

📆 Monthly Summary: View total expenses grouped by month and year.

💾 Auto Save & Load: All expenses are saved in a JSON file so they persist after you exit.

🛠 How It Works

When you first run the program, it automatically creates a file named expenses.txt (if it doesn’t already exist).
This file is used to store all expense records in JSON format.
You don’t need to upload or create this file yourself—the program will handle it.

▶️ How to Run

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git


Navigate into the project folder:

cd <repo-name>


Run the program:

python expense_tracker.py


(Make sure you have Python 3 installed)

📁 Files in the Project
File	Purpose
expense_tracker.py	Main Python script with all program logic
expenses.txt	Automatically created JSON file to store expenses (not uploaded by default)
📜 License

This project is licensed under the MIT License – you can freely use, modify, and distribute it, but there is no warranty.
