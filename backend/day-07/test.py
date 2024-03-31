shopping_list = []

with open("cart.txt", "r") as cart_file:
    shopping_list = cart_file.read().splitlines()


    check_element = input("Enter the element you want to check: ")

    for item in shopping_list:
        if item == check_element:
            print("Element was found..")
            break
        else:
            print("Element was not found.")
            break
    # print(check_element in shopping_list)
cart_file.close()
# with open("cart.txt", "a") as cart_file:
#     adding_item = input("Enter the item: ")
#     shopping_list.append(adding_item)
#     cart_file.write(str(adding_item + " \n"))
    