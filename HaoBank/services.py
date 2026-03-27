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