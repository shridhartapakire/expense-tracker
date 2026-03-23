# Expense Tracker Main

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

        if choice == '4':
            print("Exiting...")
            break
        else:
            print("Feature coming soon...")


if __name__ == "__main__":
    main()
