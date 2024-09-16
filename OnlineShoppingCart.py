import shutil

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description

    @property
    def total_cost(self):
        return float(self.item_price * self.item_quantity)

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.total_cost:.2f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020", cart_total=0.0, num_items=0):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items: ItemToPurchase = []
        self.cart_total = cart_total
        self.num_items = num_items

    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)
        self.cart_total += item.total_cost
        self.num_items += item.item_quantity

    def remove_item(self, item_name: str):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_total -= item.total_cost
                self.num_items -= item.item_quantity
                self.cart_items.remove(item)
                print(f"{item.item_name} removed.")
                return
        
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, item: ItemToPurchase):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                self.cart_total -= cart_item.total_cost
                self.num_items -= cart_item.item_quantity

                cart_item.item_price = float(item.item_price)
                cart_item.item_quantity = int(item.item_quantity)
                cart_item.item_description = item.item_description

                self.cart_total += cart_item.total_cost
                self.num_items += cart_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return self.num_items

    def get_cost_of_cart(self):
        return self.cart_total
    
    def print_total(self):
        print(center_text("OUTPUT SHOPPING CART"))
        print(center_text(f"{self.customer_name}'s Shopping Cart - {self.current_date}"))
        if self.get_num_items_in_cart() == 0:
            print(center_text("SHOPPING CART IS EMPTY"))
        else:
            print(center_text(f"Number of Items: {self.get_num_items_in_cart()}"))
            print()
            for item in self.cart_items:
                print(center_text(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item.total_cost:.2f}"))
            print()
            print(center_text(f"Total: ${self.get_cost_of_cart():.2f}"))

    def print_descriptions(self):
        print(center_text("OUTPUT ITEMS' DESCRIPTIONS"))
        print(center_text(f"{self.customer_name}'s Shopping Cart - {self.current_date}"))
        if len(self.cart_items) == 0:
            print(center_text("SHOPPING CART IS EMPTY"))
        else:
            print(center_text("Item Descriptions"))
            for item in self.cart_items:
                print(center_text(f"{item.item_name}: {item.item_description}"))

def print_menu(cart: ShoppingCart, user_input: str):
    while user_input != 'q':
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_input = input("Choose an option: ")
        if user_input == 'q':
            break
        elif user_input == "a":
            item_name = input("Enter the name of the item: ")
            item_price = float(input("Enter the price of the item: "))
            item_quantity = int(input("Enter the quantity of the item: "))
            item_description = input("Enter the description of the item: ")
            cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))

        elif user_input == "r":
            item_name = input("Enter the name of the item to remove: ")
            cart.remove_item(item_name)

        elif user_input == "c":
            item_name = input("Enter the name of the item to change: ")
            item_price = float(input("Enter the new price of the item: "))
            item_quantity = int(input("Enter the new quantity of the item: "))
            item_description = input("Enter the description of the item: ")
            cart.modify_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))

        elif user_input == "i":
            cart.print_descriptions()

        elif user_input == "o":
            cart.print_total()
    
def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    return text.center(terminal_width)

def main():
    
    cart_name = input("Enter customer's name: ")
    cart_date = input("Enter today's date: ")
    cart = ShoppingCart(cart_name, cart_date)
    print_menu(cart, "")

if __name__ == "__main__":
    main()