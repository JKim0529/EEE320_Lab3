from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        self.menu_items = [MenuItem(item[0], item[1]) for item in MENU_ITEMS]


class Table:

    def __init__(self, seats, location):
        self.n_seats = seats
        self.location = location
        self.orders = [Order() for _ in range(seats)]

    def has_order_for(self, seat):
        return len(self.orders[seat].items) > 0

    def order_for(self, seat):
        return self.orders[seat]


class Order:
    def __init__(self):
        self.order_items = [OrderItem(MenuItem(item[0], item[1])) for item in MENU_ITEMS]
        self.items = []

    def add_item(self, item):
        self.items.append(OrderItem(item))

    def unordered_items(self):
        return [item for item in self.order_items if not item.ordered]

    def place_new_orders(self):
        for item in self.items:
            item.mark_as_ordered()

    def remove_unordered_items(self):
        for item in self.items:
            if not item.ordered:
                self.items.remove(item)

    def total_cost(self):
        return sum([item.details.price for item in self.items])

class OrderItem:
    def __init__(self, menu_item):
        self.details = menu_item
        self.ordered = False

    def mark_as_ordered(self):
        self.ordered = True


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
