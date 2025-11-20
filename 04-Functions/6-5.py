def letter_e_count(phrase):
    counter = 0
    for char in phrase:
        if char == 'e' or char == 'E':
            counter += 1
    return counter

if __name__ == '__main__':
    input_phrase = input('Enter a phrase: ')
    print(f'The number of letters "e" in the phrase is {letter_e_count(input_phrase)}')