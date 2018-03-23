import os

print(input("Hie welcome to CBZ Bank!"))
os.system('clear')

print(input("Enter your Username"))
os.system('clear')

print(input("Enter your password"))
os.system('clear')

def show_help():
    #Print out instructions on how to use platform.
    print("""
    Enter 'DONE' to end the program.
    Enter 'HELP' to get help.
    Enter 'SHOW' to see your balance and transactions.
    """)
show_help      

class Client(object):
    # A customer of CBZ Bank with a checkingn account.  Customers have the following properties:
    def __init__(self, name='Genius chamisa', balance = 10000.00):
        #Return a customer object whose name is *name* and starting balance is *balance*
        self.name = name
        self.balance = balance  
        
    def withdraw(self, amount):
        #Return the balance remaining after withdrawing *amount* ndollars
        if amount > self.balance:
            raise RuntimeError(amount > self.balance)
            self.balance += amount
            print(self.balance)
    withdraw(self, amount = 1600.00)        
    
    def deposit(self, amount):
        #Return the balance remaining after depositing *amount* dollar.
        self.balance += amount
        print(self.balance)
    deposit(self, amount = 5000.00)    
    
Client(object) 
