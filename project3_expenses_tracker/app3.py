# Function to add an expense to the list
def add_expense(expenses, amount, category):
    # Append a dictionary with amount and category to the expenses list
    expenses.append({'amount': amount, 'category': category})
    

# Function to print all expenses
def print_expenses(expenses):
    # Loop through each expense in the list
    for expense in expenses:
        # Print expense details: amount and category
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

# Function to calculate the total of all expenses
def total_expenses(expenses):
    # Use map to extract 'amount' from each expense, then sum them
    return sum(map(lambda expense: expense['amount'], expenses))
    

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    # Return only expenses that match the given category
    return filter(lambda expense: expense['category'] == category, expenses)
    

# Main function to run the expense tracker
def main():
    expenses = []  # Initialize an empty list to store expenses

    while True:  # Infinite loop until the user chooses to exit
        # Display menu options
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        # Take user input for menu choice
        choice = input('Enter your choice: ')

        if choice == '1':  # Option to add an expense
            amount = float(input('Enter amount: '))   # Ask for amount
            category = input('Enter category: ')      # Ask for category
            add_expense(expenses, amount, category)   # Save expense

        elif choice == '2':  # Option to list all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':  # Option to show total
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':  # Option to filter by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # Get filtered expenses
            expenses_from_category = filter_expenses_by_category(expenses, category)
            # Print only those expenses
            print_expenses(expenses_from_category)

        elif choice == '5':  # Option to exit
            print('Exiting the program.')
            break  # Break out of loop and end pr