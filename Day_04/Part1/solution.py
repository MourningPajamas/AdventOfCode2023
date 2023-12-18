import re

def winning_numbers(game: str) -> int:
    """
    Finds the number of winning numbers for each card

    Args:
        game: String containing the winning numbers and numbers on our card

    Returns:
        Points earned on the card
    """
    numbers = re.findall(r'\w+', game)
    winning_numbers = numbers[2:12]
    card_numbers = numbers[12:]

    correct_numbers = 0    

    for num in winning_numbers:
        if num in card_numbers:
            correct_numbers += 1

    if correct_numbers == 0:
        return 0
    else:
        return 2 ** (correct_numbers - 1) 


with open("input.txt", "r") as cards:
    points = 0

    for game in cards:
        points += winning_numbers(game)
    
    print(points)
