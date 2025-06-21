from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

# url processors
# example: http://127.0.0.1:8080/greet/rakibulH
@app.route('/greet/<name>')
def greet(name):
    return f"<h1>Hello {name}!</h1>"

# example: http://127.0.0.1:8080/add/10/20
# response: 10 + 20 = 1020
@app.route('/add/<number1>/<number2>')
def add(number1, number2):
    return f"<h1>{number1} + {number2} = {number1+number2}</h1>"


# example: http://127.0.0.1:8080/sum/10/20
# response: 10 + 20 = 30
@app.route('/sum/<int:number1>/<int:number2>')
def sum(number1, number2):
    return f"<h1>{number1} + {number2} = {number1+number2}</h1>"


@app.route('/with_return_code')
def with_return_code():
    return "<h1>Hello World!</h1>", 200


@app.route('/handle_http_verbs', methods=['GET','POST'])
def handle_http_verbs():
    if request.method == 'GET':
        return "you made a GET request"
    elif request.method == 'POST':
        return "you made a POST request"
    else:
        return "you will never get here, because this method accpets only GET or POST"



# example: http://127.0.0.1:8080/handle_url_params?greeting=hi&name=rakibul
# response: hi, rakibul
@app.route('/handle_url_params')
def handle_url_params():
    if 'greeting' in request.args and 'name' in request.args:
        print("all params are passed correctly")
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f"<h1>{greeting}, {name}</h1>"


@app.route("/custom_response")
def custom_response():
    response = make_response("hello custom response")
    response.status = 201
    response.content_type = 'application/json' # either this
    response.headers['content-type'] = 'text/plain' # or this
    return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)