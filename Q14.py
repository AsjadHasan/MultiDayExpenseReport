def generate_expense_report():
    daily_expenses = {}
    all_categories = set()

    number_of_days = int(input("How many days to log? "))

    for i in range(number_of_days):
        date = input("Enter date: ")
        total = 0

        while True:
            entry = input("Enter category and amount (or 'done'): ")

            if entry.lower() == "done":
                break

            category, amount = entry.split(",")
            category = category.strip()
            amount = float(amount.strip())

            total += amount
            all_categories.add(category)

        daily_expenses[date] = total

    print("\nDaily Expense Report:")

    for date, total in daily_expenses.items():
        print(f"{date}: {total:.2f}")

    print("Unique categories:", all_categories)


generate_expense_report()