import time


def function_1(list):
    """Function that checks if element is in the list."""
    element = int(input('For what  are you looking for in this list? Which number?'))
    if element in list:
        return True
    else:
        return False

def function_2(set):
    """Function that checks if element is in the set."""
    element = int(input('For what  are you looking for in this list? Which number?'))
    if element in set:
        return True
    else:
        return False

def function_3():
    """Function that creates list or a set."""
    question = input('What do you want to create : list or a set?')
    if question == 'l':
        list_from_1_to_100 = [i for i in range(1,100)]
        print(function_1(list_from_1_to_100))
        return list_from_1_to_100
    elif question == 's':
        set_from_1_to_100  = {i for i in range(1,100)}
        print(function_2(set_from_1_to_100))
        return set_from_1_to_100
    else:
        print('Something went wrong ! Maybe you typed incorrect answer!')

def function_4(func,how_many_times=0):
    """Function that measures performance of the script."""
    sum = 0
    for i in range(0,how_many_times):
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

print(function_4(function_3(),4))
