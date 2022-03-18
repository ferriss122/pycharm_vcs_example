import time

list_from_1_to_100 = [i for i in range(1,100)]
set_from_1_to_100 = (i for i in range(1,100))


def function_that_measures_performance_of_the_script(func,arg,how_many_times=1):
    sum = 0
    for n in range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum


def is_number_in_the_list(number):
    if number in list_from_1_to_100:
        return True
    else:
        return False

def is_number_in_the_set(number):
    if number in set_from_1_to_100:
        return True
    else:
        return False

print(function_that_measures_performance_of_the_script(is_number_in_the_list,20,how_many_times=5))
print(function_that_measures_performance_of_the_script(is_number_in_the_set,120,how_many_times=10))






