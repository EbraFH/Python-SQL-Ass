class products:
    """
    a class that defines products information
    """

    def __init__(self, barcode: str, product_name: str, quantity: int):
        """
        Constructor which defines the products info
        :param barcode: displays the products barcode
        :param product_name: displays products name
        :param quantity: displays the amount of a certain product
        """
        self.barcode = barcode
        self.product_name = product_name
        self.quantity = quantity

    @property
    def barcode(self):
        """
        Getter return the products barcode
        :return: products barcode
        """
        return self.__barcode

    @property
    def product_name(self):
        """
        Getter return product name
        :return: product_name
        """
        return self.__product_name

    @property
    def quantity(self):
        """
        Getter return products quantity
        :return: quantity
        """
        return self.__quantity

    @barcode.setter
    def barcode(self, barcode: str):
        """
        Setter which defines the products barcode
        if the string length is 10 chars and only small letters and numbers
        :return: none
        """
        maximum_chars = 10
        if len(barcode) == maximum_chars and barcode.islower() and not barcode.isnumeric():
            self.__barcode = barcode
        else:
            raise TypeError("products barcode  should be numbers with chars")
            raise ValueError("barcodes length should be 10 characters and is made of numbers and lowercase chars")

    @product_name.setter
    def product_name(self, product_name: str):
        """
        Setter which defines the products name
        if the products length is between 3-25
        :return: none
        """
        min_range = 3
        max_range = 25
        if min_range <= len(product_name) <= max_range and not product_name.isnumeric():
            self.__product_name = product_name
        else:
            raise TypeError("products name should not be in numbers")
            raise ValueError("products name length can only be between 3-25")

    @quantity.setter
    def quantity(self, quantity: int):
        """
        Setter which defines products quantity
        iff the quantity is between 0-999
        :return: none
        """
        min_range = 0
        max_range = 999
        if min_range <= quantity <= max_range and isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ValueError("products quantity can only be an integer between 0-999")

    def __str__(self) -> str:
        """
        Method returns a string that displays the product
        :return:
        """
        return f"Product:\n barcode: {self.barcode} \n products name: {self.product_name} \n " \
               f"quantity: {self.quantity}"
