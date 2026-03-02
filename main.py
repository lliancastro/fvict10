from pyscript import display, document # type: ignore

def account_creation(e):
    document.getElementById('output').innerHTML = " "

    username = document.getElementById('username').value
    username_length = len(username)

    password = document.getElementById('password').value
    password_length = len(password)  

    letter_checker = False
    number_checker = False
    for req in password:
        if req.isalpha():
            letter_checker = True
        if req.isdigit():
            number_checker = True

    if not username_length < 7:
        if not password_length < 10:
            if letter_checker == True:
                if number_checker == True:
                    display("You've Successfully Created Acoount", target="output", append=False)
                else:
                    display(f"""Account Creation Failed, Password must contain at least one number .""", target="output", append=False)
            elif letter_checker == False and number_checker == False:
                display(f"""Account Creation Failed, Password must contain at least one number and one letter.""", target="output", append=False)
            else:
                display(f"""Account Creation Failed, Password must contain at least one letter.""", target="output", append=False)
        else:
            if letter_checker == False or number_checker == False:
                display(f"""Account Creation Failed, Password must contain at least 10 digits, one number, and one letter.""", target="output", append=False)
            else:
                display(f"""Account Creation Failed, Password must contain at least 10 digits.""", target="output", append=False)
    
    elif not password_length < 10:
        if letter_checker == True:
            if number_checker == True:
                display(f"""Account Creation Failed, Username must contain at least 7 digits, Password is acceptable.""", target="output", append=False)
            else:
                display(f"""Account Creation Failed, Username must contain at least 7 digits, Password must contain at least one number.""", target="output", append=False)
        elif letter_checker == False and number_checker == False:
            display(f"""Account Creation Failed, Username must contain at least 7 digits, Password must contain at least one number and one letter.""", target="output", append=False)
        else:
            display(f"""Account Creation Failed, Username must contain at least 7 digits, Password must contain at least one letter.""", target="output", append=False)
    else:
        if letter_checker == False or number_checker == False:
            display(f"""Account Creation Failed, Username must contain at least 7 digits, one number, and one letter.""", target="output", append=False)
        else:
            display(f"""Account Creation Failed, Username must contain at least 7 digits.""", target="output", append=False)
