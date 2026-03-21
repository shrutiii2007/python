print("menu driven calling sustem.")
print()
print ("Press 1 for english.")
print ("Press 2 for Hindi.")
print ("Press 3 for Gujrati")

print()
mo=int(input("Enter Your choosen langugae :"))
print()

match mo:
    case 1:
        print("Select the option for the procedure :-")
        print (" 1 update the number.")
        print (" 2 Enable the number.")
        print (" 3 change the number.")
        print()

        to=int(input("To continue the process, please choose an option.:"))
        match to:
            case 1:
                print("your request of updating the number is under process")
            case 2:
                print("your request of Enabling the number is under process.")
            case 3:
                print("your request of changing the number is under process.")

    case 2:
        print("Procedure ke liye option select kijiye.:-")
        print (" 1 number ko update krna hai.")
        print (" 2 number ko enable krna hai.")
        print (" 3 number ko change krna hai.")
        print()

        to=int(input("age ki process jari rkhne ke liye ek option choose ki jiye:"))
        match to:
            case 1:
                print("  Aapka number update karne ka anurodh prakriya mein hai..")
            case 2:
                print("  Aapka number enable karne ka anurodh prakriya mein hai..")
            case 3:
                print("  Aapka number change karne ka anurodh prakriya mein hai..")

    case 3:
        print(" Prakriya mate no vikalp pasand karo ")
        print (" 1 Number update karvano chhe.")
        print (" 2 Number enable karvano chhe.")
        print (" 3 Number change karvano chhe.")
        print()

        to=int(input("Prakriya aagal chalu rakhva mate krupaya ek vikalp pasand karo.:"))
        match to:
            case 1:
                print(" Tamaru number update karva no anurodh prakriya maa chhe..")
            case 2:
                print(" Tamaru number enable karva no anurodh prakriya maa chhe..")
            case 3:
                print(" Tamaru number change karva no anurodh prakriya maa chhe..")


print()
print("Thank you for your information.")
print ("Please wait for a while we make the cahnges as per your instructions.")