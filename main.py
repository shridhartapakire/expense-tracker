# Expense Tracker Main

from tracker import add_expense, view_expenses, total_spending, filter_by_category


def menu():
    print("\n===== EXPENSE TRACKER 💰 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Filter by Category")
    print("5. Exit")


def main():
    print("\nWelcome to Expense Tracker 💰")

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (food, travel, etc.): ")

            try:
                amount = float(input("Enter amount: "))
            except:
                print("❌ Invalid amount")
                continue

            print(add_expense(category, amount))

        elif choice == '2':
            print(view_expenses())

        elif choice == '3':
            print(total_spending())

        elif choice == '4':
            category = input("Enter category to filter: ")
            print(filter_by_category(category))

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
