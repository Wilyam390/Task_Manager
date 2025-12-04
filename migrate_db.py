"""
Migration script to add users table and update tasks table with user_id column.
This will backup the old database and create the new schema.
"""
import sqlite3
import shutil
from datetime import datetime
from database import init_database, Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def migrate_sqlite():
    """Migrate SQLite database to new schema with users table"""
    db_path = Config.SQLITE_DATABASE
    
    # Backup existing database
    backup_path = f"{db_path}.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    try:
        shutil.copy2(db_path, backup_path)
        logger.info(f"Database backed up to {backup_path}")
    except FileNotFoundError:
        logger.info("No existing database found, creating new one")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Check if users table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        if not cursor.fetchone():
            logger.info("Creating users table...")
            cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(80) UNIQUE NOT NULL,
                    email VARCHAR(120) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)
            logger.info("Users table created successfully")
        else:
            logger.info("Users table already exists")
        
        # Check if tasks table has user_id column
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tasks'")
        tasks_exists = cursor.fetchone()
        
        task_count = 0
        if tasks_exists:
            cursor.execute("PRAGMA table_info(tasks)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if 'user_id' not in columns:
                logger.info("Adding user_id column to tasks table...")
                
                # Check if there are existing tasks
                cursor.execute("SELECT COUNT(*) FROM tasks")
                task_count = cursor.fetchone()[0]
                
                if task_count > 0:
                    logger.warning(f"Found {task_count} existing tasks. Creating default user...")
                    
                    # Create a default user for existing tasks
                    from werkzeug.security import generate_password_hash
                    default_password = generate_password_hash("password123")
                    
                    cursor.execute("""
                        INSERT INTO users (username, email, password_hash)
                        VALUES (?, ?, ?)
                    """, ("admin", "admin@taskmanager.local", default_password))
                    
                    default_user_id = cursor.lastrowid
                    logger.info(f"Default user created (username: admin, password: password123)")
                    
                    # Add user_id column with default value
                    cursor.execute(f"ALTER TABLE tasks ADD COLUMN user_id INTEGER DEFAULT {default_user_id}")
                    
                    # Update existing tasks to belong to default user
                    cursor.execute(f"UPDATE tasks SET user_id = {default_user_id}")
                    
                    logger.info(f"Updated {task_count} existing tasks to belong to default user")
                else:
                    # No existing tasks, just add the column
                    cursor.execute("ALTER TABLE tasks ADD COLUMN user_id INTEGER")
                    logger.info("Added user_id column to empty tasks table")
            else:
                logger.info("Tasks table already has user_id column")
        else:
            logger.info("Tasks table doesn't exist yet, creating from schema...")
            # Read and execute schema.sql
            with open('schema.sql', 'r') as f:
                conn.executescript(f.read())
            logger.info("Database schema created from schema.sql")
        
        conn.commit()
        logger.info("Migration completed successfully!")
        
        if task_count > 0:
            print("\n" + "="*60)
            print("IMPORTANT: Default user created for existing tasks")
            print("Username: admin")
            print("Password: password123")
            print("Please change this password after first login!")
            print("="*60 + "\n")
        
    except Exception as e:
        logger.error(f"Migration failed: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    logger.info("Starting database migration...")
    
    if Config.DB_TYPE == 'sqlite':
        migrate_sqlite()
    elif Config.DB_TYPE == 'azure_sql':
        logger.info("For Azure SQL, run init_azure_db.py to create the new schema")
    else:
        logger.error(f"Unknown database type: {Config.DB_TYPE}")
    
    logger.info("Migration process complete!")
