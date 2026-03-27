# Import
import json
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

#Funtion to save bank data
def save_bank_data(bank):
    all_accounts_data = {}

    with open("bank.json", "w") as file:
        # Add each account data to the list of all accounts of the bank
        for account in bank.accounts.values():
            account_data = {
                "username": account.username,
                "password": account.password,
                "fullname": account.fullname,
                "balance": account.balance,
                "account_number": account.account_number
            }

            # Add the above data to the account list
            all_accounts_data[str(account.account_number)] = account_data

        # Save all the account data to the file
        json.dump(all_accounts_data, file, indent=4)     

# Funtion to load the bank data
def load_bank_data():
    # Instantiate a new bank data
    #Reset the value in case of adding more funds to the bank
    Bank.total_bank_funds = 0.0
    my_bank = Bank()

    try:
        with open("bank.json", "r") as file:
            data_list = json.load(file)

            # Extract the data from the file to each account, then add to the bank data
            for data in data_list.values():
                new_account = BankAccount(data["username"], data["password"], data["fullname"], data["balance"], data["account_number"])

                # Add the current account data to the list
                my_bank.add_account(new_account)

            return my_bank

    except FileNotFoundError:     
        print("\nThere is no data in the bank!")
        
        return my_bank
    
def main():
    my_bank = load_bank_data()

    is_Running = True

    while is_Running:
        print("\nWelcome to the banking system application. Please enter a number to proceed.")
        print("1. Create an account\n2. Login\n3. Admin: View Total Bank Funds\n4. Exit")

        choice = input("Your choice: ")

        # Creating a new account
        if choice == "1":
            print("\nYou are creating a new account!")
            user_registration(my_bank)

        elif choice == "2":
            #Check if the credential is correct
            current_account = user_authentication(my_bank)

            if current_account is not None:
                user_menu(current_account)
            else:
                print("You have attemped to many failed logins ! You will be returned to the main menu !")
        elif choice == "3":
            print(f"\nThe total funds of the bank is: {Bank.get_total_funds():.2f}$")
        elif choice == "4":
            is_Running = False
            # Save all data
            save_bank_data(my_bank)

            print("Thank you for using our program! Please have a nice day!")
        else:
            print("Invalid input, please enter a number from 1-4 !")

# Funtion to create a bank account
def user_registration(bank):
    while True:
        # Validate input name
        username = input("Please enter a valid username: ")
        username_exist = False

        # Check for empty input
        if username.strip() == "":
            print("\nPlease enter a username, dont leave a blank space")
            continue

        # Check for duplication
        for account in bank.accounts.values():
            if username == account.username:
                print("\n This username is already exist, please try another username !")
                username_exist = True
                break
        if username_exist:
            continue
        else:
            # Finish the loop for username
            break

    while True:
        # Validate input password
        has_letter = False
        has_number = False
        has_special = False
        has_upper = False

        password = input("Please enter your password: ")

        # Check for empty input
        if password.strip() == "":
            print("\nPlease enter a password, dont leave a blank space")
            continue

        # Check for password length
        if len(password) < 8:
            print("\nPassword length must be greater than or equal to 8 characters !")
            continue
        elif len(password) > 24:
            print("\nPassword length must be smaller than or equal to 24 characters !")
            continue

        #Check for first letter being an uppcase character
        if password[0].isupper():
            has_upper = True
        else:
            print("\nThe first character must be an uppercase letter !")
            continue

        # Check for letter, number and special character in the password
        for char in password:
            if char.isalpha():
                has_letter = True
            if char.isdigit():
                has_number = True
            if not char.isalnum():
                has_special = True

        # If there are conditions that are not met, reprompt the user for input  
        if not has_letter:
            print("\nPassword must contain at least one letter !")
            continue
        if not has_number:
            print("\nPassword must have at least one number !")
            continue
        if not has_special:
            print("\nPassword must have at least one special character !")
            continue

        # Pass all conditions, break the password validation loop
        break

    has_valid_name = False

    while True:
        is_name_valid = True

        fullname = input("Please enter your full name: ")

        # Check for empty input
        if fullname.strip() == "":
            print("\nPlease enter a name, dont leave a blank space")
            continue

        for char in fullname:
            if not (char.isalpha() or char == " "):
                is_name_valid = False
                break

        if not is_name_valid:
            print("\nYour name must not contain number or special characters !")
            continue

        # Format the name
        fullname = fullname.upper()
        has_valid_name = True

        # Met the name conditions
        break
    
    # Pass all the validation steps
    if has_letter and has_number and has_special and has_upper and has_valid_name:
        # Create a new BankAccount object
        bank_account = BankAccount(username, password, fullname)

        #Add to the bank data
        bank.add_account(bank_account)

        print(f"\nAccount created successfully! Your account number is {bank_account.account_number}")

# Funtion to validate user credentials
def user_authentication(bank):
    # Prevent the user from entering too much invalid credentials
    username_attempts = 0
    current_account = None

    while username_attempts < 3:
        input_username = input("Please enter your username: ")

        # Check for empty input
        if input_username.strip() == "":
            print("\nPlease enter a username, dont leave a blank space !")
            continue

        # use bank method to find account
        current_account = bank.get_account_by_username(input_username)

        if current_account is not None:
            password_attempts = 0

            while password_attempts < 3:
                input_password = input("Enter your password: ")

                # Check for empty input
                if input_password.strip() == "":
                    print("\nPlease enter your password, dont leave a blank space !")
                    continue

                # use class method to check password
                is_valid = current_account.validate_password(input_password)

                if is_valid:
                    print("\nLogin successful!")
                    return current_account
                else:
                    print("\nWrong password. Try again.")
                    password_attempts += 1

            print("\nToo many failed password attempts.")
            return None
        else:
            print("\nInvalid username. Try again.")
            username_attempts += 1
        
    return None

def user_menu(account):
    while(True):
        print("\nWelcome to the banking system application. Please enter a number to proceed.")
        print("1. Show balance\n2. Withdraw\n3. Deposit\n4. Log out")

        choice = input("Your choice: ")

        # Main loop for the program
        # Show balance
        if(choice == "1"):
            account.showBalance()
        # Withdraw 
        elif(choice == "2"):
            try:
                amount = float(input("Please enter the amount that you want to withdrawn: "))
                account.withdraw(amount)
            except ValueError:
                print("\nPlease only enter a valid amount (No alphabet or special characters)")
        # Deposit
        elif(choice == "3"):
            try:
                amount = float(input("Please enter the amount that you want to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("\nPlease only enter a valid amount (No alphabet or special characters)") 
        # Exit
        elif choice == "4":
            print("\nThanks for using our program. You are now log out! Have a good day !")
            #Break the loop
            break
        # Invalid input
        else:
            print("\nInvalid choice. Please pick a number from 1-4.")  

# Main program
if __name__ == "__main__":
    main()

