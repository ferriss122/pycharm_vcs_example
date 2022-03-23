import random,time

steps = 5

chest = ['green','orange','purple','gold']
nothing_or_chest = ['nothing','chest']
values_of_chests = {'green':1000,'orange':4000,'purple':9000,'gold':16000}
list_for_gold = []
list_for_time = []



Menu_of_your_choices = 0
while Menu_of_your_choices != 1:
    Menu_of_your_choices = int(input("""Enter a number from menu:'
    1.exit
    2.moves_amount
    3.reset
    4.move
    5.sum of your gold
    6.your time
    """))
    if Menu_of_your_choices ==2:
        print('You have now ', steps, 'steps')
    elif Menu_of_your_choices ==3:
        steps = 5
        print('Reset completed!')
    elif Menu_of_your_choices ==4:
        while steps>0:
            start = time.perf_counter()

            print('You have an opportunity to meet nothing or a chest!')
            print('Generating...')
            input("Press anything to go by 1 move...")
            percent_radio_for_nothing_or_chest = random.choices(nothing_or_chest, [40, 60], k=1)
            random_choice = random.choice(percent_radio_for_nothing_or_chest)
            if random_choice == "chest":
                percent_ratio_for_chest = (random.choices(chest,[75,20,4,1],k=1))
                for element in percent_ratio_for_chest:
                    print(element)
                gold = values_of_chests.get(element)
                list_for_gold.append(gold)
                print(gold)
            else:
                print("You meet nothing!")
            steps-=1
            end = time.perf_counter()
            overall_time = end - start
            list_for_time.append(overall_time)
    elif Menu_of_your_choices == 5:
        sum_of_gold = 0
        for gold in list_for_gold:
            sum_of_gold = sum_of_gold + gold
        print(sum_of_gold)
    elif Menu_of_your_choices == 6:
        print('You crossed the tunnel in time showed below:')
        print(overall_time)
        sum_time = 0
        for time_element in list_for_time:
            sum_time = sum_time + time_element
        print('The program overall runned for :')
        print(sum_time)




