import Pizza  # import the Pizza class


def main():  # Initialize main()
    pizzas = []  # Create an array to hold pizza objects
    repeat = True
    name = str(input("Enter your name: "))

    while repeat:
        try:
            numPizzas = int(input("Enter number of pizzas: "))
            repeat = False

            for i in range(1, numPizzas + 1, 1):
                print("\bPizza #" + str(i))
                size = selectSize()
                size_price = sizePrice(size)
                toppings = selectToppings()
                shape = selectShape()
                crust = selectCrust()
                num_toppings = len(toppings)
                my_pizza = Pizza.Pizza(name, size, size_price, toppings, num_toppings, shape, crust)
                pizzas.append(my_pizza)

        except ValueError:
            print("Invalid entry. Try again.")



    menu(pizzas)


def menu(pizzas):
    repeat = True
    while repeat:
        try:
            print("1. Calculate\n"
                  "2. Start Over\n"
                  "3. Exit")
            
            selection = int(input("Enter the number of your selection: \n"))

            if selection == 1:
                calculate(pizzas)
                repeat = False
            elif selection == 2:
                main()
                repeat = False
            elif selection == 3:
                print("Thank you for using the Pizza Ordering Program!")
                exit()
            else:
                print("Invalid Entry. Try again.")
        except ValueError:
            print("Invalid Entry. Try again.")




def selectSize():
    largePrice = 15.95
    medPrice = 12.95
    smallPrice = 10.95
    repeat = True

    print("1. Large - $" + str(largePrice) +
          "\n2. Medium - $" + str(medPrice) +
          "\n3. Small - $" + str(smallPrice))

    while repeat:
        try:
            size = int(input("Choose the size for your pizza: "))
            if size == 1:
                return "Large"
            elif size == 2:
                return "Medium"
            elif size == 3:
                return "Small"
            else:
                print("Invalid Entry. Try again.")
        except ValueError:
            print("Invalid Entry. Try again.")




def sizePrice(size):
    if size == 'Large':
        return 15.95
    elif size == "Medium":
        return 12.95
    elif size == "Small":
        return 10.95


def selectToppings():
    price = 1.25
    total = 0
    toppingsList = []
    repeat = True

    print("1. Pepperoni\n"
          "2. Mushrooms\n"
          "3. Bacon\n"
          "4. Ham")

    while repeat:
        miniRepeat = True
        try:
            toppings = int(input("Enter the toppings you would like: "))

            if (toppings == 1):
                toppingsList.append("Pepperoni" + " - $" + str(price))
                total += price

            elif (toppings == 2):
                toppingsList.append("Mushrooms" + " - $" + str(price))
                total += price

            elif (toppings == 3):
                toppingsList.append("Bacon" + " - $" + str(price))
                total += price

            elif (toppings == 4):
                toppingsList.append("Ham" + " - $" + str(price))
                total += price
            else:
                print("Invalid Entry. Try again.")

        except ValueError:
            print("Invalid Entry. Try again.")

        while miniRepeat:
            try:
                another = str(input("Would you ike another topping? (Y|N): "))
                if another.lower() == 'y' or another.lower() == "yes":
                    miniRepeat = False
                elif another.lower() == 'n' or another.lower() == "no":
                    repeat = False
                    miniRepeat = False
                else:
                    print("Invalid entry. Try again.")
            except ValueError:
                print("Invalid entry. Try again.")

    return toppingsList


def selectShape():
    repeat = True

    print("\n1. Round\n"
          "2. Square")

    while repeat:
        try:
            shape = int(input("Enter the shape of the Pizza: "))

            if shape == 1:
                return "Round"

            elif shape == 2:
                return "Square"

            else:
                print("Invalid Entry. Try Again.")

        except ValueError:
            print("Invalid Entry. Try again.")


def selectCrust():
    repeat = True
    print("\n1. Thin\n"
          "2. Thick")

    while repeat:
        try:
            crust = int(input("Enter the Crust Type: "))

            if crust == 1:
                return "Thick"
            elif crust == 2:
                return "Thin"
            else:
                print("Invalid Entry. Try again.")

        except ValueError:
            print("Invalid Entry. Try again.")


def calculate(pizzas):
    for i in range(0, len(pizzas), 1):
        print()
        print("Customer Name: " + pizzas[i].get_name())
        print("Pizza Size: " + pizzas[i].get_size() + " - $" + str(pizzas[i].get_size_price()))
        print("Toppings: ")
        for n in range(0, len(pizzas[i].get_topping_names()), 1):
            print(pizzas[i].get_topping_names()[n])
        print("Shape: " + pizzas[i].get_shape())
        print("Crust: " + pizzas[i].get_crust())
        print("Subtotal: $" + format(pizzas[i].get_size_price() + (pizzas[i].get_num_toppings() * 1.25), '.2f'))
        print("\n\n\nThe program will now start over")
        main()

        
main()
