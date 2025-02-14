import random

def order_summery(*args,**kwargs):
    if not args:
        print("Error: No order made")

    print("Ordered Items:")
    for item in args:
        print(f"- {item}")
    print()

    table_number = kwargs.get("table_number", random.randint(1,20))
    print("Customer Details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

    if "table_number" not in kwargs.keys():
        print(f"Table Number (Random): {table_number}")
    print("-"*50)
order_summery("Cheeseburger","Small Salad", "Spaghetti Carbonara", "Mineral Water", "Orange Juice", customer_name= "Sarah", table_number=12, special_request = "Gluten Free Spaghetti")


order_summery("Shrimp Salad","Onion Quiche", "Risotto", "Diet Coke", "Carlsberg", customer_name= "Bob", special_request = "Extra sauce for risotto")

order_summery(customer_name = "Eyal", table_number=4)
