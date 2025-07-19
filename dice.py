import random


def roll(dice):
    try:
        num_dice, sides = map(int, dice.split("d"))

        result = [random.randint(1, sides) for i in range(num_dice)]

        return result

    except TypeError:
        return "Invalid input. Please use XdY format"


dice_roll = input("Dice roll: ")
result = roll(dice_roll)
print(f"{result}")
