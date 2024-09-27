from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.utils.dates import days_ago

# DAG Tanımı
dag = DAG(
    'ssh_to_ubuntu',
    description='SSH ile Ubuntu containerında komut çalıştırma',
    schedule_interval=None,  # Çalışma zamanlaması (None ise manuel çalışır)
    start_date=days_ago(1),
    catchup=False,
)

# SSHOperator Kullanarak Komut Çalıştırma
# makineye aşağıdaki komutlar yüklü olmak zorunda dır
# apt-get update && apt-get install -y openssh-server
# service ssh start
# adduser airflow
# passwd airflow


ssh_task = SSHOperator(
    task_id='run_ls_command',
    ssh_conn_id='ubuntu_ssh',  # Airflow Connection ID (önceki adımda tanımlanan)
    command='ls > deneme.txt',  # Ubuntu container'ında çalışacak komut
    dag=dag,
)

# DAG'daki Task'ı Tanımlama
ssh_task
