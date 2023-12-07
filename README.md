# paws-and-carts
This is a Python project where a user can add/remove 'pet accessories' and the price, to build a shopping cart to calculate costs. This project involved the use of conditional statements, iterations, and manipulating lists. 

The users shopping cart will show to the user
Then they will have to select an option from the list:
1. View the cost of the cart
2. Add an item to the cart
3. Remove an item to the cart
4. Check out

If the user wants to view the cost of the cart, the code first checks the cart isn't empty to avoid a IndexError.
If there is something in the cart, it will use the price list to find the total using a while loop

If the user wants to add something to the cart, they will type in the item, how many items, and the price.
The item will be added to the list, if there is more then one, it will be added multiple times.
The price will be added to a separate list.

If the user wants to remove an item, the code asks which item to remove, and how many they want to move
The code checks this item is in the cart, and how many are in the cart to avoid any IndexErrors.
If the item is in the cart, and there is more than the user wants to remove, this amount of items will be removed.
The corresponding price will be removed from the price list.

The checkout option will end the program.
