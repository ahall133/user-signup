from flask import Flask, request, render_template
from functions import username_func, password_func, ver_pass_func, email_func
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/user_signup_error", methods=['POST'])
def errors():
    username = request.form['username']
    password = request.form['password']
    ver_password = request.form['ver_password']
    email = request.form['email']

    name_error = username_func(username)
    pass_error = password_func(password)
    ver_pass_error = ver_pass_func(password, ver_password)
    email_error = email_func(email)

    return render_template('home.html', name_error=name_error, pass_error=pass_error, ver_pass_error = ver_pass_error, email_error = email_error)
app.run()