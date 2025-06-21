from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/jinja")
def some_jinja():
    list_of_even_numbers = [2, 4, 6, 8, 10]
    return render_template("basic_jinja.html", name="rakibulH", email="john@gmail.com", numbers=list_of_even_numbers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)