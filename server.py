from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




#to be codded 
#login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#Database Table Creation Section
# app.app_context().push()

#to create tables
#inside terminal
#from server import app, db
#app.app_context().push()
#db.create_all()

#Sign up table which contains data of user
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    phoneno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

# class userBalance(UserMixin, db.Model):
#     username = db.Column(db.String(100), primary_key=True)
#     balance = db.Column(db.String(100))



@app.route("/login_or_sign_up", methods=["GET", "POST"])
def login_or_sign_up():

    #login
    if request.method == "POST":
        if request.form["submit"] == "log_in":


            l_username = request.form["l_username"]
            l_password = request.form["l_password"]
            print(l_username, l_password) 

            user = User.query.filter_by(username=l_username).first()
            if not user:
                flash("this username does not exist, Please Register")
                return redirect(url_for('login_or_sign_up'))
            elif not check_password_hash(user.password, l_password):
                flash("Password zincorrect, PLease Try Again")
                return redirect(url_for('login_or_sign_up'))
            else:
                login_user(user)
                return redirect(url_for('home'))
        
        #sign up
        if request.form["submit"] == "Sign_up":

            if User.query.filter_by(username=request.form.get('l_username')).first():
            #User already exists
                flash("You've already signed up with that username, log in instead!")
                return redirect(url_for('login'))


            s_username = request.form["s_username"]
            s_fname = request.form["s_fname"]
            s_lname = request.form["s_lname"]
            s_phoneno = request.form["s_phoneno"]
            s_email = request.form["s_email"]
            s_password = request.form["s_password"]
            print(s_username, s_fname, s_lname, s_phoneno, s_email, s_password)

            hash_and_salted_password = generate_password_hash(
                s_password,
                method='pbkdf2:sha256',
                salt_length=8
            )

            new_user = User(
                username = s_username,
                fname = s_fname,
                lname = s_lname,
                phoneno = s_phoneno,
                email = s_email,
                password = hash_and_salted_password
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("home"))

            #database of new user
            # modelName = s_username + "db"
            # class modelName(db.Model):
            #     transcation_id = db.Column(db.Integer, primary_key=True)
            #     transaction_amt = db.Column(db.Integer)
            #     remaning_amt = db.Column(db.Integer)
            # # db.create_all()
            # modelName.__table__.create(db.session.bind, checkfirst=True)

            print("new user data inserted into database")


    return render_template("loginorsignup.html", logged_in=current_user.is_authenticated)

@app.route("/")
def main():
    return redirect(url_for('login_or_sign_up'))


#home page or main landing page
@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    # print(current_user.username)
    return render_template("home.html", username=current_user.username, logged_in=True)

#logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login_or_sign_up'))


#pay section

#username pay
@app.route("/pay/username", methods=["GET", "POST"])
@login_required
def pay_username():
    if request.method == 'POST':
        p_username = request.form["username"]
        p_amount = request.form["amount"]
        print(p_amount, p_username)
    return render_template("pay_username.html")

#qr pay
@app.route("/pay/qr")
@login_required
def pay_qr():
    return render_template("pay_qr.html")

#phone no pay
@app.route("/pay/phoneno")
@login_required
def pay_phoneno():
    return render_template("pay_phoneno.html")

#bank transfer
@app.route("/pay/banktransfer")
@login_required
def pay_banktransfer():
    return render_template("pay_banktransfer.html")

if __name__ == "__main__":
    app.run(debug=True)

