from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def upperLevel(name):
    return not(any(x.isupper() for x in name))
def lowerLevel(name):
    return not(any(x.islower() for x in name))
def numberEnd(name):
    return not(name[-1].isdigit())

@app.route('/report')
def report():
    userName = request.args.get('UserName')
    upper = upperLevel(userName)
    lower = lowerLevel(userName)
    numbr = numberEnd(userName)
    if not(upper and lower and numbr):
        result = True
    else:
        result=False
    print(result)
    return render_template('report.html',result=result,upper=upper,lower=lower,number=numbr)

if __name__ =='__main__':
    app.run(debug=True)