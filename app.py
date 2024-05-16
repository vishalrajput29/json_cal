from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Home Page "

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/success/<int:score>")
def success(score):
    return "The person is pass and the scoe is " +str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person is pass and the scoe is " +str(score)

@app.route("/calculate",methods=["GET","POST"])
def calculate():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        maths = float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
        average_marks = (maths+science+history)/3
        result = ""
        if average_marks >=50:
            result= "success"
        else:
            result="fail"
        
        return redirect(url_for(result,score=average_marks))

            

if __name__ == "__main__":
    app.run()