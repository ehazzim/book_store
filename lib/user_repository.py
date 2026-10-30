from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users ORDER BY id;")
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["password"])
            users.append(item)
        return users

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s);",
            [user.username, user.password]
        )
        return None

    def find_by_username(self, username):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE username = %s;", [username]
        )
        if not rows:
            return None
        row = rows[0]
        return User(row["id"], row["username"], row["password"])