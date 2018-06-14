import os
from os import path
import sqlite3, hashlib   #enable control of an sqlite database



def encrypt_password(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

DATABASE = path.dirname(__file__) + "/../data/closet.db"
print "DIR: " + DATABASE

datab = sqlite3.connect(DATABASE, check_same_thread=False)
datab.create_function('encrypt', 1, encrypt_password)
c = datab.cursor()    #facilitate db ops
print DATABASE + "xxx"

create_accounts = "CREATE TABLE accounts (email TEXT PRIMARY KEY, password TEXT);"
#0 - default status (working)
#1 - not working
#2 - broken (repairs)

create_elevators = "CREATE TABLE elevators (id TEXT PRIMARY KEY, status INTEGER);"
enable_elevators = "INSERT INTO elevators (id, status) VALUES ('2_3_up', 0), ('2_3_down', 0), ('2_4_up', 0), ('2_4_down', 0), ('3_5_up', 0), ('3_5_down', 0), ('4_6_up', 0), ('4_6_down', 0), ('5_7_up', 0), ('5_7_down', 0), ('6_8_up', 0), ('6_8_down', 0), ('7_9_up', 0), ('7_9_down', 0);"

insert_admin = "INSERT INTO accounts VALUES ('test', encrypt('test'));"

values_to_insert = [(23, 0), (32, 0), (24, 0), (42, 0), (35, 0), (53, 0), (46, 0), (64, 0), (57, 0), (75, 0), (68, 0), (86, 0), (79, 0), (97, 0)]



try:
    c.execute(create_accounts)
    c.execute(create_elevators)
    c.execute(enable_elevators)
    c.execute(insert_admin)
    c.executemany("INSERT INTO some_table ('item_num', 'item_name') VALUES (?, ?);", values_to_insert)
except:
    pass

datab.commit() #save changes
#db.close()  #close database


# Login - Returns true if successful, false otherwise
def login_test(email, password):
    # datab = sqlite3.connect("elevators.db")
    # c = datab.cursor()

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
    # datab = sqlite3.connect("elevators.db")
    # c = datab.cursor()


    if is_valid_email(email) and not does_email_exist(email):
        add_user(email, password)
        print "Create Account Successful"
        return True
    print "Create Account Failed"
    return False

def add_user(email, password):
    # Add user to accounts table
	datab = sqlite3.connect(DATABASE) #open if f exists, otherwise creat
	c = datab.cursor()
	hash_pass = encrypt_password(password)
	print ('The string to store in the db is: ' + hash_pass)
	c.execute('INSERT INTO accounts VALUES("%s", "%s");' %(email, hash_pass))

#    c.execute("INSERT INTO accounts VALUES ('%s', '%s')" % (email, encrypt_password(password)))

	print "it got added bro"
	datab.commit()
	datab.close()

# Checks if email exists - Returns true if email exists, false otherwise
def does_email_exist(email):
    # datab = sqlite3.connect("elevators.db")
    # c = datab.cursor()

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
