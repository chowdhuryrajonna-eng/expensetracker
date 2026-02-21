import sqlite3
import matplotlib.pyplot as plt


def category_expense_graph():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE type='expense'
        GROUP BY category
    """)
    data = cursor.fetchall()

    if not data:
        print("No expense data to show.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Category-wise Expenses")
    plt.show()

    conn.close()


def income_vs_expense_graph():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    expense = cursor.fetchone()[0] or 0

    plt.bar(["Income", "Expense"], [income, expense])
    plt.title("Income vs Expense")
    plt.ylabel("Amount")
    plt.show()

    conn.close()


def expense_pie_chart():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM transactions
        WHERE type='expense'
        GROUP BY category
    """)
    data = cursor.fetchall()

    if not data:
        print("No expense data to show.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()

    conn.close()