"""Contains defination of CliUserInterface class."""

import sys
from application.expense_tracker import ExpenseTracker


class CliUserInterface:
    """Implements the CliUserInterfave class."""
    
    def __init__(self):
        self._expense_tracker = ExpenseTracker()
    
    def print_menu(self):
        print(f'\t{"Expense Tracker Application"}\n')
        print(f'\t{"1. Create Expense File"}')
        print(f'\t{"2. Select Expense File"}')
        print(f'\t{"3. Export Expense File to CSV"}')
        print(f'\t{"4. Edit Expense Categories"}')
        print(f'\t{"5. Add Expenses"}')
        print(f'\t{"6. View Expenses"}')
        print(f'\t{"7. Filter Expenses"}')
        print(f'\t{"8. Exit"}\n')
        
    
    def process_menu_choice(self):
        menu_choice = input("Select Menu item: ")
        
        match(menu_choice):
            case "1":
                self.create_expense_file()
            
            case "2":
                self.select_expense_file()
            
            case "5":
                self.add_expenses()
            
            case "6":
                self.view_expenses()
        
            case "7":
                self.filter_expenses()
                
            case "8":
                sys.exit(0)
            case _:
                self.invalid_menu_choice()
    

    
    def create_expense_file(self)->None:
        filename = input("Enter filename to create: ")
        self._expense_tracker.create_expense_file(filename=filename)
    
    def invalid_menu_choice(self):
        print(f'{"Invalid menu choice..."}')
    
    
    def add_expenses(self):
        expense = {}
        while (True):
            try:
                expense["date"] = input("Expense Date: ")
                expense["category"] = input("Category: ")
                expense["amount"] = float(input("Amount: "))
                self._expense_tracker.save_expense(expense)
                keep_going = input("Add anothe? Y/N: ")
                if(keep_going.upper() == "N"):
                    break
            except Exception as e:
                print(f"Problem entering expense: {e}")
                
    def select_expense_file(self):
        print(f"CliUserInterfave::select_expense_file() stub method called...")
        # Show a list of expose files in the directory to choose from
        
        #Let user choose a file
        
        #Get filename of file
        
        #Call expense_tracker.select_expense_file()
        
    
    def start(self):
        while True:
            self.print_menu()
            self.process_menu_choice()
    
    def view_expenses(self):
        expenses = self._expense_tracker.get_expenses()
   
        if not expenses:
            print("No expenses found.")
            return
        
        for expense in expenses:
            print(expense)
    
    def filter_expenses(self):
        expenses = self._expense_tracker.get_expenses()
        
        start_date = input("Start Date: (YYYY-MM-DD): ")
        end_date = input("End Date (YYYY-MM-DD): ")
        category = input("Category: ")
        
        for expense in expenses:
            if start_date and expense["date"] < start_date:
                continue
            if end_date and expense["date"] > end_date:
                continue
            if category and expense["category"].lower() != category.lower():
                continue
            
            print(expense)
        