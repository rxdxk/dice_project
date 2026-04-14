from dice import roll_dice, calculate_total, calculate_range

def main():
    dice_number = int(input("Кількість кісток: "))
    die_sides = int(input("Кількість граней: "))
    modifier = int(input("Модифікатор (може бути від’ємний): "))

    rolls = roll_dice(dice_number, die_sides)
    total = calculate_total(rolls, modifier)
    min_val, avg_val, max_val = calculate_range(dice_number, die_sides, modifier)

    print(f"\nКидок кісток {dice_number}к{die_sides}{modifier:+}:")
    print(f"Значення кісток: {rolls}")
    print(f"Результат: {total}")
    print(f"Можливий діапазон [мін., сер., макс.]: [{min_val}, {avg_val}, {max_val}]")

if __name__ == "__main__":
    main()