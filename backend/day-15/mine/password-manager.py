"""
Author: Willie M. Bonavente
Date Started: 12/05/2023
Date Finished: 12/22/2023
Simple Password Manager

For REQUIREMENT(S): AWSCC-CODEQUEST-BACKEND


Note: I am exploring some the fantastic features of python.
"""

# importing necessary modules and libs.
import getpass # libs for censoring pass
import os
import json
import datetime
import hashlib

class Password:

    def __init__(self, password) :
        self.password = password

    def __sizeof__(self) -> int:
        return super().__sizeof__()  # Return the size of the object in bytes

    def strength_pass_checker(self, password):
        # Check if the password meets the desired criteria
        if len(password) < 8:
            return "Pathetic: Password should be at least 8 characters long."
        elif not any(char.isdigit() for char in password):
            return "Weak: Password should contain at least one digit."
        elif not any(char.isalpha() for char in password):
            return "Weak: Password should contain at least one letter."
        elif not any(char.isalnum() for char in password):
            return "Weak: Password should contain at least one alphanumeric character."
        elif not any(not char.isalnum() for char in password):
            return "Weak: Password should contain at least one special character."
        else:
            return "Strong: Password meets the desired criteria."

    def to_strong_password(self, password):
        """
        Converting when password is weak.
        """
        # Check if the password is weak
        if self.strength_pass_checker(password) == "Weak: Password should be at least 8 characters long.":
            # Add additional characters to meet the desired criteria
            password += "123"
        elif self.strength_pass_checker(password) == "Weak: Password should contain at least one digit.":
            # Add a digit to the password
            password += "1"
        elif self.strength_pass_checker(password) == "Weak: Password should contain at least one letter.":
            # Add a letter to the password
            password += "a"
        elif self.strength_pass_checker(password) == "Weak: Password should contain at least one alphanumeric character.":
            # Add an alphanumeric character to the password
            password += "a1"
        elif self.strength_pass_checker(password) == "Weak: Password should contain at least one special character.":
            # Add a special character to the password
            password += "@"

        return password

    def suggestion(self, password):
        """
        Feedback about the password input
        Insert case by case scenario
        case 1: All letters -> suggest to add numbers or special character
        case 2: All numbers -> suggest to add letters or special character
                __Case sensitivity checker__
        case 3: All lowercase -> suggest to add uppercase
        case 5: All uppercase -> suggest to add lowercase
        """
        if password.isalpha():
            return "Add numbers or special characters to improve the password."
        elif password.isdigit():
            return "Add letters or special characters to improve the password."
        elif password.islower():
            return "Add uppercase letters to improve the password."
        elif password.isupper():
            return "Add lowercase letters to improve the password."
        else:
            return "No suggestion for improvement."

    def hashing(self, password):
        """
        Hashes the given password using SHA-256 algorithm.
        """
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password


def main():

    global running  # for looping until case 6

    menu_option()
    choice = int(input("Enter your choice >> "))

    match choice:
        case 1:
            add_data()
        case 2:
            traverse()
        case 3:
            search()
        case 4:
            delete()
        case 5:
            update()
        case 6:
            exit()

        case _:
            raise ValueError("Please Enter a valid choice.")


def menu_option():
    option = ["1 - Add Username and Password",
              "2 - View",
              "3 - Search",
              "4 - Delete",
              "5 - Update",
              "6 - Exit"]
    for i in option:
        print(f"{" ":>20}{i}")
    print()
# 1st Option


def add_data():
    website = input("Enter website: ")
    email = input("Enter email: ")
    
    # Create an instance of the Password class
    password = getpass.getpass("Enter password: ")

    # Use the methods of the Password class
    password_strength = Password(password).strength_pass_checker(password)
    print(f"Password strength: {password_strength}")

    # Suggestion
    password_suggestion = Password(password).suggestion(password)
    print(f"Suggestion: {password_suggestion}")

    # Hashing
    hashed_password = Password(password).hashing(password)
    print(f"Hashed Password {hashed_password}")
    
    # Storage 
    new_data = {
        website: [{
            'email': email,
            'password': password,
            'hashed password': hashed_password
        }]
    }
    # Writing
    if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
        with open('data.json', 'r') as f:
            data = json.load(f)
    else:
        data = {}

    if website in data:
        data[website].append({'email': email, 'password': password, 'hashed password': hashed_password})
    else:
        data.update(new_data)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    print("Data Successfully added!")
    log_entry = logging("User Created an account.", new_data)
    print(f"User Added New Account: {log_entry}")


