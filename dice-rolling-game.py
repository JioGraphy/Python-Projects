import random


# roll dice function
def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total


# Main program
def main():
    player_1 = input("Enter player 1's name: ")
    player_2 = input("Enter player 2's name: ")
    roll_1 = roll_dice()
    roll_2 = roll_dice()

    print(player_1, 'rolled', roll_1)
    print(player_2, 'rolled', roll_2)

    if roll_1 > roll_2:
        print(player_1, 'wins! ')
    elif roll_2 > roll_1:
        print(player_2, 'wins! ')
    else:
        print('Tie')


# invoke main function
main()
