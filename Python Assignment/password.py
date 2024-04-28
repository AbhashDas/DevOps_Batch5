# Function to validate the strength of the password
def check_password_strength(pwd):
    low,up,dig,sp = 0, 0, 0, 0
    # condition to check if the password length is greater than 8
    if len(pwd) >= 8:
        for i in pwd: # iterate each character of the password
            if i.islower(): #check if the password has lowercase characters
                low += 1
            
            if i.isupper(): #check if the password has uppercase characters
                up +=1

            if i.isdigit(): #check if the password has digits
                dig +=1

            if i in ('@','$','#','%','!','&'): #check if the password has special characters
                sp +=1

    # returns 1 if all the validation for the password is passed
    if low >= 1 and up >= 1 and dig >= 1 and sp >= 1: 
        return 1
    # returns 0 if the password validation fails
    else:
        return 0
    
# Accept password input from the user
pwd = input("Please, enter your password: ")

# calling the function to check the validity of the password and accepting a boolean return
valid = check_password_strength(pwd)

# providing feedback to the user based on the return from the validity function
if valid == 1:
    print("Your password is strong and secure.")
else:
    print("""Your password is NOT strong!!!
        - Password needs to be atleast 8 characters long.
        - Password needs to have atleast one uppercase character.
        - Password needs to have atleast one lowercase character.
        - Password needs to have atleast one digit.
        - Password needs to have atleast one special character('@','$','#','%','!','&'). """)
