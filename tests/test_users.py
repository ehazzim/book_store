from lib.user import User
from lib.user_repository import UserRepository

"""
When we call #all on UserRepository, we get a list of all users
"""
def test_all_users(db_connection):
    repository = UserRepository(db_connection)
    users = repository.all()

    assert users == [
        User(1, 'cyber_reader', 'matrix_pass123')
    ]

"""
When we call #create on UserRepository, a new user is saved to the database
"""
def test_create_user(db_connection):
    repository = UserRepository(db_connection)
    new_user = User(None, 'neon_rider', 'cyberpunk2077')
    repository.create(new_user)

    assert repository.find_by_username('neon_rider') == User(2, 'neon_rider', 'cyberpunk2077')