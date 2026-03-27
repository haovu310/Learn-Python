import random

# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Bank account class
class BankAccount(User):
    def __init__(self, username, password, fullname, balance=0.0, account_number = None):
        super().__init__(username, password)
        self.fullname = fullname
        self._balance = balance

        if account_number is None:
            self.account_number = random.randint(1000, 9999)
        else:
            self.account_number = account_number

    def __str__(self):
        return f"Account Holder: {self.fullname} | Balance: ${self.balance:.2f}"

    # Get the current balance of the account
    def showBalance(self):
        print(f"Card holder: {self.fullname}. Your current balance is: ${self.balance:.2f}")

    # Deposit money to the account
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
            Bank.total_bank_funds += amount

            print(f"You have successfully deposited {amount:.2f}$ to your account !")
            self.showBalance()
        else:
            print("Invalid input, please enter an amount that is larger than 0")

    # Withdraw money from the account
    def withdraw(self, amount):
        if (amount > 0 and amount <= self.balance ):
            self.balance -= amount
            Bank.total_bank_funds -= amount

            print(f"You have successfully withdrawn {amount}$ from your account")
            self.showBalance()
        elif (amount > self.balance):
            print("Please enter an amount that is less than or equal to your current balance !")
            self.showBalance()
        else:
            print("Invalid input, please enter an amount that is larger than 0")

    def validate_password(self, password):
        if self.password == password:
            return True
        return False   

    def validate_username(self, username):
        if self.username == username:
            return True
        return False   
    
    # Getter for the balance
    @property
    def balance(self):
        return self._balance
    
    # Setter for the balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Balance must not be negative")

# Bank class
class Bank:
    total_bank_funds = 0.0

    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        # Add the new account to the dictionary of the bank, the key is the account number
        self.accounts[account.account_number] = account

        # Update the total fund of the bank
        Bank.total_bank_funds += account.balance

    def get_account(self, account_number):
        return self.accounts.get(account_number)
    
    def get_account_by_username(self, username):
        for account in self.accounts.values():
            if account.username == username:
                return account
        return None
         
    
    @classmethod
    def get_total_funds(cls):
        return cls.total_bank_funds