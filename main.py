import sqlite3
from analytics import category_expense_graph, income_vs_expense_graph, expense_pie_chart


def add_transaction(t_type, category, amount, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
        (t_type, category, amount, date)
    )

    conn.commit()
    conn.close()
    print("Transaction added successfully!")


def show_summary():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0

    savings = income - expense

    print("\n--- Financial Summary ---")
    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Savings:", savings)

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE type='expense'
        GROUP BY category
        ORDER BY SUM(amount) DESC
        LIMIT 1
    """)
    result = cursor.fetchone()

    if result:
        print("Highest Spending Category:", result[0], "=", result[1])

    conn.close()


def menu():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Show Category Expense Graph")
        print("5. Show Income vs Expense Graph")
        print("6. Show Expense Pie Chart")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Enter income category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("income", category, amount, date)

        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction("expense", category, amount, date)

        elif choice == "3":
            show_summary()

        elif choice == "4":
            category_expense_graph()

        elif choice == "5":
            income_vs_expense_graph()

        elif choice == "6":
            expense_pie_chart()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


menu()