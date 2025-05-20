from customer import Customer
from coffee import Coffee
from order import Order

# Create a customer named James
james = Customer("James")

# Create some coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# James places an order for a Latte and an Espresso
order1 = james.create_order(latte, 5.0)
order2 = james.create_order(espresso, 3.5)

# Print details of the orders
print(f"Customer: {james.name}")
print(f"Ordered Coffee 1: {order1.coffee.name}, Price: {order1.price}")
print(f"Ordered Coffee 2: {order2.coffee.name}, Price: {order2.price}")

# Check the number of orders for each coffee
print(f"Number of orders for Latte: {latte.num_orders()}")
print(f"Average price for Latte: {latte.average_price()}")