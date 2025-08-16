import sqlite3
from datetime import datetime, timedelta

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


# Connect to an SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('webdata.db')

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Insert blog data
cursor.execute(f'''INSERT INTO blog (date, title, author, excerpt, content) VALUES ("{str(date).split(".")[0]}", "{title}", "{author}", "{excerpt}", "{content}")''')

connection.commit()

connection.close()
