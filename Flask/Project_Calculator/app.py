from flask import Flask, jsonify, render_template, request

app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/math",methods=["POST"])
def math_operations():
    if (request.method=='POST'):
        op=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if (op=="add"):
            r=num1+num2
            result= "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="subtract"):
            r=num1-num2
            result= "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="multiply"):
            r=num1*num2
            result= "The multiplication of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="divide"):
            r=num1/num2
            result= "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)
        return render_template("results.html",result=result)



@app.route("/postman",methods=["POST"])
def math_operations_2():
    if (request.method=='POST'):
        op=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if (op=="add"):
            r=num1+num2
            result= "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="subtract"):
            r=num1-num2
            result= "The difference of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="multiply"):
            r=num1*num2
            result= "The multiplication of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if (op=="divide"):
            r=num1/num2
            result= "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)
        return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")