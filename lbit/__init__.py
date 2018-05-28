from flask import Flask, render_template, redirect, url_for, request
from os import path


app = Flask(__name__)
DIR = path.dirname(__file__)


@app.route('/')
def root():
	return render_template('homepage.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/signup')
def signup():
	return render_template('signup.html')




#================= Login =================
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)


#================= Debug =================
#DANGER DANGER! Set to FALSE before deployment!

if __name__ == '__main__':
    app.debug = True #DANGER DANGER! Set to FALSE before deployment!
    app.run()


from flask import Flask, url_for
from os import path



#console output will appear in /var/log/apache2/error.log




