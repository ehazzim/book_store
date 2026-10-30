from flask import Flask, render_template, request, redirect, url_for
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.user import User
from lib.user_repository import UserRepository

# Instantiate Flask web app object
app = Flask(__name__)

# ------------------------------------------------------------------------------
# ROUTE DEFINITIONS
# ------------------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# /books
@app.route("/books", methods=["GET"])
def get_books():
    connection = DatabaseConnection()
    connection.connect()

    repository = BookRepository(connection)
    books = repository.all()
    
    return render_template("books.html", books=books)

# /quotes
@app.route("/quotes", methods=["GET"])
def get_quotes():
    return render_template("quotes.html")

# /signup
@app.route("/signup", methods=["GET"])
def get_signup():
    return render_template("signup_form.html")

@app.route("/signup", methods=["POST"])
def post_signup():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return render_template("signup_form.html", error="Username and password are required."), 400

    connection = DatabaseConnection()
    connection.connect()
    
    repository = UserRepository(connection)

    # Check if username is already taken
    existing_user = repository.find_by_username(username)
    if existing_user:
        return render_template("signup_form.html", error="Username already registered."), 400

    # Create and persist new user
    new_user = User(None, username, password)
    repository.create(new_user)

    return redirect(url_for("index"))

# /team
@app.route("/team", methods=["GET"])
def get_team():
    return render_template("team.html")

# ------------------------------------------------------------------------------
# SERVER RUNTIME / ENTRY POINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)