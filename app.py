from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1><p>Your Flask application is running successfully.</p>"

# Run the application
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)
