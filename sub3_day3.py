

def User ():
    print("Enter your information below")
    firstname_str = input("Enter Your First Name: ")
    firstname_int = str(firstname_str)
    middlename_str = input("Enter Your Middle Name: ")
    middlename_int = str(middlename_str)
    lastname_str = input("Enter Your last Name: ")
    lastname_int = str(lastname_str)
    phone_str = input("Enter Your Phone Number: ")
    phone_int = int(phone_str)
    gender_str = input("Enter Your Gender: ")
    gender_int = str(gender_str)
    DOB_str = input("Enter Your Date of Birth: ")
    DOB_int = str(DOB_str)
    email_str = input("Enter Your Email Address: ")
    email_int = str(email_str)
    occupation_str = input("Enter Your Occupation: ")
    occupation_int = str(occupation_str)
    details = "Your First Name is: ", firstname_int, "Your Middle Name is: ", middlename_int, "Your Last Name is: ", lastname_int, "Your Phone Number is: ", phone_int, "Your Gender is: ", gender_int, "Your Date of Birth is: ", DOB_int, "Your Email Address is: ", email_int, "Your Occupation is: ", occupation_int

    return details

print(User())
print("The Above Is all your information you provided :) ")