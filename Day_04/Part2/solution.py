import re

def winning_numbers(game: str) -> int:
    """
    Finds the number of winning numbers for each card

    Args:
        game: String containing the game number, winning numbers, and numbers on our card

    Returns:
        Number of correct numbers
    """
    numbers = re.findall(r'\w+', game)
    winning_numbers = numbers[2:12]
    card_numbers = numbers[12:]

    correct_numbers = 0    

    for num in winning_numbers:
        if num in card_numbers:
            correct_numbers += 1

    return correct_numbers


def point_counter(points_earned: list) -> int:
    """
    Tallies up the points using the system in part 2

    Args:
        card_games: List of points earned for each game

    Returns:
        Sum of the number of cards earned
    """
    number_of_cards = [1]*201

    for card in range(len(points_earned)):
        for i in range(1,points_earned[card]+1):
            if card + i > 200:
                break
            else:
                number_of_cards[card + i] += number_of_cards[card]

    return sum(i for i in number_of_cards)


with open("input.txt", "r") as cards:
    wins = []

    for game in cards:
        wins.append(winning_numbers(game))

    print(point_counter(wins))
