CREATE TABLE IF NOT EXISTS html_etuovi (
 id INTEGER PRIMARY KEY,
 timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
 html TEXT NOT NULL
);