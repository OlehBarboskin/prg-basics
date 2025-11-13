def input_string(message):
    return input(message)

def input_integer(message):
    return int(input(message))

if __name__ == "__main__":
    print("Please enter a string:")
    name = input_string("Name: ")
    age = input_integer("Age: ")
    print(f'Hello, {name}. You are {age} years old.')