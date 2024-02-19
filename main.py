import products
import store
import promotions


def display_menu():
    print("\nStore Menu:\n___________")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_all_products(shop):
    print("\nAll Products in Store:")
    count = 1
    for product in shop.get_all_products():
        print(f"{count}. {product.show()}")
        count += 1


def show_total_amount(shop):
    total_quantity = shop.get_total_quantity()
    print(f"\nTotal Amount in Store: {total_quantity}")


def make_an_order(shop):
    order_list = []

    list_all_products(shop)
    print("\n")

    while True:
        prod_num = input("Enter product number (or just 'press enter' to finish): ")
        if prod_num == '':
            break

        prod_num = int(prod_num)    

        all_products = shop.get_all_products()  # List of all the products available

        if prod_num > len(all_products) or prod_num <= 0:
            print(f"Invalid product number. Please enter a valid product number from 1 - {len(all_products)}")
            continue

        product = all_products[prod_num - 1]
        quantity = int(input(f"Enter the quantity you want: "))

        if product and product.is_active():
            order_list.append((product, quantity))
            print("Product added to list\n")
        else:
            print(f"Item is not available in the store or is inactive.")

    total_order_price = shop.order(order_list)
    print(f"Total Order Price: {total_order_price}")


if __name__ == "__main__":
    # # setup initial stock of inventory
    # product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
    #                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    #                 products.Product("Google Pixel 7", price=500, quantity=250),
    #                 products.NonStockedProduct("Windows License", price=125),
    #                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    #                 ]

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    while True:
        display_menu()

        try:
            choice = int(input("Please choose a number: ").strip())
            if choice == 1:
                list_all_products(best_buy)
            elif choice == 2:
                show_total_amount(best_buy)
            elif choice == 3:
                make_an_order(best_buy)
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
