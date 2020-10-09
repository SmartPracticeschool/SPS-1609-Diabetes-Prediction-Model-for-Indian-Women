from flask import Flask,render_template,request,redirect,jsonify
import json
import requests
app = Flask(__name__)
s=""
j = {"data":""}
@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "GET":

        return render_template("index.html")
    else:
        
        x=request.form.get("preg")
        s=str(x)
        x=request.form.get("glucose")
        s=s+","+str(x)
        x=request.form.get("bp")
        s=s+","+str(x)
        x=request.form.get("st")
        s=s+","+str(x)
        x=request.form.get("insulin")
        s=s+","+str(x)
        x=request.form.get("bmi")
        s=s+","+str(x)
        x=request.form.get("dpf")
        s=s+","+str(x)
        x=request.form.get("age")
        s=s+","+str(x)
        
      
        
        print(s)
        j={"data":s}
        print(type(j))
        print(j)
        
        
        j = json.dumps(j, indent = 4)
        r = requests.post(
            'https://g364vkf5me.execute-api.us-east-1.amazonaws.com/final',
            data=j)
        if r.text == '1':
            res = "Yes,the person is diabetic"
        else:
            res = "No,the person is not diabetic"
        print(r.text)
        return render_template("result.html",res=res)
        


if __name__ == '__main__':
    app.run(debug=True)
