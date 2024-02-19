import pytest
import products


# Test for a normal product
def test_normal_product_works():
    bose = products.Product("Bos QuietComfort Earbuds", price=250, quantity=500)
    assert bose.name == "Bos QuietComfort Earbuds"
    assert bose.price == 250
    assert bose.quantity == 500
    assert bose.active is True


# Test that when a product reaches 0 quantity, it becomes inactive.
def test_inactive_product():
    bose = products.Product("Bos QuietComfort Earbuds", price=250, quantity=0)
    assert bose.is_active() is False


# Test that negative price invokes exception
def test_negative_price():
    with pytest.raises(ValueError) as exc_info:
        products.Product("Bose Airpods", price=-10, quantity=100)
    assert str(exc_info.value) == "Price cannot be negative."


# Test that empty name invokes exception
def test_empty_name():
    with pytest.raises(ValueError) as exc_info:
        products.Product("", price=-10, quantity=100)
    assert str(exc_info.value) == "Name cannot be empty."


# Test that product purchase modifies the quantity and returns the right output.
def test_product_purchase_returns_right_output():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    if bose.buy(5):
        assert bose.quantity == 5
    assert bose.buy(5) == 5 * 250


# Test that buying a larger quantity than what exists invokes exception
def test_buying_quantity_exceeded():
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    with pytest.raises(ValueError):
        bose.buy(150)
    assert bose.quantity == 10


pytest.main()
