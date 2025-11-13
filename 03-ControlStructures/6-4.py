new_password = input("Enter new password: ")
if len(new_password) < 12:
    print("Password too short, must be at least 12 characters.")
else:
    print("Password long enough")