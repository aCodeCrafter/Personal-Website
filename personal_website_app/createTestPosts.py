import psycopg
import dotenv
from os import environ
from datetime import datetime, timedelta

dotenv.load_dotenv(dotenv_path="secrets.env")

# Connect to an SQLite database (or create it if it doesn't exist)
connection = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('admin_db_user')} password={environ.get('admin_db_password')} host={environ.get('db_host')}")

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Insert TEST data
date = datetime(2025,1,1)
td = timedelta(days=1)
for i in range(40):
  date += td
  cursor.execute(f'''
  INSERT INTO posts (title, author, excerpt, content)
  VALUES ('Post {i}', 'Liam Callahan', 'Really cool exerpt', 'Some amazing content');''')

connection.commit()

connection.close()
