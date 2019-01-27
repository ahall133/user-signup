from flask import Flask, request, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

error = "there is and error"

@app.route("/")
def index():
    
    return render_template('home.html')

@app.route("/user_signup", methods=['POST'])
def enter_name():
    username = request.form["username"]

    if len(username) == 0 :
        return render_template('home.html', error = error)
        print("error")
        
    return render_template('home.html')
app.run()