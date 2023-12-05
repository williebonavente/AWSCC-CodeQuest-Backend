"""
Author: Willie M. Bonavente
Date: 12/05/2023
Simple Password Manager

For REQUIREMENT(S): AWSCC-CODEQUEST-BACKEND

"""

# importing necessary modules and libs.
import os # Libs for 'cls'
from datetime import datetime, time 
import json
import hashlib

class Password:
    
    def __init__(self, numbers, letters, alpha_num, special_char):
        self.numbers = numbers
        self.letters = letters
        self.alpha_num = alpha_num
        self.special_char = special_char


    def strength_pass_checker(self):
        
        """
        A method to check the strength of the password.
        """
        
        pass

    
    def to_strong_password(self):
        
        """
        Converting when password is weak.
        """
        
    
    def suggestion(self):
        
        """
        Feedback about the password input
        Insert case by case scenario
        case 1: All letters -> suggest to add numbers or special character
        case 2: All numbers -> suggest to add letters or special character
                __Case sensitivity checker__
        case 3: All lowercase -> suggest to add uppercase
        case 5: All uppercase -> suggest to add lowercase
        """
        pass
    
    def hashing(self):
        pass
    
    def dates(self):
        
        """
        Systematic formatting about date, time.
        """
        pass
    
    def logging(self):
        
        """
        We are creating a separate file for the logging when the password was created.
        """
        pass
    
    def censoring(self):
        
        """
        Function to censor the character input whenever the password is being input.
        For example: 
            Enter password: 8888 instead of 8888 in the terminal it will display ****
        """
        pass
    
    def encryption(self):
        
        """
        This is the encryption about the data.json file.
        Partial implementation only we will refer to the manual about this.
        """
        pass
    

def main():

    global running # for looping until case 6
    
    menu_option()
    choice = int(input("Enter your choice: "))
    
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
        print(i)

# 1st Option
def add_data():
    os.system('cls')
    website = input("Enter website: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    
    
    added_data =  {
        website: [{
            'email': email,
            'password': password
        }]
    }
    
    with open('data.json', 'r') as f:
        data = json.load(f)
    print("Adding data")

# 2nd Option
def traverse():
    print("Traversing File")
    pass

# 3rd Option
def search():
    print("Searching an element.")
    pass

# 4th Option
def delete():
    print("Deleting specific data.")
    pass

# 5th Option
def update():
    print("Function update.")
    pass

running = True

if __name__ == '__main__':
    while running:
        print("=======PASSWORD MANAGER=======")
        main()