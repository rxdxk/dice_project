import random

def roll_dice(dice_number, die_sides):
    results = []
    for _ in range(dice_number):
        roll = random.randint(1, die_sides)
        results.append(roll)
    return results

def calculate_total(rolls, modifier):
    return sum(rolls) + modifier

def calculate_range(dice_number, die_sides, modifier):
    min_val = dice_number * 1 + modifier
    max_val = dice_number * die_sides + modifier
    avg_val = (min_val + max_val) / 2
    return min_val, avg_val, max_val
