"""
AUTHOR: WILLIE M. BONAVENTE

First Mini Project. AWSSC-CODEQUEST-BACKEND ✨
SHOPPING LIST
"""

"""
4 Options to select with
    1. To add
    2. View
    3. Remove
    4. Quit
    
"Additional Logic, the item must be saved even when the program was terminated.
"""

import os

def main():

    # Display the options available
    # Display first the choices available
    print("Options: ")
    print("1. Add item to the shopping list")
    print("2. View  shopping list")
    print("3. Remove item from  shopping list")
    print("4. Quit")

    choice = int(input("Enter the number of your choice: "))
    process_routine(choice)


def process_routine(choice):
    # Shopping list is empty by default
    shopping_list = []

    if choice == 1:
        adding_item = input("Enter the item you want to add: ")
        shopping_list.append(adding_item)
        try:
            with open("cart.txt", "a") as cart_file:
                cart_file.write(str(adding_item + "\n"))
            print(f"{adding_item} has been added to your shopping list.")
        except PermissionError:
            print("Permission denied. Unable to add item to the shopping list.")
    elif choice == 2:
        print("Your shopping list: ")
        try:
            with open("cart.txt", "r") as cart_file:
                shopping_list = cart_file.read().splitlines()
            for item in shopping_list:
                print(item)
        except FileNotFoundError:
            print("Shopping list file not found.")
    
    # Temporary file to handle the Errno[13] Permission denied
    # It occurs when we try to read and write the file at the same time.
    # This is temporary file comes to save the day.
    
    elif choice == 3:
        removing_item = input("Enter the item you want to remove: ")
        item_found = False

        try:
            with open("cart.txt", "r") as cart_file, open("temp.txt", "w") as temp_file:
                for line in cart_file:
                    item = line.strip()
                # shopping_list = cart_file.read().splitlines()
                    if item == removing_item:
                        item_found = True
                    else:
                        temp_file.write(item + "\n")
            
            if item_found:
                os.remove("cart.txt")
                os.rename("temp.txt", "cart.txt")
                print("Opening file for writing...")
                print(f"{removing_item} has been removed from your shopping list.")
            else:
                os.remove("temp.txt")
                print("Item was not found.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error: {str(e)}")
    elif choice == 4:
        print("Goodbye!")
    else:
        print(f"{choice} is not a valid choice. Please try again.")


if __name__ == '__main__':
    main()
