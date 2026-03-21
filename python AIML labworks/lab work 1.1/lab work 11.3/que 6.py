class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email or not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailError("Invalid email address")
    print("Valid email")

# validate_email("user@gmail.com")
validate_email("usergmail.@com")


# output:-

# if its well formated then valid 
# Valid email   
# if its not well formatted than invalid             
# raise InvalidEmailError("Invalid email address") 