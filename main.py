# Expense Tracker Main

from tracker import add_expense, view_expenses


def menu():
    print("\n===== EXPENSE TRACKER 💰 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Exit")


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

            msg = add_expense(category, amount)
            print(msg)

        elif choice == '2':
            print(view_expenses())

        elif choice == '3':
            print("Feature coming soon...")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
