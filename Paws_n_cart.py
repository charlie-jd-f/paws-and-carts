# This is an app so users can view their shopping cart, add and remove items from
# their carts, and calculate the total cost

# Create list to store items and prices
shopping_cart = []
price = []

print("Welcome to Paws n Cart! \n")

while True:

    # Display the cart to the user
    print('-'*60)
    print("This is your shopping cart:")
    if len(shopping_cart) == 0:
        pass
    else:
        for i in range(len(shopping_cart)):
            print(f"{shopping_cart[i]} \t \t £{price[i]}")
    print('-'*60)

    # Create a menu for the user
    print("Would you like to: \n")
    print("1. View the cost of your cart")
    print("2. Add an item to your cart")
    print("3. Remove an item from your cart")
    print("4. Check out \n")

    option = input("Enter the number of the option you would like to choose: \n")

    if option == '1':

        # Calculate the total cost in each list
        total = 0.0
        if len(shopping_cart) == 0:
            print("Your cart is empty. " \
                  "Add items to your list to calculate the total cost. \n")
        else:
            for i in range(len(shopping_cart)):
                total += price[i]
            print(f"The total cost of your cart is £{total}")

    elif option == '2':

        # Ask user for information about the item to add
        new_item = input("What would you like to add to your cart? \n")
        quantity = int(input("How many items would you like to add? \n"))
        cost = float(input("What is the cost of the item? \n"))
        i = 1

        # Add the item to the list
        while i <= quantity:
            shopping_cart.append(new_item)
            price.append(cost)
            i += 1

    elif option == '3':

        # ask user for information about the item to remove
        remove_item = input("What would you like to remove from your cart? \n")
        quantity = int(input("How many items would you like to remove? \n"))

        # count how many items are in the 
        counter = 0
        for item in shopping_cart:
            if item == remove_item:
                counter += 1
        
        # remove the item from the list, if it is in the list
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

    elif option == '4':

        # exit the loop and end the application 
        print('-'*60)
        print("Thank you for using Paws n Cart. Good bye!")
        break

    else:
        print("Request not recognised. Please try again. \n")