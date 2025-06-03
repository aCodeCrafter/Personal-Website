See also [Website Design thought process](Website_Design_thought_process), and [Canvas](Website%20Design.canvas)
### Dependancies
PostgreSQL
gunicorn
nginx
Flask
psycopg
dotenv
### PostgreSQL
##### Setup
1. In terminal open postgres user: 
	`sudo -u postgres psql`
2. Create superuser for DB management:
```
CREATE USER [current user];
ALTER USER [current user] WITH SUPER USER;
CREATE DATABASE WEBSITE_DB OWNER [current user];
```
3. Update passwords in setup.sql
4. cd to Personal-Website
5. Run `psql -d website_db -f setup.sql`

Tables:
	Posts
	Users
	Logs
Posts	
```
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    author VARCHAR(255),
    excerpt VARCHAR(255),
    content TEXT
    );
```    
Users
```
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    creation_timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(10),              -- user role, e.g. admin
    username VARCHAR(100),         -- username
    hash VARCHAR(100)             -- password hash
);
```
Logs
```
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(10),              -- e.g. INFO, ERROR, DEBUG
    source VARCHAR(100),            -- e.g. "auth", "api", "db"
    message TEXT                  -- the actual log message
);
```
