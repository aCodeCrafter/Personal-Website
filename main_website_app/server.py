from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Define main page route
@app.route("/")
def main_page():
  return render_template("main.html",posts=getBlogArchives(1,5))

# Define route for blog archive section of website
@app.route("/blog-archive")
@app.route("/blog-archive/page-<page>")
def blog_archive(page=1):
  page = int(page)
  return render_template("blog_archive.html",posts=getBlogArchives(page,10),next=page+1,prev=page-1)

# Define route for blog section of website
@app.route("/blog")
@app.route("/blog/id-<postId>")
def blog_post(postId=1):
  postId = int(postId)
  return render_template("blog.html",post=getBlog(postId))


# Return dict for multiple blog posts titles, authors, and excerpts
def getBlogArchives(page, numPerPage):
  assert isinstance(page, int)
  assert isinstance(numPerPage, int)

  #Open DB
  c = sqlite3.connect('webdata.db') 

  #Query database for post with id
  cursor = c.cursor()
  cursor.execute('''SELECT id, date, title, author, excerpt
                    FROM blog
                    ORDER BY date DESC
                    LIMIT ?
                    OFFSET ?''',
                    [numPerPage, numPerPage*(page-1)]) 
  result = cursor.fetchall()
  c.commit()
  c.close() 

  # Format results from sql
  output = []
  for row in result:
    if not row is None:
      output.append({
        "id":row[0],
        "date":datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S").strftime("%b %d, %Y"),
        "title":row[2],
        "author":row[3],
        "excerpt":row[4]})
  return output

def getBlog(pageId):
  assert isinstance(pageId, int)

  #Open DB
  c = sqlite3.connect('webdata.db') 

  #Query database for post with id
  cursor = c.cursor()
  cursor.execute('SELECT id, date, title, author, content FROM blog WHERE id = ?',[pageId]) 
  result = cursor.fetchone()
  c.commit()
  c.close() 

  # Format results from sql
  return {
        "id":result[0],
        "date":datetime.strptime(result[1], "%Y-%m-%d %H:%M:%S").strftime("%b %d, %Y"),
        "title":result[2],
        "author":result[3],
        "content":result[4]}
if __name__ == "__main__":
  app.run(host="0.0.0.0")