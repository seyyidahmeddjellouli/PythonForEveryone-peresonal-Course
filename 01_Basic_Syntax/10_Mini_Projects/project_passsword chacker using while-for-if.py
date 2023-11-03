while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password should be at least 8 characters long.")
        continue

    has_letter = False
    has_number = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True

    if has_letter and has_number:
        print("Password is valid.")
        break
    else:
        print("Password should contain both letters and numbers.")
