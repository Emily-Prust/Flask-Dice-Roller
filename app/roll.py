from random import randint


def roll(amount, dice_number):
    roll_result = ""
    for i in range(amount):
        roll_result += str(randint(1, dice_number))
        if i < amount-1:
            roll_result += ", "
    return roll_result
