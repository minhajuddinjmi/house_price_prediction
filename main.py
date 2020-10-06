from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'POST':
        CRIM = request.form('CRIM')
        ZN = request.form('ZN')
        INDUS = request.form('INDUS')
        CHAs = request.form('CHAS')
        NOX = request.form('NOX')
        RM = request.form('RM')
        AGE = request.form('AGE')
        DIS = request.form('DIS')
        RAD = request.form('RAD')
        TAX = request.form('TAX')
        PTRATIO = request.form('PTRATIO')
        B = request.form('B')
        LSTAT = request.form('LSTAT')
        print(CRIM)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)