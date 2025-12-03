CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT 0,
    priority VARCHAR(10) NOT NULL DEFAULT 'Medium',
    category VARCHAR(100) DEFAULT 'General',
    due_date DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
