from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["submit"] == "log_in":
            l_username = request.form["l_username"]
            l_password = request.form["l_password"]
            print(l_username, l_password)
        
        if request.form["submit"] == "Sign_up":
            s_username = request.form["s_username"]
            s_fname = request.form["s_fname"]
            s_lname = request.form["s_lname"]
            s_phoneno = request.form["s_phoneno"]
            s_email = request.form["s_email"]
            s_password = request.form["s_password"]
            print(s_username, s_fname, s_lname, s_phoneno, s_email, s_password)

    return render_template("loginorsignup.html")


if __name__ == "__main__":
    app.run(debug=True)

