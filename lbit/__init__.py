from flask import Flask, render_template, redirect, url_for, request
from os import path

app = Flask(__name__)

DIR = path.dirname(__file__)

#================= Root =================
@app.route('/')
def root():
    print "=====================================\nConsole Message\n"
    print DIR + "\n====================================="
    body = "<h2> Longer Blockchain Iced Tea </h2>"
    body+= "DIR: " + DIR + "<br>"
    body+= '<img src="' + url_for('static', filename='img/icedtea.jpeg') + '" width="500"</img>'
    return body

#================= Login =================
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



#================= Debug =================
#DANGER DANGER! Set to FALSE before deployment!

if __name__ == '__main__':
    app.debug = True #DANGER DANGER! Set to FALSE before deployment!
    app.run()