def traverse():
    print("Traversing File")
    with open('data.json', 'r') as f:
        data = json.load(f)
        for website, credentials in data.items():
            print(f"\n{"Website": >30}: {website}")
            for credential in credentials:
                print(f"{"Email": >28}: {credential['email']}")
                print(f"{"Password":>31}: {'*' * len(credential['password'])}")
                if 'hashed password' in credential:
                    print(f"{"Hashed Password":>38}: {credential['hashed password']}")
            print()
    
    log_entry = logging("User", "User View Data")
    print(f"User Traverse  at {log_entry}")

def search():
    print("Searching for an element.")
    target = input("Enter the website or account you want to search: ")

    with open('data.json', 'r') as f:
        data = json.load(f)

    found = False
    for website, credentials in data.items():
        if website.lower() == target.lower():
            found = True
            print(f"Website: {website}")
            for credential in credentials:
                print(f"Email: {credential['email']}")
                print(f"Password: {credential['password']}")
            print()

    if not found:
        print("Element not found.")

    log_entry = logging("User Search specific account.", target)
    print(f"Account Searched {target }at {log_entry}.")

def delete():
    print("\n___Deleting Mode___\n")
    target = input("Enter the website or account you want to delete: ")

    with open('data.json', 'r') as f:
        data = json.load(f)

    if target in data:
        del data[target]
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully deleted {target} from data.json.")
    else:
        print(f"{target} does not exist in data.json.")
    
    log_entry = logging("Deleting Account.", target)
    print(f"Deleted Account: {target} at {datetime.datetime.now()}")

# 5th Option


def update():
    print("Function update.")
    target = input(
        "Enter the website or account you want to update (or type 'esc' to cancel): ")

    if target.lower() == 'esc':
        print("Update canceled.")
        return

    with open('data.json', 'r') as f:
        data = json.load(f)

    if target in data:
        print(f"Updating {target}...")
        for credential in data[target]:
            if input("Do you want to update the website? (yes/no): ").lower() == 'yes':
                new_website = input("Enter the new website or account: ")
                if credential['website'] != new_website:
                    credential['website'] = new_website
                    with open('activity_log.txt', 'a') as f:
                        f.write(f"User updated website for {target} at {datetime.datetime.now()}\n")

            if input("Do you want to update the email? (yes/no): ").lower() == 'yes':
                new_email = input("Enter the new email: ")
                if credential['email'] != new_email:
                    credential['email'] = new_email
                    with open('activity_log.txt', 'a') as f:
                        f.write(f"User updated email for {target} at {datetime.datetime.now()}\n")

            if input("Do you want to update the password? (yes/no): ").lower() == 'yes':
                new_password = getpass.getpass("Enter the new password: ")
                if credential['password'] != new_password:
                    credential['password'] = new_password
                    with open('activity_log.txt', 'a') as f:
                        f.write(f"User updated password for {target} at {datetime.datetime.now()}\n")

        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Successfully updated {target}.")
    else:
        print(f"{target} does not exist in data.json.")
    
# Insert the referencing here....Example aaabbb-11223

def reference_acct():
    
    """
    In this we will simulate the random function to generate the reference number for 
    account.
    """
    pass


def logging(activity, account):
        """
        Writes the user activity to a log file.
        """
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}:{account} {activity}\n"

        with open("activity_log.txt", "a") as log_file:
            log_file.write(log_entry)
        return account
    
    
running = True

if __name__ == '__main__':
    while running:
        print(f"\n\n{"=======PASSWORD MANAGER=======":>50}\n")
        main()