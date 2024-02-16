import products


class Store:
    def __init__(self, product_list):
        if product_list:
            self.products = product_list
        else:
            self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print("product removed successfully!")
        else:
            print("Product does not exists.")

    def get_total_quantity(self):
        # Returns the total quantity of products in the store
        total_quantity = 0
        for product in self.products:
            if product.is_active():
                total_quantity += product.get_quantity()
        return int(total_quantity)

    def get_all_products(self):
        # Returns a list of all active products that are in the store
        all_products = []
        for product in self.products:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        # Gets a list of Tuples (Product, quantity) and returns the total price of the order
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
