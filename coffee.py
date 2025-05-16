class Coffee:
    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        self._orders = []

    @property
    def name(self):
        return self._name

    def orders(self):
        return self._orders.copy()

    def customers(self):
        return list({order.customer for order in self._orders})
