def read_from_file(name):
   content=""
   with open(name, 'r') as file:
      content = file.readlines()
   return content
file_content = read_from_file('it_company.csv')
job_title = 'Software Engineer'
for line in file_content:
    if job_title in line:
        print (line)
