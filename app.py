<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging
import sys
from datetime import datetime
from config import config, Config
from database import get_db_connection
=======
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, flash
import os
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
<<<<<<< HEAD

# Load configuration
env = Config.ENVIRONMENT
app.config.from_object(config[env])
app.secret_key = app.config['SECRET_KEY']

# Azure Application Insights integration
if app.config.get('APPINSIGHTS_INSTRUMENTATION_KEY'):
    try:
        from opencensus.ext.azure.log_exporter import AzureLogHandler
        from opencensus.ext.azure import metrics_exporter
        from opencensus.ext.flask.flask_middleware import FlaskMiddleware
        
        # Add Azure monitoring
        middleware = FlaskMiddleware(
            app,
            exporter=metrics_exporter.new_metrics_exporter(
                connection_string=f"InstrumentationKey={app.config['APPINSIGHTS_INSTRUMENTATION_KEY']}"
            )
        )
        
        # Add Azure log handler
        azure_handler = AzureLogHandler(
            connection_string=f"InstrumentationKey={app.config['APPINSIGHTS_INSTRUMENTATION_KEY']}"
        )
        logger.addHandler(azure_handler)
        logger.info("Azure Application Insights enabled")
    except ImportError:
        logger.warning("Azure Application Insights packages not installed")
    except Exception as e:
        logger.error(f"Failed to initialize Application Insights: {e}")

logger.info(f"Application started in {env} mode")

=======
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-later')

# Determine which database to use
USE_AZURE_SQL = os.getenv('AZURE_SQL_CONNECTION_STRING') is not None

if USE_AZURE_SQL:
    import pyodbc
    AZURE_SQL_CONNECTION_STRING = os.getenv('AZURE_SQL_CONNECTION_STRING')
else:
    import sqlite3
    DATABASE = 'tasks.db'

def get_db_connection():
    """Create database connection (SQLite or Azure SQL)"""
    if USE_AZURE_SQL:
        conn = pyodbc.connect(AZURE_SQL_CONNECTION_STRING)
    else:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
    return conn
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

@app.route('/')
def home():
    """Display all tasks"""
<<<<<<< HEAD
    try:
        logger.info("Fetching all tasks")
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks ORDER BY created_at DESC').fetchall()
        conn.close()
        logger.info(f"Retrieved {len(tasks)} tasks")
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        flash('Error loading tasks', 'error')
        return render_template('index.html', tasks=[])
=======
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC' if not USE_AZURE_SQL else 'SELECT * FROM tasks ORDER BY created_at DESC')
    tasks = cursor.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

@app.route('/task/add', methods=['POST'])
def add_task():
    """Create a new task"""
    try:
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()

        if not title:
            logger.warning("Task creation attempted without title")
            flash('Task title is required', 'error')
            return redirect(url_for('home'))
        
        if len(title) > 255:
            logger.warning(f"Task title too long: {len(title)} characters")
            flash('Task title too long (max 255 characters)', 'error')
            return redirect(url_for('home'))
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO tasks (title, description) VALUES (?, ?)',
            (title, description)
        )
        conn.commit()
        conn.close()
        
        logger.info(f"Task created: {title}")
        flash('Task created successfully', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        flash('Error creating task', 'error')
        return redirect(url_for('home'))
<<<<<<< HEAD
=======
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if USE_AZURE_SQL:
        cursor.execute(
            'INSERT INTO tasks (title, description, completed, created_at) VALUES (?, ?, 0, GETDATE())',
            (title, description)
        )
    else:
        cursor.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description)
        )
    
    conn.commit()
    conn.close()
    
    flash('Task created successfully', 'success')
    return redirect(url_for('home'))
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

@app.route('/task/<int:task_id>/toggle', methods=['POST'])
def toggle_task(task_id):
    """Toggle task completion status"""
<<<<<<< HEAD
    try:
        conn = get_db_connection()
        task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
        
        if task:
            new_status = 0 if task['completed'] else 1
            conn.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
            conn.commit()
            logger.info(f"Task {task_id} status toggled to {new_status}")
            flash('Task status updated', 'success')
        else:
            logger.warning(f"Task {task_id} not found for toggle")
            flash('Task not found', 'error')
        
        conn.close()
        return redirect(url_for('home'))
    except Exception as e:
        logger.error(f"Error toggling task {task_id}: {e}")
        flash('Error updating task', 'error')
        return redirect(url_for('home'))
=======
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if USE_AZURE_SQL:
        cursor.execute('SELECT completed FROM tasks WHERE id = ?', (task_id,))
    else:
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    
    task = cursor.fetchone()
    
    if task:
        new_status = 0 if task[0 if USE_AZURE_SQL else 3] else 1
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (new_status, task_id))
        conn.commit()
        flash('Task status updated', 'success')
    else:
        flash('Task not found', 'error')
    
    conn.close()
    return redirect(url_for('home'))
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

@app.route('/task/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    """Delete a task"""
<<<<<<< HEAD
    try:
        conn = get_db_connection()
        result = conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        
        if result.rowcount > 0:
            logger.info(f"Task {task_id} deleted")
            flash('Task deleted successfully', 'success')
        else:
            logger.warning(f"Task {task_id} not found for deletion")
            flash('Task not found', 'error')
        
        conn.close()
        return redirect(url_for('home'))
    except Exception as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        flash('Error deleting task', 'error')
        return redirect(url_for('home'))
=======
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    
    flash('Task deleted successfully', 'success')
    return redirect(url_for('home'))
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

@app.route('/health')
def health():
    """Health check endpoint"""
    try:
        conn = get_db_connection()
<<<<<<< HEAD
        count = conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
        conn.close()
        
        response = {
            'status': 'healthy',
            'tasks_count': count,
            'environment': app.config['ENVIRONMENT'],
            'database': app.config['DB_TYPE']
        }
        logger.info("Health check passed")
        return jsonify(response), 200
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    logger.warning(f"404 error: {request.url}")
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"500 error: {error}")
    return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}", exc_info=True)
    return render_template('errors/500.html'), 500

=======
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM tasks')
        count = cursor.fetchone()[0]
        conn.close()
        return {'status': 'healthy', 'tasks_count': count, 'database': 'Azure SQL' if USE_AZURE_SQL else 'SQLite'}, 200
    except Exception as e:
        return {'status': 'unhealthy', 'error': str(e)}, 500
>>>>>>> 97c530a081e03c25087ee48c42c2b4acf2448e82

if __name__ == '__main__':
    logger.info("Starting Flask application")
    port = 8000 if app.config['DEBUG'] else 80
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])