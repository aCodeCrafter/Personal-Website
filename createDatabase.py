import sqlite3

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
for i in range(40):
  cursor.execute(f'''INSERT INTO blog (title, author, excerpt, content) VALUES ("Test Blog {i}", "Liam Callahan", "Excerpt #{i}", "Now here is the content, probably stored in html")''')

connection.commit()

connection.close()
