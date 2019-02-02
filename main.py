from flask import Flask, request, render_template, redirect
from functions import username_func, password_func, ver_pass_func, email_func
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/user_signup", methods=['POST'])
def errors():
    username = request.form['username']
    username = cgi.escape(username)
    password = request.form['password']
    ver_password = request.form['ver_password']
    email = request.form['email']
    

    name_error = username_func(username)
    pass_error = password_func(password)
    ver_pass_error = ver_pass_func(password, ver_password)
    email_error = email_func(email)

    ready_to_redirect = None

    if name_error== '' and pass_error== '' and ver_pass_error == '' and email_error== '':
        ready_to_redirect = True

    if ready_to_redirect == True:
        return render_template('welcome.html', name=username)

    else:
        return render_template('home.html', me=username, emailme=email, name_error=name_error, pass_error=pass_error, ver_pass_error = ver_pass_error, email_error = email_error)
       
app.run()
#finished

