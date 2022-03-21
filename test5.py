import random

def symulation_of_lotto(amount=6,total_amount=49):
    """A function that draws six times numbers from 1 to 49 with no duplicates."""
    list_for_numbers = []
    while len(list_for_numbers)<amount:
        random_number = random.randint(1,total_amount)
        if random_number in list_for_numbers:
            pass
        else:
            list_for_numbers.append(random_number)
            continue
    for element in list_for_numbers:
        print(element)

symulation_of_lotto()
