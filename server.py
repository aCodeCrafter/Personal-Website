from flask import Flask, render_template
import sqlite3

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


# TODO ADD /rss endpoint

# Return dict containing blog post metadata and content. If entry is not found,
# return a dict with the same structure, but populated with None type
# @app.route("/blog-json-<id>")
# def getBlogPost(id):
#   #Open DB
#   c = sqlite3.connect('webdata.db') 

#   #Query database for post with id
#   cursor = c.cursor()
#   cursor.execute('SELECT * FROM blog WHERE id = ?',id) 
#   output = cursor.fetchone()
#   c.close() 
#   if (output is None):
#     return {
#       "id":None,
#       "date":None,
#       "title":None,
#       "author":None,
#       "content":None}
#   else:
#     return {
#       "id":output[0],
#       "date":output[1],
#       "title":output[2],
#       "author":output[3],
#       "content":output[4]}

# Return dict for multiple blog posts titles, authors, and excerpts
def getBlogArchives(page, numPerPage):
  assert isinstance(page, int)
  assert isinstance(numPerPage, int)

  #Open DB
  c = sqlite3.connect('webdata.db') 

  #Query database for post with id
  cursor = c.cursor()
  cursor.execute('SELECT id, date, title, author, excerpt FROM blog WHERE id < ? AND id >= ?',[page*numPerPage,(page-1)*numPerPage]) 
  result = cursor.fetchall()
  c.commit()
  c.close() 

  # Format results from sql
  output = []
  for row in result:
    if not row is None:
      output.append({
        "id":row[0],
        "date":row[1],
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
        "date":result[1],
        "title":result[2],
        "author":result[3],
        "content":result[4]}