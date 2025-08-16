from os import environ
import psycopg
import dotenv
import bcrypt

# Load secrets from the same secrets.env file
dotenv.load_dotenv(dotenv_path="secrets.env")

def create_user():
    # Get connection info from environment
    db_name = environ.get("db_name")
    db_user = environ.get("admin_db_user")
    db_password = environ.get("admin_db_password")
    db_host = environ.get("db_host")

    # Ask for user details
    username = input("Enter new username: ").strip()
    role = input("Enter role: ").strip()
    password = input("Enter password: ").strip()

    # Hash the password like your Flask app does
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    try:
        # Connect to database
        print(f"dbname={db_name} user={db_user} password={db_password} host={db_host}")
        conn = psycopg.connect(
            f"dbname={db_name} user={db_user} password={db_password} host={db_host}"
        )
        cur = conn.cursor()

        # Insert new user
        cur.execute("""
            INSERT INTO users (username, role, hash)
            VALUES (%s, %s, %s);
        """, (username, role, hashed_pw))

        conn.commit()
        print(f"✅ User '{username}' created successfully.")
    
    except psycopg.Error as e:
        print("Database error:", e)
    
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    create_user()
