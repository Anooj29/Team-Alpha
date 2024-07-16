class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Quantity Available: {self.quantity}")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))
        print(f"Added {quantity} of '{product.name}' to the cart.")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

    def display_cart(self):
        print("\nShopping Cart:")
        for product, quantity in self.items:
            print(f"{product.name} - Quantity: {quantity}")

    def checkout(self):
        self.display_cart()
        print(f"\nTotal Amount Payable: ${self.calculate_total()}")

    def clear_cart(self):
        self.items = []
        print("Shopping cart cleared.")


def main():
    cart = ShoppingCart()

    while True:
        print("\n1. Add Product to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Clear Cart")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Quantity: "))
            product = Product(product_id, name, price, quantity)
            cart.add_item(product, quantity)

        elif choice == "2":
            cart.display_cart()

        elif choice == "3":
            cart.checkout()

        elif choice == "4":
            cart.clear_cart()

        elif choice == "5":
            print("Thank you for shopping with us!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
