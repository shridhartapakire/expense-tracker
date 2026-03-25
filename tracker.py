# Expense Tracker Logic

import json
from pathlib import Path

DATA_FILE = "data.json"


def load_data():
    if Path(DATA_FILE).exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_expense(category, amount):
    data = load_data()

    expense = {
        "category": category,
        "amount": amount
    }

    data.append(expense)
    save_data(data)

    return "✅ Expense added successfully"


def view_expenses():
    data = load_data()

    if not data:
        return "No expenses found"

    result = "\n📋 All Expenses:\n"
    for i, exp in enumerate(data, start=1):
        result += f"{i}. {exp['category']} - ₹{exp['amount']}\n"

    return result
    

def total_spending():
    data = load_data()

    if not data:
        return "No expenses found"

    total = sum(exp["amount"] for exp in data)
    return f"💰 Total Spending: ₹{total}"


def filter_by_category(category):
    data = load_data()

    filtered = [
        exp for exp in data
        if exp["category"].lower() == category.lower()
    ]

    if not filtered:
        return "No expenses found for this category"

    result = f"\n📂 Expenses for '{category}':\n"
    for i, exp in enumerate(filtered, start=1):
        result += f"{i}. ₹{exp['amount']}\n"

    return result
