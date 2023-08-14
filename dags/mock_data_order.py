from faker import Faker
import random
import datetime

fake = Faker()
def generate_mock_order():
    today = datetime.date.today()
    order = {
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "product": fake.random_element(['The Great Gatsby', 'To Kill a Mockingbird', '1984', 'Pride and Prejudice']),
        "quantity": random.randint(1, 10),
        "order_date": today.strftime('%Y-%m-%d'),
    }
    return order
# print(generate_mock_order())
# def check_item(name:str, quantity:int):
#     hook = SqliteHook(sqlite_conn_id="inventory")
#     query = f"SELECT quantity from inventory WHERE book_title = '{name}';"
#     available_quantity = hook.get_pandas_df(query)
#     if available_quantity >= quantity:
#         return True
#     else:
#         return False


# def get_order():
#     order = generate_mock_order()
#     responce = check_item(order['product'], order['quantity'])
#     print(responce)


# get_order()
