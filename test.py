import time



def sum_all_of_the_numbers(number):
    sum = 0
    for number in range(1,number+1):
        sum = sum + number

    return sum


def function_that_measures_script_performance(func,arg,how_many_times=2):
    sum = 0
    for i in range(0,how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
    return sum

print(function_that_measures_script_performance(sum_all_of_the_numbers,5000,3))
print(function_that_measures_script_performance(sum_all_of_the_numbers,10000))
print(function_that_measures_script_performance(sum_all_of_the_numbers,2500))
print(function_that_measures_script_performance(sum_all_of_the_numbers,20000))


