# collect email from user
# slice or split the email using the @, the first part as the username, second part as a domain
# split domain using .

def main():
    print("Wellcome to program email slicer")
    print("")

    email_input = input("Input your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username: {username}")
    print(f"Domain: {domain}")
    print(f"Extension: {extension}")


a = True
while a == True:
    main()
    x = input("stop? (y/n)")
    if x == "n" or x == "N":
        a = True
    elif x == "y" or x == "Y":
        a == False
    else:
        print("Error")
