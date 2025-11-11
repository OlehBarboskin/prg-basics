plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    encrypted_text = encrypted_text +chr(ord(char) + 1) 

print(f'Encrypted text: {encrypted_text}')