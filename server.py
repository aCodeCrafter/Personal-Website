from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
  return render_template("main.html")

@app.route("/blog")
def blog_page():
  return render_template("blog.html")

# ADD blog-json endpoint
# ADD /rss endpoint
