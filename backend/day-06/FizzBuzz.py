"""
Solving the very well-known  FizzBuzz.
Application of Looping
"""

def FizzBuzz(num):
    """
    Prints numbers from 0 to num-1, replacing multiples of 3 with "Fizz",
    multiples of 5 with "Buzz", and multiples of both 3 and 5 with "FizzBuzz".

    Args:
        num (int): The limit of numbers to be printed.

    Returns:
        int: The sum of all the numbers printed.
    """
    print("Limit:", num - 1)
    element_list = []
    both_divisible = []
    div_by_three = []
    div_by_five = []
    for i in range(21):
        if (i % 3 == 0 and i % 5 == 0):
            element_list.append(i)
            both_divisible.append(i)
            print("FizzBuzz!")
            continue
        elif (i % 5 == 0):
            element_list.append(i)
            div_by_five.append(i)
            print("Buzz")
            continue
        elif (i % 3 == 0):
            element_list.append(i)
            div_by_three.append(i)
            print("Fizz")
            continue
        print(i)
    print(sum(both_divisible), sum(div_by_five), sum(div_by_three))
    return sum(element_list)

print(FizzBuzz(21))
