import time

def function_1(number):
    """Function that sums numbers from 1 to number defined by user."""
    sum = 0
    for number in range(1,number+1):
        sum = sum + number

    return sum

print(function_1(5))
print(function_1(10))

def function_2(func,arg):
    """Function that measures time performance of the script."""
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

print(function_2(function_1,5))
print(function_2(function_1,10))