from flask import Flask, render_template, redirect, url_for, request
from os import path


app = Flask(__name__)
DIR = path.dirname(__file__)

app.secret_key = os.urandom(64)

execfile("db_builder.py")

#encrypts password
def encrypt_password(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

#create dict of usernames and passwords
def user_dict():
    users = {} #{username: password}
    user_data = c.execute("SELECT * FROM users;")
    for data in user_data:
        users[data[0]] = data[1]
    return users

#authenticate username and password
def authenticate(username, password):
    users = user_dict()
    if username in users.keys():
        if password == users[username]:
            return SUCCESS
        else:
            return BAD_PASS
    else:
        return BAD_USER

#check if username already exists
def check_newuser(username):
    users = user_dict()
    if username in users.keys():
        return BAD_USER
    return SUCCESS

@form_site.route('/', methods=['POST', 'GET'])
#login page if user is not in session, otherwise welcome
def root():
    if 'user' not in session:
        return render_template('login.html', title="Login")
    else:
        return redirect( url_for('welcome') )

@form_site.route('/signup', methods=['POST', 'GET'])
#register page is user is not in session, otherwise root
def register():
    if 'user' not in session:
        return render_template('signup.html', title="Register")
    else:
        return redirect( url_for('root') )

@form_site.route('/createaccount', methods=['POST', 'GET'])
#creates an account and runs encryption function on password
def create_account():
    username = request.form['user']
    password = request.form['pw']
    result = check_newuser(username)
    users = user_dict()
    if result == SUCCESS:
        with db:
            c.execute("INSERT INTO users VALUES (?, encrypt(?))", (username, password))
        users[username] = password
        flash(username + " registered.")
    elif result == BAD_USER:
        flash("That username is already in use. Try another one")
        return redirect(url_for('register'))
    return redirect(url_for('root'))

@form_site.route('/auth', methods=['POST', 'GET'])
#checks if login information is correct
def auth():
    username = request.form['user']
    password = request.form['pw']
    encrypted = encrypt_password(password)
    result = authenticate(username, encrypted)
    if result == SUCCESS:
        session['user'] = username
        flash(session['user'] + " successfully logged in.")
    if result == BAD_PASS:
        flash("Incorrect password.")
    elif result == BAD_USER:
        flash("Incorrect Username.")
    return redirect(url_for('root'))


@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/escalator')
def escalator():
	return render_template('escalator.html')


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
