from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(80), nullable = True)
    lname = db.Column(db.String(80), nullable = True)
    date = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, fname, lname, date):
        self.fname = fname
        self.lname = lname
        self.date = date

    def __repr__(self):
        return U'<User%r' % self.fname

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("app.html")
    else:
        firstname = request.form['fname']
        lastname = request.form['lname']
        user = User(fname=firstname, lname=lastname, date = datetime.now())
        db.session.add(user)
        db.session.commit()
        the_name = User.query.all()
        return render_template("get.html", names = the_name)




if __name__ == "__main__":
    app.run(debug = True)