import os
from forms import  addForm , delForm,addFormOwner
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.getcwd()

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):
    __tablename__='puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)
    
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f'The name of the puppy is {self.name} and the owner is {self.owner}'
        else:
            return f'The name of the puppy is {self.name} and has no owner yet!'
    
class Owner(db.Model):
    __tablename__='owners'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))
    
    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id = puppy_id
    def __repr__(self):
        return f'{self.name}'
        
@app.route('/')
def index():
    return render_template('base.html')

@app.route('/add_pup',methods=['GET','POST'])
def add_pup():
    form = addForm()
    
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add_pup.html',form=form)

@app.route('/del_pup',methods=['GET','POST'])
def del_pup():
    form = delForm()
    
    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('del_pup.html',form=form)

@app.route('/list_pup',methods=['GET','POST'])
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list_pup.html',puppies=puppies)

@app.route('/owner',methods=['GET','POST'])
def owner():
    form = addFormOwner()
    
    if form.validate_on_submit():
        id = form.id.data
        name = form.name.data
        print(id)
        print(name)
        add_owner = Owner(name,id)
        db.session.add(add_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('owner.html',form=form)

if __name__ =='__main__':
    app.run(debug=True)

    