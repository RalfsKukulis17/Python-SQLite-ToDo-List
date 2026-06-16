import sqlite3
from datetime import datetime

DB_NAME = "todo.db"

def create_tasks_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                deadline TEXT NOT NULL,
                is_done INTEGER DEFAULT 0,
                created_at TEXT NOT NULL,
                completed_at TEXT
        )
    """)

    connection.commit()
    connection.close()

def add_task(title, deadline):
    created_at = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, deadline, created_at)
        VALUES (?, ?, ?)
        """, (title, deadline, created_at))
    
    connection.commit()
    connection.close()