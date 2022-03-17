def function_that_checks_if_element_is_in_a_list(list):
    element = int(input('For what  are you looking for in this list? Which number?'))
    if element in list:
        return True
    else:
        return False

def function_that_checks_if_element_is_in_a_set(set):
    element = int(input('For what  are you looking for in this list? Which number?'))
    if element in set:
        return True
    else:
        return False

def function_that_creates_list_or_a_set():
    question = input('What do you want to create : list or a set?')
    if question == 'l':
        list_from_1_to_100 = [i for i in range(1,100)]
        print(function_that_checks_if_element_is_in_a_list(list_from_1_to_100))
        return list_from_1_to_100
    elif question == 's':
        set_from_1_to_100  = {i for i in range(1,100)}
        print(function_that_checks_if_element_is_in_a_set(set_from_1_to_100))
        return set_from_1_to_100
    else:
        print('Something went wrong ! Maybe you typed incorrect answer!')

function_that_creates_list_or_a_set()
