from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    return "hello world!!!"

@app.route('/suma', methods=['GET'])
def suma():
    num1 = request.args.get('a')
    print(num1)
    num2 = request.args.get('b')
    print(num2)
    
    suma =int(num1) + int(num2)

    return f"la suma de {num1} + {num2} es = {num1 + num2}"


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="10050")


