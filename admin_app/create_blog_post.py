import datetime
import psycopg
import dotenv
from os import environ
from datetime import datetime, timezone

dotenv.load_dotenv(dotenv_path="secrets.env")

def create_post(title, author, excerpt, content, timestamp=datetime.now()):
  """
  Attempts to create blog post
  Accepts:
    title: String
    author: String
    excerpt: String
    content: String
    timestamp: datetime object
  Returns:
    Boolean: True if blog post created successfully, false if creation attempt failed.
  """
  # Connect to DB
  connection = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('admin_db_user')} password={environ.get('admin_db_password')} host={environ.get('db_host')}")
  try:
    cursor = connection.cursor()

    # Insert blog data
    cursor.execute('''
    INSERT INTO posts (title, author, excerpt, content, date)
    VALUES (%s, %s, %s, %s, %s);
    ''', (title, author, excerpt, content, timestamp.strftime('%Y-%m-%d %H:%M:%S.%f%z')))
    connection.commit()
  except Exception as e:
    print(e)
    return False
  finally:
    connection.close()
  return True

if __name__ == "__main__":
  # Get blog data
  temp = input("Input date in ISO format, or enter for today: ")
  if len(temp) < 1:
    date = datetime.today()
  else:
    date = datetime.fromisoformat(temp)
  title = input("Input Title: ")
  temp = input("Enter Author, or enter for Liam Callahan: ")
  if len(temp) < 1:
    author = "Liam Callahan"
  else:
    author = temp
  content = input("Enter content: ")
  temp = input("Enter excerpt, or enter for auto excerpt: ")
  if len(temp) < 1:
    excerpt = content.split(".")[0]+"..."
  else:
    excerpt = temp

  # Attempt le thing
  attempt = create_post(title, author, excerpt, content, date)
  if attempt:
    print("Successfully Created Post")
  else:
    print("Attempt Failed")
