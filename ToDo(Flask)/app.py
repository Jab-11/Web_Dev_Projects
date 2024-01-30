from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
app.config["SQLALCHEMY_BINDS"] = {
    'trash': 'sqlite:///trash.db',
    'done': 'sqlite:///done.db'
}
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

app.app_context().push()

class Todo(db.Model):
    __tablename__ = 'todo'
    sno = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), nullable=False)
    d_date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"{self.sno} - {self.todo}"

class Trash(db.Model):
    __bind_key__ = 'trash'
    __tablename__ = 'trash'
    sno = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), nullable=False)
    d_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10))

class Done(db.Model):
    __bind_key__ = 'done'
    __tablename__ = 'completed'
    sno = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(50), nullable=False)
    d_date = db.Column(db.DateTime, default=datetime.utcnow)
    c_date = db.Column(db.DateTime, default=datetime.utcnow)
    
    
@app.route('/', methods=["GET","POST"])
def home():
    if request.method =="POST":
        title = request.form['todo']
        date_str = request.form['date']
        date = datetime.strptime(date_str, '%Y-%m-%d')
        todo = Todo(todo=title,d_date=date)
        db.session.add(todo)
        db.session.commit()
    all = Todo.query.all()
    # print(all)
    return render_template("index.html",all=all)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    title = todo.todo
    date = todo.d_date
    trash = Trash(todo=title,d_date=date,status='Pending')
    db.session.delete(todo)
    db.session.add(trash)
    db.session.commit()
    return redirect("/")

@app.route('/done/<int:sno>')
def done(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    title = todo.todo
    date = todo.d_date
    done = Done(todo=title,d_date=date)
    db.session.delete(todo)
    db.session.add(done)
    db.session.commit()
    return redirect("/")
    
@app.route('/done')
def completed():
    all_c = Done.query.all()
    return render_template("done.html",all=all_c)

@app.route('/done/delete/<int:sno>')
def d_delete(sno):
    done = Done.query.filter_by(sno=sno).first()
    title = done.todo
    date = done.d_date
    trash = Trash(todo=title,d_date=date,status='Completed')
    db.session.delete(done)
    db.session.add(trash)
    db.session.commit()
    return redirect("/done")

@app.route('/trash')
def trash():
    all_t = Trash.query.all()
    return render_template("trash.html",all=all_t)

@app.route('/trash/delete/<int:sno>/')
def t_delete(sno):
    trash = Trash.query.filter_by(sno=sno).first()
    db.session.delete(trash)
    db.session.commit()
    return redirect("/trash")

if __name__ == "__main__":
    with app.app_context():
        # Create the database tables
        db.create_all()
    app.run(debug=True)