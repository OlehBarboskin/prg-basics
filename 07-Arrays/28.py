# def f(string):
#     number_of_words = len(string.split())
#     return number_of_words
# input_string = "An apple a day keeps the doctor away"
# print(f(input_string))  # Output: 6

def ordered_array_of_words_shortest_longest(string):
    words = string.split()
    words.sort(key=len)
    return words
input_string = "An apple a day keeps the doctor away"
print(ordered_array_of_words_shortest_longest(input_string))  # Output: ['An', 'a', 'day', 'keeps', 'apple', 'doctor', 'away', 'the']

def alphabetical_array_of_words(string):
    words = string.split()
    words.sort()
    return words
input_string = "An apple a day keeps the doctor away"
print(alphabetical_array_of_words(input_string))  # Output: ['An', 'a