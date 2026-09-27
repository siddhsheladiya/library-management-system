import mysql.connector

def get_connection():
    """Establishes and returns a connection to the MySQL database."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password_here",  # Replace with your MySQL root password
        database="project1"
    )