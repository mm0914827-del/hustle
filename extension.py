class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Ticket 2: Method inside Item class
    def set_price(self, amount):
        if amount < 0:
            print("Price cannot be less than zero!")
        else:
            self.price = amount

import random  # Ticket 1: Put at the VERY TOP of your file

# --- SETUP: Store Items & Cart ---
item1 = Item("Python 101", 15)
item2 = Item("Space Cats", 15)

# Dictionary of items on sale/available
store = {1: item1, 2: item2}

cart = []  # List to store selected items

# --- TICKET 1: A Random Welcome ---
welcome_messages = [
    "Hey there, happy shopping!",
    "Welcome to our store!",
    "Glad you're here today!",
]
print(random.choice(welcome_messages))

# --- TICKET 2: Put an Item on Sale ---
# Lower price for item1 and print notification
item1.set_price(10)
print(item1.name + " is on sale for $" + str(item1.price) + "!")

# --- TICKET 3: Show the Menu ---
print("Here is what we have:")
for number, item in store.items():
    print(str(number) + ": " + item.name + " - $" + str(item.price))

# --- TICKET 4: Handle a Wrong Choice (Shopping Loop) ---
while True:
    choice = input("Pick a number, or 'done': ")

    if choice == "done":
        break
    elif choice.isdigit() and int(choice) in store:
        selected_item = store[int(choice)]
        cart.append(selected_item)
        print(selected_item.name + " added!")
    else:
        print("Sorry, that's not on the menu!")

# --- TICKET 5: Print a Receipt ---
print("----- Your receipt -----")
total_cost = 0

for item in cart:
    print(item.name + " ..... $" + str(item.price))
    total_cost += item.price

# --- TICKET 6: Count the Order ---
print("You bought " + str(len(cart)) + " items.")
print("Mailing it!")
print("Total: $" + str(total_cost))
