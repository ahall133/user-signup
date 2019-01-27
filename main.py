from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def username_func():
    username = request.form['username']
    name_error = ''

    if len(username) < 3 or len(username) > 20 :
        name_error = "You did not enter a valid username (must be 3-20 characters)"
        
    for let in username:
        if let == ' ':
            name_error = "You did not enter a valid username (may not contain spaces)"

    return name_error

def password_func():
    password = request.form['password']
    pass_error = ''

    if len(password) < 3 or len(password) > 20 :
            pass_error = "You did not enter a valid password (must be 3-20 characters)"
        
    for char in password:
        if char == ' ':
            pass_error = "You did not enter a valid password (may not contain spaces)"

    return pass_error

def ver_pass_func():
    ver_password = request.form['ver_password']
    password = request.form['password']
    ver_pass_error = ''

    if ver_password != password or len(ver_password) == 0:
        ver_pass_error = "Your passwords do not match"
    
    return ver_pass_error

def email_func():
    email = request.form['email']
    email_error = ''

    for let in email:
        if let == '':
            email_error = ''
            break

        elif let == "@":
            email_error = ''
            break

        else:
            email_error = "Please enter a valid email"

    return email_error

    

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/user_signup", methods=['POST'])
def errors():
    name_error = username_func()
    pass_error = password_func()
    ver_pass_error = ver_pass_func()
    email_error = email_func()
                 

   
    
        
        
    return render_template('home.html', name_error=name_error, pass_error=pass_error, ver_pass_error = ver_pass_error, email_error = email_error)
app.run()