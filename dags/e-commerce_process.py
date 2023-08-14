#  create an automated workflow for processing e-commerce orders.
from airflow.decorators import dag, task
import pendulum

from mock_data_order import generate_mock_order
# from airflow.operators.dummy_operator import DummyOperator 
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['rishi.shrestha101@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

@dag(
    dag_id='e_commerce_orderprocess',
    schedule_interval=None,
    start_date=pendulum.datetime(2023, 8, 8),
    catchup=False,
    default_args=default_args,
    description='Trying to figure out ways to get data. ',
    tags=['dummy', 'test'],
)
def ecommeres():

    @task
    def get_mock():
        mock_data = generate_mock_order()
        return mock_data

    @task
    def check_status(product, quantity, **kwargs):
        name = product
        hook = SqliteHook(sqlite_conn_id="inventory")
        query = f"SELECT quantity from inventory WHERE book_title = '{name}'"
        available_quantity = hook.get_pandas_df(query).iloc[0][0]
        if quantity <= available_quantity:
            status = True
        else:
            print("Limited available on stock.")
            status = False
        return status

    @task
    def shipping(status, **kwargs):
        if status:
            print('Your item is ready for shipping.')
        else:
            print("It's not available.")

    # Define a placeholder task to indicate the start of the workflow
    # start_task = DummyOperator(task_id="start_task")

    # Define the main tasks
    mock_data = get_mock()
    status = check_status(mock_data['product'], mock_data['quantity'])
    ship = shipping(status)

    # Set task dependencies
    mock_data >> status >> ship

ecommeres()