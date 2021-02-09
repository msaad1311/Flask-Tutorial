from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def upperLevel(name):
    return any(x.isupper() for x in name)
def lowerLevel(name):
    return any(x.islower() for x in name)
def numberEnd(name):
    return name[-1].isdigit()

@app.route('/report')
def report():
    userName = request.args.get('UserName')
    upper = upperLevel(userName)
    lower = lowerLevel(userName)
    numbr = numberEnd(userName)
    if upper and lower and numbr:
        result = True
    else:
        result=False
    return render_template('report.html',result=result,upper=not(upper),lower=not(lower),number=not(numbr))

if __name__ =='__main__':
    app.run(debug=True)