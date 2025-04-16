
import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    amount = input("Enter amount: ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    print("✅ Expense added!")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(row)

def filter_by_category():
    category = input("Enter category to filter: ").lower()
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[2].lower() == category:
                print(row)

def show_total_spent():
    total = 0.0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[1])
    print(f"💰 Total spent: ${total:.2f}")

def main():
    initialize_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Show Total Spent")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_by_category()
        elif choice == "4":
            show_total_spent()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
