# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return 'this is the main page'

def latinName(name):
    if name[-1]!='y':
        return name+'y'
    else:
        return name[:-1]+'iful'

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    return f'Hi {name}, your latin name is {latinName(name)}'
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
