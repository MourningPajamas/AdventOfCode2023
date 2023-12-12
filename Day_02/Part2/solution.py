import re

def cube_min_count(game: str) -> tuple:
    """ 
    Takes in game and returns the max cubes shown for each color 

    Args:
        game: A string that contains the game ID and max cube count for each color

    Returns:
        Tuple with (red, green, blue) where red, green, and blue are the max counts shown for that color
    """
    red = 0
    green = 0
    blue = 0

    split_game = game.split()
    split_game.reverse()

    for i in range(len(split_game)-2):
        if re.sub(r'\W', '', split_game[i]) == 'red' and int(split_game[i+1]) > red:
            red = int(split_game[i+1])
        if re.sub(r'\W', '', split_game[i]) == 'green' and int(split_game[i+1]) > green:
            green = int(split_game[i+1])
        if re.sub(r'\W', '', split_game[i]) == 'blue' and int(split_game[i+1]) > blue:
            blue = int(split_game[i+1])


    return (red, green, blue)

def power_of_cubes(game_stats: tuple) -> int:
    """
    Calculates the power of a set of cubes by multiplying the count for each color

    Args:
        game_stats: Tuple that contains (red_max_shown, green_max_shown, blue_max_shown)

    Returns:
        Product of red_max_shown, green_max_shown, blue_max_shown
    """
     
    return game_stats[0]*game_stats[1]*game_stats[2]

with open("input.txt", "r") as games:
    cube_sum = 0
    for game in games:
        stats = cube_min_count(game)
        cube_sum += power_of_cubes(stats)

    print(cube_sum)
