from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class addForm(FlaskForm):
    name = StringField('What is the name of the Puppy?') 
    submit = SubmitField('Submit')
    
class delForm(FlaskForm):
    id = IntegerField('What is the id of the puppy')
    submit = SubmitField('Submit')
    
class addFormOwner(FlaskForm):
    id = IntegerField('What is the id of the puppy')
    name = StringField('What is your name')
    submit = SubmitField('Submit')