from repository import load_bank_data, save_bank_data
from services import user_registration, user_authentication
from models import Bank

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