sum = 0

with open('01\Part1\input.txt', 'r') as input_file:
    for word in input_file:
        letters_list = []
        two_digit_string = ""
        for letter in word:
            if letter.isdigit():
                letters_list.append(letter)
        if len(letters_list) == 1:
           two_digit_string = letters_list[0] + letters_list[0] 
        elif len(letters_list) != 0:
            two_digit_string = letters_list[0] + letters_list[-1]

        sum += int(two_digit_string)

print(sum) 