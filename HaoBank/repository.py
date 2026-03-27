import json
from pathlib import Path
from models import Bank, BankAccount

# Define the base path for the data file to be read and save
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "bank.json"

#Funtion to save bank data
def save_bank_data(bank):
    all_accounts_data = {}

    with open(DATA_FILE, "w") as file:
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
        with open(DATA_FILE, "r") as file:
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