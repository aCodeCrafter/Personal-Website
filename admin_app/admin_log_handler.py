from os import environ
import dotenv
import psycopg

dotenv.load_dotenv(dotenv_path="secrets.env")

def get_recent_logs(max_logs):
  """
  Returns the n most recent logs 
  """
  connection = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('admin_db_user')} password={environ.get('admin_db_password')} host={environ.get('db_host')}")
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM logs LIMIT %s",[max_logs])
  return cursor.fetchall()

