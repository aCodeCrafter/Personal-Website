from flask import Flask, render_template
import psycopg
import dotenv
import markdown
from os import environ
from datetime import datetime

#Load environment variables
dotenv.load_dotenv(dotenv_path="secrets.env")
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
  c = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('frontend_db_user')} password={environ.get('frontend_db_password')} host={environ.get('db_host')}")

  #Query database for post with id
  cursor = c.cursor()
  cursor.execute('''SELECT id, date, title, author, excerpt
                    FROM posts
                    ORDER BY date DESC
                    LIMIT %s
                    OFFSET %s''',
                    (numPerPage, numPerPage*(page-1))) 
  result = cursor.fetchall()
  c.commit()
  c.close() 

  # Format results from sql
  output = []
  for row in result:
    if not row is None:
      output.append({
        "id":row[0],
        "date":row[1].strftime("%b %d, %Y"),
        "title":row[2],
        "author":row[3],
        "excerpt":markdown.markdown(row[4])})
  return output

# Return the contents/metadata for an individual post
def getBlog(pageId):
  assert isinstance(pageId, int)

  #Open DB
  c = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('frontend_db_user')} password={environ.get('frontend_db_password')} host={environ.get('db_host')}")

  #Query database for post with id
  cursor = c.cursor()
  cursor.execute('SELECT id, date, title, author, content FROM posts WHERE id = %s',[pageId]) 
  result = cursor.fetchone()
  c.commit()
  c.close() 

  # Format results from sql
  return {
        "id":result[0],
        "date":result[1].strftime("%b %d, %Y"),
        "title":result[2],
        "author":result[3],
        "content":markdown.markdown(result[4])}
if __name__ == "__main__":
  app.run(host="0.0.0.0")