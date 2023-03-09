# Define passwords for three levels
level1_password = "password1"
level2_password = "password2"
level3_password = "password3"

# Get user input for level 1 password
password1_input = input("Enter Level 1 Password: ")
if password1_input == level1_password:
    print("Access granted to Level 1")
    # Get user input for level 2 password
    password2_input = input("Enter Level 2 Password: ")
    if password2_input == level2_password:
        print("Access granted to Level 2")
        # Get user input for level 3 password
        password3_input = input("Enter Level 3 Password: ")
        if password3_input == level3_password:
            print("Access granted to Level 3")
        else:
            print("Incorrect Level 3 Password")
    else:
        print("Incorrect Level 2 Password")
else:
    print("Incorrect Level 1 Password")
