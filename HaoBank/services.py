from models import BankAccount

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
        
        # Check for number and special characters
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
        # Generate an account number
        account_number = bank.generate_account_number()
        bank_account = BankAccount(username, password, fullname, account_number=account_number)

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

def transfer_validation(bank, sender_account):
    acc_num_attempts = 0
    amount_attempts = 0

    while acc_num_attempts < 3:
        receiver_acc_num = input("Please enter the receiver account number: ")

        # Check if the receiver account number is not empty
        if receiver_acc_num.strip() == "":
            print("Please enter the receiver account number, dont leave a blank space !")
            continue

        # Check if the user enter any alphabet or special character
        if not receiver_acc_num.isdigit():
            print("The receiver account number must not contains any alphabet or special characters !")
            acc_num_attempts += 1
            continue

        # Initialize the receiver account
        receiver_account = bank.get_account(int(receiver_acc_num))

        # Check if the receiver account number is a valid number
        if receiver_account is None:
            print("The receiver account was not found ! Please enter a valid account number !")
            acc_num_attempts += 1
            continue

        # Check if the user transfer the money to them selve
        if receiver_account.account_number == sender_account.account_number:
            print("Please enter another account number ! Dont transfer money to yourself :v ")
            acc_num_attempts += 1
            continue
        
        while amount_attempts < 3:
            # Ask for amount to be tranfered
            amount = input("Please input the amount you want to transfer: ")

            # Check if the amount is not empty
            if amount.strip() == "":
                print("Please enter a valid amount, dont leave a blank space !")
                amount_attempts += 1
                continue

            # Check if the user enter any alphabet or special character
            try:
                amount = float(amount)
            except ValueError:
                print("Invalid amount ! The transfer amount must not contains any alphabet or special characters !")
                amount_attempts += 1
                continue


            # Check for negative amount
            if amount <= 0:
                print("The transfer amount must be greater than 0 !")
                amount_attempts += 1
                continue

            # Check if the balance of the sender is enough
            if amount > sender_account.balance:
                print("Insufficient balance! Please enter an amount that is less than or equal to your balance !")
                sender_account.showBalance()
                continue
            
            # Validation complete, begin the transfer process

            transfer_money(sender_account, receiver_account, amount)
            return True
        print("You have enter a wrong amount so many times ! You will be directed back to the previous page !")
        return False
    
    print("You have enter a wrong account number so many times ! You will be directed back to the previous page !")
    return False

def transfer_money(sender, receiver, amount):
    sender.decrease_balance(amount)
    receiver.increase_balance(amount)

    print("Transfered successfully !")