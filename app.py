# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.

@app.route('/')
def index():
# ‘/’ URL is bound with hello_world() function.
    return render_template("index.html")




@app.route('/getdata', methods=["POST", "GET"])
def getData():
    if request.method=="POST":
        fname = request.form["fname"]
        email = request.form["memail"]
        sex = request.form["sex"]
        address = request.form["address"]
        full_details = "Full name:  " + fname + " " + "email: " + email + " " + "sex: " + sex + " address: "+ " "+ address
        print(full_details)
        return "your Full details are: " + "\n" + full_details
    return render_template("index.html")



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        return "login details: " + email + " " + password
    return render_template("login.html")



@app.route("/reg", methods=["POST", "GET"])
def reg():
    if request.method=="POST":
        print("post request")
        #email = request.form["email"]
        # password = request.form["password"]
        # return "login details: " + email + " " + password
    return render_template("reg.html")



# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
