from flask import Flask, render_template, request, session, redirect, url_for, flash
import os, sqlite3, hashlib

USER_SESSION = "logged_in"

form_site = Flask(__name__)
form_site.secret_key = os.urandom(64)




#DIR = path.dirname(__file__)

filepath = os.path.dirname(__file__) 

filepath += "/" 
filepath += "db_builder.py"



execfile(filepath)


def display_name():
    if is_logged():
        ans = session[USER_SESSION]
        return ans[0:ans.find('@')]
    else:
        return "Guest"
   

#create dict of usernames and passwords
def user_dict():
    users = {} #{username: password}
    user_data = c.execute("SELECT * FROM users;")
    for data in user_data:
        users[data[0]] = data[1]
    return users

@form_site.route('/', methods=['POST', 'GET'])
#login page if user is not in session, otherwise welcome
def root():
    return render_template('homepage.html', login_user=display_name())

@form_site.route('/floor')
def floor():
	return render_template('floor.html', login_user=display_name())

@form_site.route('/stats')
def stats():
    return render_template('stats.html', login_user=display_name())

def is_logged():
    return USER_SESSION in session

def is_null(username, password, confpw):
    return username == "" or password == "" or confpw == ""

def add_session(username, password):
    if is_null(username, password, "filler"):
        flash("Username or password is blank")
        return False
    if(login_test(username, password)):
        session[USER_SESSION] = username
        return True
    else:
        flash("Incorrect login credentials")
        return False

@form_site.route("/login", methods=["GET", "POST"])
def login():
    if is_logged():
        return render_template("back.html", login_user=display_name())
    elif (request.method == "GET"):
        return render_template("login.html", login_user=display_name())
    else:
        email = request.form["email"]
        password = request.form["password"]
        if request.form["form"] == "Login":
            if add_session(email, password):
                return redirect(url_for("root"))
        else:
            if(password != request.form["confirm_password"]):
                flash("Oops! Your Password and Confirm Password did not match. :(")
            elif not create_account(email, password):
                flash("Invalid Email Address: It must be a  @stuy.edu email address that has not been previously registered.")
            else:
                flash("Congratulations! You have created an account successfully. :)")
    return render_template("login.html", login_user=display_name())

@form_site.route("/logout")
def logout():
    if is_logged():
        session.pop(USER_SESSION)
    return redirect(url_for("login"))

# Login - Returns true if successful, false otherwise
def login_test(email, password):
    db = sqlite3.connect("elevators.db")
    c = db.cursor()
    c.execute("SELECT email, password FROM accounts WHERE email = '%s'" % (email));
    for account in c:
        print account
        uemail = account[0]
        passw = account[1]
        # Check if email and encrypted password match
        if email == uemail and encrypt_password(password) == passw:
            print "Successful Login"
            return True
    print "Login Failed"
    return False
    
# Encrypt password - Returns SHA256
def encrypt_password(password):
    encrypted = hashlib.sha256(password).hexdigest()
    return encrypted

# Create account - Returns true if successful, false otherwise
def create_account(email, password):
    db = sqlite3.connect("elevators.db")
    c = db.cursor()
    if not does_email_exist(email) and is_valid_email(email):
        # Add user to accounts table
        c.execute("INSERT INTO accounts VALUES('%s', '%s')" % (email, encrypt_password(password)))
        db.commit()
        db.close()
        print "Create Account Successful"
        return True
    print "Create Account Failed"
    return False

# Checks if email exists - Returns true if email exists, false otherwise
def does_email_exist(email):
    db = sqlite3.connect("elevators.db")
    c = db.cursor()
    c.execute("SELECT email FROM accounts WHERE email = '%s'" % (email))
    for account in c:
        # Username exists
        print "Email exists"
        return True
    print "Email does not exist"
    return False

# Checks if email is stuy.edu - Returns true if it is, false otherwise
def is_valid_email(email):
    if (email.find("@stuy.edu") != -1) and (email.split("@")[1] == "stuy.edu"):
        print "Valid Email"
        return True
    print "Invalid Email"
    return False


#================= Debug =================
#DANGER DANGER! Set to FALSE before deployment!

if __name__ == '__main__':
    form_site.debug = True #DANGER DANGER! Set to FALSE before deployment!
    form_site.run()





#console output will appear in /var/log/apache2/error.log
