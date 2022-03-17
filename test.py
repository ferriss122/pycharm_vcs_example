def sum_all_of_the_numbers(number):
    sum = 0
    for number in range(1,number+1):
        sum = sum + number

    return sum

n = int(input('Enter a number:'))
print(sum_all_of_the_numbers(n))