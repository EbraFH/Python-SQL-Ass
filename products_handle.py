from products import *
from query_handler import *


def adding_product(product: products, query: QueryHandler):
    """
    function that adds or updates a product if it already exists in the database
    """
    query.execute_non_fetch(
        "INSERT INTO products (barcode,products_name,quantity) VALUES(%s,%s,%s) ON DUPLICATE KEY UPDATE barcode=VALUES(barcode), products_name=VALUES(products_name),quantity=VALUES(quantity)",
        (product.barcode, product.product_name, product.quantity))
    print("insert done")


def delete_product(barcode: str, query: QueryHandler):
    """
    function that deletes a product in the database according to the given barcode
    :param barcode: products barcode (special code)
    """
    products = query.execute_fetch("SELECT * FROM products WHERE barcode=%s", (barcode,))
    if len(products) != 0:
        query.execute_non_fetch("DELETE FROM products WHERE barcode=%s", (barcode,))
        print("delete done")
    else:
        print("Barcode doesn't exist")


def show_all_products(query: QueryHandler):
    """
    fucntion that prints the products table in the database
    """
    # print(query.execute_fetch("SELECT * FROM products", ()))
    products = query.execute_fetch("SELECT * FROM products", ())
    for item in products:
        for k,v in item.items():
            print(k,":",v)
        print()

def start_Code(q):
    """
    Function that either insert/update/delete or print products according to users input
    if user clicks 1 it inserts or updates the databse
    if user clicks 2 it deletes a product from database
    if user clicks 3 it prints all the table in the database
    if user clicks 4 it exists the code
    """
    while True:
        option = input("""enter your choice: 
                    Number 1: To insert or update a product.
                    Number 2: To delete a product.
                    Number 3: To print all the products
                    Number 4: To exit
                    my choice: 
                    """)

        if option == "1":
            print("please enter product details,, ")
            product = products(input("product barcode: "), input("product name: "),
                               int(input("product quantity: ")))
            adding_product(product, q)
        elif option == "2":
            print("please enter product barcode,, ")
            barcode = input("product barcode: ")
            delete_product(barcode, q)
        elif option == "3":
            show_all_products(q)
        elif option == "4":
            print("Thank you for using our program. Exiting...")
            break
        else:
            print("please enter only one option for the list [1,2,3,4]")
