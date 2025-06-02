from flask import Flask, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Define main page route
@app.route("/")
def main_page():
  return render_template("dashboard.html")

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000)