from flask import Flask  

app = Flask(__name__)  # Create the Flask app instance

@app.route("/home")
def welcome():
    return "Welcome to my world!.welcome to home page "

@app.route("/carrers")
def carrers():
    return "Welcome to job fair "

@app.route("/contact")
def contacts():
    return "Welcome to my world!. hello hj hi da "

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development
