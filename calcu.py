from flask import Flask ,jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hey"

@app.route("/cal",methods=["GET"])
def math_operators():
    operation= request.json["operation"]
    number1= request.json["number1"]
    number2=request.json["number2"]
    
    if operation == "add":
        result = int(number1)+int(number2)
    elif operation == "multiply":
        result =int(number1)*int(number2)
    elif operation == "divide":
        result = int(number1)/int(number2)
    else :
        result = int(number1)-int(number2)
    return jsonify(result)
    

if __name__ == "__main__":
    app.run()