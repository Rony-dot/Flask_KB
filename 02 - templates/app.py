from flask import Flask, render_template, redirect, url_for

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
    return render_template("basic_jinja.html", name="rakibul hassan", email="john@gmail.com", numbers=list_of_even_numbers)


@app.template_filter("repeat")
def repeat_value(value, times=2):
    return value*times

@app.route("/redirect")
def redirect_page():
    return redirect(url_for('some_jinja'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)