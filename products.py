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
        self.promotion = None

    def get_quantity(self):
        return int(self.quantity)

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        if self.quantity <= 0:
            return False
        return True

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        if self.promotion:
            promotion_info = f", Promotion: {self.promotion.name}"
            return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}"
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            print(f"Sorry, {self.name} is currently unavailable for purchase.")
            return 0.0
        elif quantity > self.quantity:
            raise ValueError("Quantity requested is too large.")
        elif self.quantity >= quantity:
            self.quantity -= quantity
            print(f"Successfully purchased {quantity} {self.name}(s), Remaining quantity: {self.quantity}.")
            if self.quantity == 0:
                self.deactivate()
            elif self.promotion:
                return self.promotion.apply_promotion(self, quantity)
            return quantity * self.price
        else:
            print(f"Insufficient quantity of {self.name} available.")
            return 0.0

    def set_promotion(self, promotion):
        self.promotion = promotion

    def remove_promotion(self):
        self.promotion = None


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def is_active(self):
        if self.quantity < 0:
            return False
        return True

    def show(self):
        if self.promotion:
            promotion_info = f", Promotion: {self.promotion.name}"
        else:
            return f"{self.name}, Price: ${self.price}"
        return f"{self.name}, Price: ${self.price}{promotion_info}"

    def buy(self, quantity):
        if not self.active:
            print(f"Sorry, {self.name} is currently unavailable for purchase.")
            return 0.0
        elif quantity > self.quantity:
            print(f"Successfully purchased {quantity} {self.name}(s).")
            return quantity * self.price
        else:
            print(f"Insufficient quantity of {self.name} available.")
            return 0.0


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)  # overwrites the quantity to 1
        self.maximum = maximum
        self.times_purchased = 0

    def buy(self, quantity):
        if self.times_purchased + quantity > self.maximum:
            raise ValueError(f"Exceeded purchase limit of {self.maximum} for {self.name}.")
        self.times_purchased += quantity
        return super().buy(quantity)


if __name__ == "__main__":

    try:
        bose = Product("Bos QuietComfort Earbuds", price=250, quantity=500)
        mac = Product("MacBook Air M2", price=1450, quantity=100)
        windows = NonStockedProduct("Windows License", price=125)
        shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

        print(bose.buy(50))
        print(mac.buy(90))
        print(windows.is_active())
        print(windows.buy(4))
        print(shipping.buy(1))

        bose.show()
        mac.show()
        windows.show()

        bose.set_quantity(1000)
        bose.show()
    except ValueError as e:
        print(f"Error: {e}")
