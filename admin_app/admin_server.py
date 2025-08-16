from flask import Flask, render_template, session, request, redirect, url_for
from datetime import datetime
import psycopg
import dotenv
from os import environ
import bcrypt
from secrets import token_urlsafe

dotenv.load_dotenv(dotenv_path="secrets.env")
app = Flask(__name__)
app.secret_key = environ.get("session_secret_key")

# Define main page route
@app.route("/")
def dashboard():
  if 'token' in session.keys() and isLoggedIn(session['token']):
    # return render_template("dashboard.html", logs=get_logs(20))
    return "successfully logged in"
  else:
    return redirect(url_for('login'))

@app.route("/login", methods={'GET','POST'})
def login():
  error = None
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    ip_address = request.remote_addr

    # Check password
    connection = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('admin_db_user')} password={environ.get('admin_db_password')} host={environ.get('db_host')}")
    cursor = connection.cursor()
    cursor.execute("SELECT hash FROM users WHERE username=%s;",[username])
    
    # If password vaild, assign new session token
    if not (password is None) and bcrypt.checkpw(password=password.encode(),hashed_password=cursor.fetchone()[0].encode()):
      token = token_urlsafe(32)
      session['token'] = token
      cursor.execute("""
        INSERT INTO sessions (user_id, ip_address, session_id)
        VALUES ((SELECT user_id FROM users WHERE username = %s),%s,%s)
        ON CONFLICT (user_id, ip_address)
        DO UPDATE SET session_id = EXCLUDED.session_id;
        """, (username, ip_address, token))
      connection.commit()
      connection.close()
      return redirect(url_for('dashboard'))
    else:
      error = 'Invalid username or password.'
    cursor.close()
  return render_template('login.html', error=error)

def isLoggedIn(token):
  "Returns true when user has a valid session_token"
  connection = psycopg.connect(f"dbname={environ.get('db_name')} user={environ.get('admin_db_user')} password={environ.get('admin_db_password')} host={environ.get('db_host')}")
  cursor = connection.cursor()
  cursor.execute("SELECT 1 FROM sessions WHERE session_id = %s",[token])
  return bool(cursor.fetchone())
if __name__ == "__main__":
  app.run(host="0.0.0.0",port=4000)