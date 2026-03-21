print("Menu-drive fastfood order system.")
print()
print ("Press 1 to order Sandwich.")
print ("Press 2 to order Pizza.")
print ("Press 3 to order Burger.")

print()
mo=int(input("Enter Your food Order :"))
print()

match mo:
    case 1:
        print("Select the type of sandwich")
        print (" 1 Regulaur Sandwich.")
        print (" 2 Grill Sandwich.")
        print (" 3 Veg Sandwich.")
        print()

        to=int(input("Enter type of sandwhich:"))
        match to:
            case 1:
                print(" Regulaur Sandwich order placed.")
            case 2:
                print(" Grill Sandwich order placed.")
            case 3:
                print(" Veg Sandwich order placed.")

    case 2:
        print("Select the type of Pizza")
        print (" 1 Thin Crust Pizza.")
        print (" 2 Cheeze Brust Pizza.")
        print (" 3 Fresh Dough Pizza.")
        print()

        to=int(input("Enter type of Pizza:"))
        match to:
            case 1:
                print(" Thin Crust Pizza order placed.")
            case 2:
                print(" Cheeze Brust Pizza order placed.")
            case 3:
                print(" Fresh Dough Pizza order placed.")

    case 3:
        print("Select the type of Burger")
        print (" 1 Shezwan Burger.")
        print (" 2 Cheese Burger.")
        print (" 3 Panner tikki Burger.")
        print()

        to=int(input("Enter type of Burger:"))
        match to:
            case 1:
                print(" Shezwan Burger order placed.")
            case 2:
                print(" Cheese Burger order placed.")
            case 3:
                print(" Panner tikki order placed.")


print()
print("Thank you for your order.")
print ("Please wait for a while to prepare your order.")