class Pizza:
    def __init__(self, name, size, size_price, topping_names, num_toppings, shape, crust):
        self.__name = name
        self.__size = size
        self.__size_price = size_price
        self.__topping_names = topping_names
        self.__num_toppings = num_toppings
        self.__shape = shape
        self.__crust = crust

    def set_name(self, name):
        self.__name = name

    def set_size(self, size):
        self.__size = size

    def set_size_price(self, size_price):
        self.__size_price = size_price

    def set_topping_names(self, topping_names):
        self.__topping_names = topping_names

    def set_num_toppings(self, num_toppings):
        self.__num_toppings = num_toppings

    def set_shape(self, shape):
        self.__shape = shape

    def set_crust(self, crust):
        self.__crust = crust

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_size_price(self):
        return self.__size_price

    def get_topping_names(self):
        return self.__topping_names

    def get_num_toppings(self):
        return self.__num_toppings

    def get_shape(self):
        return self.__shape

    def get_crust(self):
        return self.__crust
