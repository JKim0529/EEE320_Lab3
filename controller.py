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
        pass

    def done(self):
        rc = RestaurantController(self.view, self.restaurant)
        self.view.set_controller(rc)
        self.view.create_restaurant_ui()


class OrderController(Controller):
    pass
