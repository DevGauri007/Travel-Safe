from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/safety")
def safety():
    return render_template("safety.html")


if __name__ == "__main__":
    app.run(debug=True)