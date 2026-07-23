# --- Step 1: Make the book shape ---
class Book:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    # Step 3: Guard method against negative prices (Encapsulation)
    def set_price(self, amount):
        if amount < 0:
            print("A price can't be below zero!")
        else:
            self.price = amount

    # Step 5: How paper books are delivered
    def deliver(self):
        print("Mailing it!")


# --- Step 4 & 5: Add an ebook (Inheritance & Polymorphism) ---
class EBook(Book):
    # Overriding deliver method for ebooks
    def deliver(self):
        print("Downloading!")


# --- Step 6: Make a cart ---
class Cart:

    def __init__(self):
        self.items = []  # Starts empty

    def add(self, item):
        self.items.append(item)
        print(item.name + " added!")

    # Step 9: Add a checkout button (Abstraction)
    def checkout(self):
        total = 0
        for item in self.items:
            item.deliver()
            total = total + item.price
        print("Total: $" + str(total))


# --- Step 2: Make some real books ---
book1 = Book("Python 101", 20)
ebook1 = EBook("Space Cats", 15)

# --- Step 7: Put books on the shelf ---
store = {"1": book1, "2": ebook1}

cart = Cart()

# --- Step 8 & Interactive Loop ---
shopping = True
while shopping:
    choice = input("Pick 1, 2, or 'done': ")
    if choice == "done":
        shopping = False
    else:
        if choice in store:
            cart.add(store[choice])
        else:
            print("Invalid choice, try again.")

# Run checkout after finishing shopping
cart.checkout()