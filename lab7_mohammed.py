# ==========================================
# DAY 1 — Build your items
# ==========================================

# TICKET 1: Your item blueprint
class Sneaker:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # TICKET 3: The price guard (encapsulation)
    def set_price(self, amount):
        if amount < 0:
            print("Error: Price cannot be negative!")
        else:
            self.price = amount

    # TICKET 5: Each item's own action (polymorphism)
    def deliver(self):
        print(f"Shipping your {self.name}s!")


# TICKET 2: Make your real items
item1 = Sneaker("Air Max", 120)

# PREDICT Ticket 2: print(item1.name) will output "Air Max"
print(item1.name)

# PREDICT Ticket 3:
# Running item1.set_price(-5) will print "Error: Price cannot be negative!"
item1.set_price(-5)  # Break it on purpose to test


# TICKET 4: A second kind of item (inheritance)
class Slide(Sneaker):
    pass  # Copies everything from Sneaker

    # TICKET 5: Override deliver for Slide (polymorphism)
    def deliver(self):
        print(f"Sliding out the door with your {self.name}s!")


# EXPLAIN Ticket 5:
# Why can the same method name do two different things?
# Answer: Because child classes can override methods inherited from parent classes,
# allowing each class to define its own specific behavior for the same action (polymorphism).

item2 = Slide("Cloud Slide", 45)


# ==========================================
# DAY 2 — Build your store
# ==========================================

# TICKET 6: Your cart
class Cart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    # TICKET 9: Checkout (abstraction)
    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()  # Runs each item's specific deliver action
            total += item.price
        print(f"Total: ${total}")


# TICKET 7: Your menu and cart
store = {
    "1": item1,
    "2": item2
}
cart = Cart()


# TICKET 8: Let customers shop & TICKET 10: Test the whole app
# PREDICT Ticket 8:
# Picking '1' adds item1 (Air Max) to the cart and prints "Air Max added!"

while True:
    choice = input("Pick 1, 2, or 'done': ").strip()
    
    if choice == "done":
        break
    elif choice in store:
        selected_item = store[choice]
        cart.add(selected_item)
        print(f"{selected_item.name} added!")
    else:
        print("Invalid selection. Try again.")

# Run Checkout at the end
cart.checkout()
