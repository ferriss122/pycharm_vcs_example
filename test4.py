import random

amount_of_players = 2

AMOUNT_OF_CARDS = 52

hand_of_player_1 = []
hand_of_player_2 = []

cardList = ["2 Club", "3 Club", "4 Club", "5 Club", "6 Club", "7 Club", "8 Club", "9 Club", "10 Club", "Jack Club",
"Queen Club","King Club", "Ace Club", "2 Diamond", "3 Diamond", "4 Diamond", "5 Diamond", "6 Diamond", "7 Diamond",
"8 Diamond", "9 Diamond", "10 Diamond", "Jack Diamond", "Queen Diamond", "King Diamond", "Ace Diamond" , "2 Heart",
"3 Heart", "4 Heart", "5 Heart", "6 Heart", "7 Heart" , "8 Heart", "9 Heart", "10 Heart", "Jack Heart", "Queen Heart",
"King Heart", "Ace Heart", "2 Spade", "3 Spade", "4 Spade", "5 Spade", "6 Spade", "7 Spade", "8 Spade", "9 Spade",
"10 Spade", "Jack Spade", "Queen Spade", "King Spade", "Ace Spade"]

random.shuffle(cardList)
for element in range(len(cardList)):
        if cardList[element] in hand_of_player_1:
            pass
        elif len(hand_of_player_1)== AMOUNT_OF_CARDS // amount_of_players:
            if cardList[element] in hand_of_player_2:
                pass
            else:
                hand_of_player_2.append(cardList[element])
        else:
            hand_of_player_1.append(cardList[element])

print(hand_of_player_1)
print(hand_of_player_2)


