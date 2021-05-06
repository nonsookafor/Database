from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

firstname = ""
lastname = ""
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///name.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(80), unique = True)
    lname = db.Column(db.String(80), unique = True)

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return U'<User%r' % self.fname

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("app.html")
    else:
        firstname = request.form['fname']
        lastname = request.form['lname']
        user = User(fname=firstname, lname=lastname)
        db.session.add(user)
        db.session.commit()
        return "Gotten"




if __name__ == "__main__":
    app.run(debug = True)