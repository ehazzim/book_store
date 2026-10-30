import pytest
from lib.database_connection import DatabaseConnection

@pytest.fixture
def db_connection():
    connection = DatabaseConnection()
    # Connect explicitly to your TEST database so production data isn't wiped!
    connection.DATABASE_NAME = "book_store_test"
    connection.connect()
    
    # Automatically reset the test DB schema and sample records before running the test
    connection.seed("seeds/book_store.sql")
    
    return connection