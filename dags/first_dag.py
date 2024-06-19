

from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

dag = DAG(
    'first_dag',
    default_args=default_args,
    description='A simple email DAG',
    schedule_interval='24 5 * * *',
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

send_email = EmailOperator(
    task_id='send_email',
    to='manishakhadka@peakvoyage.com',
    subject='Airflow Email Test',
    html_content='Good morning didi. I hope u are doing well',
    dag=dag,
)

start >> send_email





# # ====================================Notes====================================

# # all_success           -> triggers when all tasks arecomplete
# # one_success           -> trigger when one task is complete
# # all_done              -> Trigger when all Tasks are Done
# # all_failed            -> Trigger when all task Failed
# # one_failed            -> one task is failed
# # none_failed           -> No Task Failed

# # ==============================================================================



# # ============================== Executor====================================

# # There are Three main  types of executor
# # -> Sequential Executor  run single task in linear fashion wih no parllelism default Dev
# # -> Local Exector  run each task in seperate process
# # -> Celery Executor Run each worker node within multi node architecture Most scalable

# # ===========================================================================