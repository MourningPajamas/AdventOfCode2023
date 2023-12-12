import re

def cube_max_count(game: str) -> tuple:
    """ 
    Takes in game and returns the game ID and max cubes shown for each color 

    Args:
        game: A string that contains the game ID and max cube count for each color

    Returns:
        Tuple with (game_id, red, green, blue) where red, green, and blue are the max counts shown for that color
    """
    red = 0
    green = 0
    blue = 0

    split_game = game.split()
    game_id = int(split_game[1][:-1])
    split_game.reverse()

    for i in range(len(split_game)-2):
        if re.sub(r'\W', '', split_game[i]) == 'red' and int(split_game[i+1]) > red:
            red = int(split_game[i+1])
        if re.sub(r'\W', '', split_game[i]) == 'green' and int(split_game[i+1]) > green:
            green = int(split_game[i+1])
        if re.sub(r'\W', '', split_game[i]) == 'blue' and int(split_game[i+1]) > blue:
            blue = int(split_game[i+1])


    return (game_id, red, green, blue)

def is_possible_game(game_stats: tuple) -> int:
    """
    Verifies if the game is possible and if so returns the game ID

    Args:
        game_stats: Tuple that contains (game_id, red_max_shown, green_max_shown, blue_max_shown)

    Returns:
        game_id if the game is possible, 0 otherwise
    """

    #If the max shown is greater than the 
    if game_stats[1] > 12:
        return 0
    elif game_stats[2] > 13:
        return 0
    elif game_stats[3] > 14:
        return 0
    
    return game_stats[0]

with open("input.txt", "r") as games:
    id_sum = 0
    for game in games:
        stats = cube_max_count(game)
        id_sum += is_possible_game(stats)

    print(id_sum)
