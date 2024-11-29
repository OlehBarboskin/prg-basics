def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()
file_lines =  sorted(file_lines)

# prints the array
for line in file_lines:
   print(line)
