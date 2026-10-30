from flask import Flask, render_template

# Instantiate Flask web app object
app = Flask(__name__)

# ------------------------------------------------------------------------------
# ROUTE DEFINITIONS
# ------------------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# ------------------------------------------------------------------------------
# SERVER RUNTIME / ENTRY POINT
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(port=5001, debug=True)