from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["submit"] == "log_in":
            siname = request.form["siname"]
            sipass = request.form["sipass"]
            print(siname, sipass)
        
        if request.form["submit"] == "Sign_up":
            username = request.form["username"]
            print(username)


    return render_template("loginorsignup.html")


if __name__ == "__main__":
    app.run(debug=True)

