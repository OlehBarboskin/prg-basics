def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content
file_content = read_from_file('pets.txt')
file_lines = file_content.split()
file_lines = len(file_lines)

print(file_lines)