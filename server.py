from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#Database Table Creation Section

#to create tables
#inside terminal
#from server import app, db
#app.app_context().push()
#db.create_all()

#Sign up table which contains data of user
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    phoneno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

@app.route("/login_or_sign_up", methods=["GET", "POST"])
def login_or_sign_up():
    if request.method == "POST":
        if request.form["submit"] == "log_in":
            l_username = request.form["l_username"]
            l_password = request.form["l_password"]
            print(l_username, l_password)

            user = User.query.filter_by(username=l_username).first()
            if not user:
                print("this username does not exist, Please Register")
                return redirect(url_for('login_or_sign_up'))
            elif not user.password == l_password:
                print("Password zincorrect, PLease Try Again")
                return redirect(url_for('login_or_sign_up'))
            else:
                print("Login")
        
        if request.form["submit"] == "Sign_up":
            s_username = request.form["s_username"]
            s_fname = request.form["s_fname"]
            s_lname = request.form["s_lname"]
            s_phoneno = request.form["s_phoneno"]
            s_email = request.form["s_email"]
            s_password = request.form["s_password"]
            print(s_username, s_fname, s_lname, s_phoneno, s_email, s_password)

            new_user = User(
                username = s_username,
                fname = s_fname,
                lname = s_lname,
                phoneno = s_phoneno,
                email = s_email,
                password = s_password
            )
            db.session.add(new_user)
            db.session.commit()
            print("new user data inserted into database")


    return render_template("loginorsignup.html")


if __name__ == "__main__":
    app.run(debug=True)

