import sqlite3
from datetime import datetime, timedelta

# Connect to an SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('webdata.db')

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Create table
cursor.execute('''DROP TABLE blog;''')
cursor.execute('''CREATE TABLE IF NOT EXISTS blog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATETIME DEFAULT CURRENT_TIMESTAMP,
                    title varchar(255),
                    author varchar(255),
                    excerpt varchar(255),
                    content LONGTEXT)''')


# Insert TEST data
# date = datetime(2025,1,1)
# td = timedelta(days=1)
# for i in range(40):
#   date += td
#   cursor.execute(f'''INSERT INTO blog (date, title, author, excerpt, content) VALUES ("{date}", "Test Blog {i}", "Liam Callahan", "Excerpt #{i}", "Now here is the content, probably stored in html")''')

connection.commit()

connection.close()
