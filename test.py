import time

set_from_1_to_100 = {i for i in range(1,100)}
list_from_1_to_100 = [i for i in range(1,100)]

def function_1(number):
    """Function that checks if the number is in the list."""
    if number in list_from_1_to_100:
        return True
    else:
        return False

def function_2(number):
    """Function that checks if the number is in the set."""
    if number in set_from_1_to_100:
        return True
    else:
        return False

def function_3(func,arg,how_many_times=1):
    """Function that measures time performance of the program."""
    sum = 0
    for n in range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum

print(function_3(function_2,20,how_many_times=2))
print(function_3(function_1,120,how_many_times=10))


