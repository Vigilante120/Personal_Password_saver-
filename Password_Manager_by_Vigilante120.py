def manage():
    print("Welcome to Password Manager Ver1.0 By Vigilante120")
    filename = input("\nEnter Filename: ")
    f = open(filename + '.txt', "w+")
    print()
    print("-*" * 40)
    website = input("\nPlease enter Website Name: ")
    user = input("Enter the E-Mail or Username: ")
    password = input("Enter the password here: ")
    print("-*" * 40)
    web2 = ("Website: " + website)
    u2 = ("\nEmail: " + user)
    pw2 = ("\nPassword: " + password)
    design = ("\n<===========================x==========================>")
    f.write(web2)
    f.write(u2)
    f.write(pw2)
    f.write(design)
    f.close()


manage()



