import sqlite3, hashlib   #enable control of an sqlite database

f="elevators.db"

def encrypt_password(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass

db = sqlite3.connect(f, check_same_thread=False) #open if f exists, otherwise create
db.create_function('encrypt', 1, encrypt_password)
c = db.cursor()    #facilitate db ops

create_users = "CREATE TABLE users (username TEXT PRIMARY KEY, password TEXT NOT NULL);"
#0 - default status (working)
#1 - not working
#2 - broken (repairs)

create_elevators = "CREATE TABLE elevators (id INTEGER PRIMARY KEY, status INTEGER NOT NULL );"

insert_admin = "INSERT INTO users VALUES ('test', encrypt('test'));"

values_to_insert = [(23, 0), (32, 0), (24, 0), (42, 0), (35, 0), (53, 0), (46, 0), (64, 0), (57, 0), (75, 0), (68, 0), (86, 0), (79, 0), (97, 0)]



try:
    c.execute(create_users)
    c.execute(create_elevators)
    c.execute(insert_admin)
    c.executemany("INSERT INTO some_table ('item_num', 'item_name') VALUES (?, ?);", values_to_insert)
except:
    pass

db.commit() #save changes
#db.close()  #close database
