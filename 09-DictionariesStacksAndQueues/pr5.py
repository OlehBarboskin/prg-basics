paragraph = "cat dog mouse cat rat cat mouse"
para = {
}
words = paragraph.split(" ")
for a in words:
    if not a in para:
        para [a] = 1
    else:
        [a] = [a] + 1
print (f'{words}')

