import random

steps = 5

chest = ['green','orange','purple','legendary']
nothing_or_chest = ['nothing','chest']
percent_radio_for_chest = random.choices(chest,[75,20,4,1],k=1)
percent_radio_for_nothing_or_chest = random.choices(nothing_or_chest,[40,60],k=1)
print(percent_radio_for_chest)