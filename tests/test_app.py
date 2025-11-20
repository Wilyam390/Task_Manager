import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, tasks, next_id

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        original_tasks = tasks.copy()

        tasks.clear()
        tasks.append({
            'id': 1,
            'title': 'Test Task',
            'description': 'This is a test task',
            'completed': False,
            'created_at': '2025-11-20 10:00'
        })
        yield client

        tasks.clear()
        tasks.extend(original_tasks)

def test_home_page(client):
    """Test that the home page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Task Manager' in response.data
    assert b'Your personal task tracking application' in response.data

def test_home_displays_tasks(client):
    """Test that the home page displays existing tasks."""
    response = client.get('/')
    assert b'Test Task' in response.data
    assert b'This is a test task' in response.data

def test_add_task_success(client):
    """Test adding a new task successfully."""
    response = client.post('/task/add', data={
        'title': 'New Task',
        'description': 'New task description'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'New Task' in response.data
    assert b'Task created successfully' in response.data

def test_add_task_title_too_long(client):
    """Test that title over 255 characters is rejected"""
    long_title = 'a' * 300
    response = client.post('/task/add', data={
        'title': long_title,
        'description': 'Test'
    }, follow_redirects=True)
    
    assert b'too long' in response.data.lower()

def test_toggle_task_completion(client):
    """Test toggling task from incomplete to complete"""
    response = client.post('/task/1/toggle', follow_redirects=True)
    assert response.status_code == 200
    assert b'Task status updated' in response.data

def test_toggle_nonexistent_task(client):
    """Test toggling a task that doesn't exist"""
    response = client.post('/task/999/toggle', follow_redirects=True)
    assert b'not found' in response.data.lower()

def test_delete_task_success(client):
    """Test deleting an existing task"""
    response = client.post('/task/1/delete', follow_redirects=True)
    assert response.status_code == 200
    assert b'deleted successfully' in response.data.lower()
    assert b'Test Task' not in response.data or b'No tasks yet' in response.data

def test_delete_nonexistent_task(client):
    """Test deleting a task that doesn't exist"""
    response = client.post('/task/999/delete', follow_redirects=True)
    assert b'not found' in response.data.lower()

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert 'tasks_count' in data
    assert isinstance(data['tasks_count'], int)

def test_task_counter_display(client):
    """Test that task counter shows correct number"""
    response = client.get('/')
    assert b'Your Tasks' in response.data