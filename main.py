from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

def username_func():
    

@app.route("/")
def index():
    
    return render_template('home.html')

@app.route("/user_signup", methods=['POST'])
def errors():

    name_error = ''
    pass_error = ''
    ver_pass_error = ''
    email_error = ''

    username = request.form["username"]
    password = request.form["password"]
    ver_password = request.form["ver_password"]
    email = request.form["email"]

    if len(username) < 3 or len(username) > 20 :
        name_error = "You did not enter a valid username (must be 3-20 characters)"
        
    for let in username:
        if let == ' ':
            name_error = "You did not enter a valid username (may not contain spaces)"
            
        
    if len(password) == 0 :
        pass_error = "You did not enter a valid password"
    
    for char in password:
        if char == ' ':
            pass_error = "no spaces"
    
    if ver_password != password or len(ver_password) == 0 :
        ver_pass_error = "Your passwords do not match"

    for let in email:
        if let == '':
            email_error = ''
            break

        elif let == "@":
            email_error = ''
            break

        else:
            email_error = "Please enter a valid email"
    
        
        
    return render_template('home.html', name_error=name_error, pass_error=pass_error, ver_pass_error = ver_pass_error, email_error = email_error)
app.run()