from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
  return render_template("main_page.html")