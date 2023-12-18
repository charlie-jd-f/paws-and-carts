# This is an app so users can view their shopping cart, add and remove items from
# their carts, and calculate the total cost

# Create list to store items and prices
shopping_cart = []
price = []

# Create list to store products and prices
products = ["Dog Food","Cat Food","Fish Food","Dog Walking Lead",
            "Cat Nip","Aquarium Castle"]
product_cost = [8,8,5,12,6,15]

print("Welcome to Paws n Cart! \n")

while True:

    print('-'*60)
    print("This is your shopping cart:\n")
    if len(shopping_cart) == 0:
        pass
    else:
        total = 0.0

        for item in products:
            num = 0
            cost = 0
            for i in range(len(shopping_cart)):
                if item == shopping_cart[i]:
                    num += 1
                    cost += price[i]
            if num != 0:
                print(f"{item:<25} x{num:<25} £{cost:<25}")


        # Display the total cart of the shopping cart
        for j in range(len(shopping_cart)):
                total += price[j]
        print(f"\nThe total cost of your cart is £{total}")
    print('-'*60)

    # Create a menu for the user
    print("Would you like to: \n")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. Check out \n")

    option = input("Enter the number of the option you would like to choose: \n")

    if option == '1':
       
        # Display the products menu to the user:
        print("-"*60)
        print("Products: ")
        for i in range(1,len(products)+1):
            print(f"{i}. {products[i-1]:<25} £{product_cost[i-1]:<25}")
        print("-"*60)

        # User to input an item from the list of products
        while True:
            new_item_num = int(input("Enter the product you would like to add: \n"))
            if (new_item_num) in range(1,len(products)+1):
                new_item = products[new_item_num-1]
                cost = product_cost[new_item_num-1]
                break
            else:
                print("Item not on the list. Please try again")
                new_item_num = int(input("Enter the product number: "))

        # check the user inputs a int only
        while True:
            try:
                quantity = int(input("How many items would you like to add? \n"))
                break
            except ValueError:
                print("Input Error: Please only enter a number (using 0 to 9)")

        # Add the correct amount of items to the list
        i = 1
        while i <= quantity:
            shopping_cart.append(new_item)
            price.append(cost)
            i += 1

    elif option == '2':

        if len(shopping_cart) == 0:
            print("You have no items in your cart to remove.")

        else:
            reduced_cart = []
            # print list of products and quantity of items
            print('-'*60)
            j = 1
            print("Your current shopping cart: \n")
            for item in products:
                num = 0
                for i in range(0,len(shopping_cart)):
                    if item == shopping_cart[i]:
                        num += 1

                        # create a reduced list containing products only
                        if item in reduced_cart:
                            pass
                        else:
                            reduced_cart.append(item)

                if num != 0:
                    print(f"{j}. {item:<25} x{num:<25}")
                    j+=1

            print('-'*60)

            # ask user for information about the item to remove
            # ensure user types in a number, and the number is in range
            print("J =",j)
            while True:
                try:
                    remove_item_num = int(input("Enter the number for which product you would" \
                                        +" like to remove? \n"))
                    if remove_item_num >= j:
                        print("Input Error: The number you entered is not recognised.")
                    elif remove_item_num <= 0:
                        print("Input Error: The number you entered is not recognised.")
                    else: 
                        remove_item = reduced_cart[remove_item_num-1]
                        break
                except ValueError:
                    print("Input Error: Please only enter a number (using 0 to 9)")
            
            # ensure user cannot type a string or char
            while True:
                try:
                    quantity = int(input("How many items would you like to remove? \n"))

                    # count how many items are in the cart
                    counter = 0
                    for item in shopping_cart:
                        if item == remove_item:
                            counter += 1
                    
                    # remove the item from the list, if there is enough in the list
                    if counter == 0:
                        print("This item is not in your list.")
                    elif counter < quantity:
                        print(f"You cannot remove this amount. \n"
                            f"The amount of \"{remove_item}\" in your cart is {counter}.")
                    else:
                        i = 0
                        while i < quantity:
                            index = shopping_cart.index(remove_item)
                            shopping_cart.pop(index)
                            price.pop(index)
                            i += 1
                        break
                except ValueError:
                    print("Input Error: Please only enter a number (using 0 to 9)")

    elif option == '3':

        # exit the loop and end the application 
        print('-'*60)
        print("Thank you for using Paws n Cart. Good bye!")
        break

    else:
        print("Request not recognised. Please try again. \n")