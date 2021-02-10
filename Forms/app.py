from flask import Flask, redirect,render_template,session,url_for,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class projectForm (FlaskForm):
    breed = StringField('What breed are you?')
    submit = SubmitField('Submit')
    
@app.route('/',methods=['GET','POST'])
def index():
    form = projectForm()
    
    session['breed']=form.breed.data
    
    if form.validate_on_submit():
        flash(f"You just clicked the {session['breed']}!")

        return redirect(url_for('index'))
    
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)
    