import json
import os
from datetime import datetime

FILE_NAME = 'expenses.json'
#================class 1. Expenses========================
class Expenses:
    def __init__(self, date, category, description, amount):
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.category = category
        self.description = description
        self.amount = amount
        
    def to_dict(self):
        """convert the data to the dictionary for json"""
        return{
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }
    
    def __str__(self):
        return f'{self.date} | {self.category} | {self.description} | {self.amount}'
    
    
#==================cllass 2.expensestracker======================
        
class ExpensesTracker:
    def __init__(self, FILE_NAME):
        self.FILE_NAME = FILE_NAME
        self.expenses = []
        self.load_expenses() 
    """Load all the expenses"""    
    def load_expenses(self):
        """convert eh data in object in order to load the data"""
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, 'r') as file:
                    data = json.load(file)
                    
                    for expense in data:
                        expense_obj = Expenses(
                            expense['date'],
                            expense['category'],
                            expense['description'],
                            expense['amount']
                        )
                        self.expenses.append(expense_obj)
            
            except json.JSONDecodeError:
                print('Error: JSON file is corrupted.')
                
    ######save expenses#########            
    def save_expenses(self):
        """save the data in the json format"""
        data = [expense.to_dict() for expense in self.expenses]
        with open(self.FILE_NAME, 'w') as file:
            json.dump(data, file, indent = 4)
            
     ######Add expenses#########       
    def add_expense(self, date , category, description, amount):
        expense = Expenses(date, category, description, amount)
        self.expenses.append(expense)
        
        self.save_expenses()
    
    ########Search Expenses##############    
    def search_expenses(self, date):
        matching_expenses = []
        for expense in self.expenses:
            if expense.date == date:
                matching_expenses.append(expense)
        return matching_expenses
    
    ##########Update Expenses##############    
    def update_expenses(self,date, category, description, amount ):
        
        expense_found = self.search_expenses(date)
        if not expense_found:
            print("No expnenses found!!")
            return 
        
        #############dispplay availabe expenses##############
        for i, expense in enumerate(expense_found, start = 1):
            print(f"{i}. {expense}")
        try:
            choice = int(input("Choose to edit:: "))
            if not (1 <= choice <= len(expense_found)):
                print("Invalid Choice!!")
                return
            selected = expense_found[choice -1]
            
            if category is None:
                new_category = input(f"New category: (current:({selected.category}))") or selected.category
            else:
                new_category = category
            
            if description is None:
                new_description = input(f"New discription: (current:({selected.description}))") or selected.description
            else: 
                new_description = description
                
            if amount is None:
                while True:
                    try:
                        amount_input = (input(f'New amount: (current:({selected.amount}))'))
                        if amount_input == "":
                            new_amount = selected.amount
                            break
                        new_amount =float(amount_input)
                        if amount_input < 0:
                            print('Amount cant be Negative: Try Again')
                            continue
                        break
                    except ValueError:
                        print('Please enter a valid number')
            else:
                new_amount = amount
                        
            #Apply Updates
            selected.category = new_category
            selected.description = new_description
            selected.amount = new_amount
            
            self.save_expenses()
            print('Expenses updated successfully')
        except ValueError:
            print('Please enter valid number for the choice:: ')
     
    
    ######## Delete the expenses##########
    def delete_expenses(self, date):
        
        expense_found = self.search_expenses(date)
        
        if not expense_found:
            print('No data found::')
            return 
        
        for i, expense in enumerate(expense_found, start = 1):
            print(f'{i}. {expense}')
            
        while True:
            try:
                choice = int(input('Enter the number to delete Expenses:: '))
                if not (1<= choice <= len(expense_found)):
                    print('Invalid number::')
                    continue
                    
                selected = expense_found[choice -1]
                self.expenses.remove(selected)
                self.save_expenses()
                print("Expenses removed sucessfully::")
                break
                 
                    
            except ValueError:
                print("Please enter number::")
                
expenses_data = ExpensesTracker(FILE_NAME)
def main():
    print('=' * 20 + 'Expenses Tracker' + '=' *20)
    
    while True:
        print("Menu")
        print('1. View all expenses:: ')
        print('2. Add Expenses:: ')
        print('3. Search Expenses:: ')
        print('4. Update Expenses:: ')
        print('5. Delete Expenses:: ')
        print('6. Exit')
        
        choice = input('Enter the task number:: ')
        
        if choice == '1':
            print('=' * 30)
            if not expenses_data.expenses:
                print("File is empty!!")
                return
            for i , expense in enumerate(expenses_data.expenses, start = 1):
                print(f"{i}. {expense.date}|{expense.category}|{expense.description}|{expense.amount}")
            
        if choice == "2":
            print("=" * 30)
            while True:
                date = input("Enter date(yy-mm-dd) or press enter for todays date:: ")
                if date == "":
                    date = None
                    break
                else:
                        
        
                
            
        break
    
        
        

main()
                
               
        
        
        
        
        
        
        
            
                