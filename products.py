class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            print(f"Sorry, {self.name} is currently unavailable for purchase.")
            return 0.0
        elif self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Successfully purchased {quantity} {self.name}(s).")
            print(f"Remaining quantity: {self.quantity}")
            if self.quantity == 0:
                self.deactivate()
            return quantity * self.price
        else:
            print(f"Insufficient quantity of {self.name} available.")
            return 0.0


if __name__ == "__main__":

    try:
        bose = Product("Bos QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)

        print(bose.buy(50))
        print(mac.buy(100))
        print(mac.is_active())

        bose.show()
        mac.show()

        bose.set_quantity(1000)
        bose.show()
    except ValueError as e:
        print(f"Error: {e}")
      
