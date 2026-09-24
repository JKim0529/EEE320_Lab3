from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        # TODO: uncomment next line
        # self.menu_items = [MenuItem(name, price) for name, price in MENU_ITEMS]


class Table:

    def __init__(self, seats, location):
        self.n_seats = seats
        self.location = location
        # TODO: Uncomment next line
        # self.orders = [Order() for _ in range(seats)]

    def has_order_for(self, seat_index ):
        pass

    def order_for(self, seat_index):
        pass


class Order:
    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]

    def add_item(self, menu_item = MENU_ITEMS):
        pass

    def unordered_items(self):
        pass

    def place_new_orders(self):
        pass

    def remove_unordered_items(self):
        pass

    def total_cost(self):
        pass


class OrderItem:
    pass


class MenuItem:
    pass
