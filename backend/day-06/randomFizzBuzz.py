"""
Implement a random numbers in python with the limit of random quantity.

"""

import random
random_number = random.randint(21, 50)
print(random_number)

def random_init(max_num_elem):
    random_nums = []
    for i in range(1, max_num_elem):
        random_nums.append(i)

    # Shuffling
    random.shuffle(random_nums)
    return random_nums

print(random_init(random_number))


def FizzBuzz(max_num_elem):
    element_list = []
    both_divisible= []
    div_by_three = []
    div_by_five = []
    for i in range(0, len(random_init(max_num_elem))):
        print(random_init(max_num_elem)[i])
        # Implement
        if(i % 3 == 0 and i % 5 == 0):
            element_list.append(i)
            both_divisible.append(i)
            print("FizzBuzz!")
            continue
        elif (i % 5 ==0):
            element_list.append(i)
            div_by_five.append(i)
            print("Buzz")
            continue
        elif (i % 3 ==0):
            element_list.append(i)
            div_by_three.append(i)
            print("Fizz")
            continue
    print(sum(both_divisible), sum(div_by_five), sum(div_by_three))
    return element_list
print(FizzBuzz(random_number))