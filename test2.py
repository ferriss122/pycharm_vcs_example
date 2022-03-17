def function_checking_if_element_is_in_the_list(list):
    element = int(input('What do you want to look for in a list? Which number?'))
    if element in list:
        return True
    else:
        return False

def function_checking_if_element_is_in_the_set(set):
    element = int(input('What do you want to look for in a set? Which number?'))
    if element in set:
        return True
    else:
        return False

def function_that_creates_list_or_set():
    list_or_generator = input('What do you want to create list or a set?')
    if list_or_generator == "l":
        list_from_1_to_100 = [i for i in range(1, 100)]
        print(function_checking_if_element_is_in_the_list(list_from_1_to_100))
        return list_from_1_to_100

    else:
        set_from_1_to_100 = {i for i in range(1, 100)}
        print(function_checking_if_element_is_in_the_set(set_from_1_to_100))
        return set_from_1_to_100

function_that_creates_list_or_set()


