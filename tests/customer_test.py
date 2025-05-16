from customer import Customer
from coffee import Coffee

def test_customer_name_validation():
    try:
        Customer("A" * 20)
        assert False, "Should raise ValueError"
    except ValueError:
        assert True

def test_customer_coffees_unique():
    c = Customer("Alice")
    coffee = Coffee("Espresso")
    c.create_order(coffee, 5.0)
    c.create_order(coffee, 6.0)
    assert len(c.coffees()) == 1
