from email.utils import quote
from products import *
from products_handle import *

if __name__ == "__main__":
    try:
        q = QueryHandler("127.0.0.1", "sqlassignment", "root", "")
        p1 = products("13f45ghtd4", "p11", 35)
        p2 = products("9fktjrne7g", "p22", 54)
        p3 = products("1fsc378623", "p33", 25)
        p4 = products("3453fsc942", "p44", 15)
        # PRINTING products information
        print(p1.__str__())
        # Showing all products
        show_all_products(q)
        # adding products to the database
        adding_product(p1, q)
        adding_product(p2, q)
        adding_product(p3, q)
        adding_product(p4, q)
        adding_product(p1, q)
        
        # Showing all products
        show_all_products(q)
        # deleting products
        delete_product(p3.barcode, q)
        # Showing all products
        show_all_products(q)
        # Activating the code
        start_Code(q)
    except ValueError as v:
        print(v)
        # Activating the code after printing the error
        start_Code(q)
    except TypeError as t:
        print(t)
        start_Code(q)