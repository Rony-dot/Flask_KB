from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form_page", methods=['GET', 'POST'])
def form_page_content():
    if request.method == "GET":
        return render_template("forms.html")
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        return f"processing post request, username: {username}, password: {password}"

@app.route("/upload_file", methods=['POST'])
def handle_file():
    file = request.files['file']
    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()
    else:
        return "unknown file type found"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)