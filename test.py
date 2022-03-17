import time



def sum_all_of_the_numbers(number):
    sum = 0
    for number in range(1,number+1):
        sum = sum + number

    return sum


def function_that_measures_script_performance(func,arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    sumary = end - start
    return sumary

print(function_that_measures_script_performance(sum_all_of_the_numbers,5000))


