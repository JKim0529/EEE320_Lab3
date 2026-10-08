from constants import *

class Controller:
    """
    Do not modify this class, just its subclasses. Represents common behaviour of all
    Controllers. Python has a mechanism for explicitly dealing with abstract classes,
    which we haven't seen yet; raising RuntimeError gives a similar effect.
    """

    def __init__(self, view, restaurant):
        self.view = view
        self.restaurant = restaurant

    def add_item(self, item):
        raise RuntimeError('add_item: some subclasses must implement')

    def cancel(self):
        raise RuntimeError('cancel: some subclasses must implement')

    def create_ui(self):
        raise RuntimeError('create_ui: all subclasses must implement')

    def done(self):
        raise RuntimeError('done: some subclasses must implement')

    def place_order(self):
        raise RuntimeError('place_order: some subclasses must implement')

    def seat_touched(self, seat_number):
        raise RuntimeError('seat_touched: some subclasses must implement')

    def table_touched(self, table_index):
        raise RuntimeError('table_touched: some subclasses must implement')


class RestaurantController(Controller):

    def __init__(self, view, restaurant):
        super().__init__(view, restaurant)

    def create_ui(self):
        self.view.create_restaurant_ui()


    def table_touched(self, table_index):
        table = self.restaurant.tables[table_index]
        # Table controller object
        tc = TableController(self.view, self.restaurant, table)
        self.view.set_controller(tc)

        self.view.create_table_ui(table)



class TableController(Controller):
    def __init__(self, view, restaurant, table):
        super().__init__(view, restaurant)
        self.table = table

    def create_ui(self):
        pass

    def seat_touched(self, seat_number):
        self.view.set_controller(
        OrderController(self.view, self.restaurant, self.table, seat_number))

    def done(self):
        rc = RestaurantController(self.view, self.restaurant)
        self.view.set_controller(rc)
        self.view.create_restaurant_ui()


class OrderController(Controller):
    def __init__(self, view, restaurant, table, seat_number):
        super().__init__(view, restaurant)
        self.table = table
        self.seat_number = seat_number
        self.order = table.order_for(seat_number)

    def create_ui(self):
        self.view.create_order_ui(self.order)

    def add_item(self, menu_item):
        self.order.add_item(menu_item)
        # Redraw the order view so the new item shows up
        self.view.create_order_ui(self.order)

    def update_order(self):
        self.order.place_new_orders()
        self._return_to_table_view()

    def cancel(self):
        self.order.remove_unordered_items()
        self._return_to_table_view()
