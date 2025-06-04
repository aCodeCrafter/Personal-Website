CREATE USER frontend WITH PASSWORD --[INSERT PASSWORD HERE];
CREATE USER admin_panel WITH PASSWORD --[INSERT PASSWORD HERE];

-- Create DB & tables
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    author VARCHAR(255),
    excerpt VARCHAR(255),
    content TEXT
    );
CREATE TABLE IF NOT EXISTS logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    level VARCHAR(10),              -- e.g. INFO, ERROR, DEBUG
    source VARCHAR(100),            -- e.g. "auth", "api", "db"
    message TEXT                  -- the actual log message
);
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    creation_timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    role VARCHAR(10),              -- user role, e.g. admin
    username VARCHAR(100),         -- username
    hash TEXT             -- password hash
);
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
    ip_address TEXT NOT NULL
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMPTZ DEFAULT (CURRENT_TIMESTAMP + interval '7 days')
);
-- Grant Permissions
GRANT INSERT ON logs TO frontend;
GRANT SELECT ON posts TO frontend;

GRANT SELECT, INSERT, DELETE ON logs TO admin_panel;
GRANT USAGE, UPDATE ON SEQUENCE posts_id_seq TO admin_panel;
GRANT SELECT, INSERT, UPDATE, DELETE ON posts, users, sessions TO admin_panel;

-- Create indexes for query speed 
CREATE INDEX ON logs (timestamp);
CREATE INDEX ON logs (level);
CREATE INDEX ON logs (source);
