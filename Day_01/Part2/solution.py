import regex as re

def number_solver(word: str) -> int:
    """
    Finds the numbers in the word and returns the two digit value using the problem criteria

    Args:
        word: String that may contain numbers or digit words

    Return:
        Two digit value using problem criteria
    """
    numbers = re.findall(r'[1-9]|one|two|three|four|five|six|seven|eight|nine', word, overlapped=True)

    conversion = {"1": "1",
                  "2": "2",
                  "3": "3",
                  "4": "4",
                  "5": "5",
                  "6": "6",
                  "7": "7",
                  "8": "8",
                  "9": "9",
                  "one": "1",
                  "two": "2",
                  "three": "3",
                  "four": "4",
                  "five": "5",
                  "six": "6",
                  "seven": "7",
                  "eight": "8",
                  "nine": "9"}

    value = conversion[numbers[0]] + conversion[numbers[-1]] 

    return int(value)


with open('input.txt', 'r') as input_file:
    total = 0

    for word in input_file:
        total += number_solver(word)

    print(total)
