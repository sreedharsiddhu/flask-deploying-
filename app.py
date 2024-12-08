from flask import Flask, render_template

app = Flask(__name__)  # Create the Flask app instance



@app.route("/data")
def carrers():
     return render_template("data.html")
@app.route("/contact")
def contacts():
    return "Welcome to my world!. hello hj hi da "

if __name__ == "__main__":
    app.run(debug=True)  # Debug mode for development