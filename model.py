from constants import TABLES, MENU_ITEMS


class Restaurant:

    def __init__(self):
        self.tables = [Table(seats, loc) for seats, loc in TABLES]
        # TODO: uncomment next line
        self.menu_items = [MenuItem(name, price) for name, price in MENU_ITEMS]


class Table:

    def __init__(self, seats, location):
        self.n_seats = seats
        self.location = location
        # TODO: Uncomment next line
        self.orders = [Order() for _ in range(seats)]

    def has_order_for(self, seat):
        pass
        # return len(self.orders[seat].items) > 0

    def order_for(self, seat):
        pass
        # return self.orders[seat]


class Order:
    def __init__(self):
        # self.tables = [Table(seats, loc) for seats, loc in TABLES]
        self.items = []
        self.unrequested = []
        self.unordered_items_lst = []
        self.unordered_items()

    def add_item(self, menu_item):
        self.unrequested.remove(menu_item)
        self.items.append(menu_item)

    def unordered_items(self):
        List1 = []
        for item in MENU_ITEMS:
            menu_item = MenuItem(item.name, item.price)
            self.List1.append(menu_item)
        for menu_item in List1:
            self.unordered_items_lst.append(OrderItem(menu_item))
        return self.unordered_items_lst

    def place_new_orders(self):
        for item in self.items:
            item.mark_as_ordered()
            self.items.append(item)

    def remove_unordered_items(self):
        for item in self.items:
            self.unrequested.append(item)
        self.items = []

    def total_cost(self):
        return sum([item.price for item in self.items])


class OrderItem:
    def __init__(self, menu_item):
        self.menu_item = menu_item
        self.ordered = False

    def mark_as_ordered(self):
        self.ordered = True


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
