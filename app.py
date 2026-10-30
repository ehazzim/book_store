from flask import Flask, render_template
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository

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

# /team
@app.route("/team", methods=["GET"])
def get_team():
    return render_template("team.html")

# ------------------------------------------------------------------------------
# SERVER RUNTIME / ENTRY POINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)