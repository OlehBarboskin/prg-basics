###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    p = 1
    for line in file:
        print(str(p) + " " + line, end ='')
        p += 1