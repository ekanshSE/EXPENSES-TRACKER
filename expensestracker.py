class ExpenseTracker:
    def __init__(self):
        # Initialize storage for expenses
        self.expenses = []

    def add_expense(self, amount, category, description):
        # Add an expense to the list
        expense = {'amount': amount, 'category': category, 'description': description}
        self.expenses.append(expense)

    def view_expenses(self, category=None):
        # View expenses, optionally filtered by category
        if category:
            return [expense for expense in self.expenses if expense['category'] == category]
        return self.expenses

    def summarize_expenses(self):
        # Summarize expenses by category
        summary = {}
        for expense in self.expenses:
            if expense['category'] in summary:
                summary[expense['category']] += expense['amount']
            else:
                summary[expense['category']] = expense['amount']
        return summary

def main():
    tracker = ExpenseTracker()
    
    while True:
        # User interface for the Expense Tracker
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            # Add an expense
            amount = float(input("Amount: "))
            category = input("Category: ")
            description = input("Description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added successfully.")
        
        elif choice == '2':
            # View expenses
            category = input("Enter category to filter or leave blank to view all: ")
            expenses = tracker.view_expenses(category)
            print("\nExpenses:")
            for expense in expenses:
                print(f"{expense['amount']} - {expense['category']} - {expense['description']}")
        
        elif choice == '3':
            # Summarize expenses
            summary = tracker.summarize_expenses()
            print("\nExpense Summary:")
            for category, amount in summary.items():
                print(f"{category}: {amount}")
        
        elif choice == '4':
            # Exit the application
            print("Exiting Expense Tracker.")
            break

        else:
            # Handle invalid options
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
