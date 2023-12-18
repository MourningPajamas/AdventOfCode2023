import regex as re

def number_solver(word: str) -> int:
    """
    Finds the numbers in the word and returns the two digit value using the problem criteria

    Args:
        word: String that may contain numbers

    Return:
        Two digit value using problem criteria
    """
    numbers = re.findall(r'[1-9]', word, overlapped=True)

    value = numbers[0] + numbers[-1]

    return int(value)


with open('input.txt', 'r') as input_file:
    total = 0

    for word in input_file:
        total += number_solver(word)

    print(total)
