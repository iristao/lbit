import sqlite3
import os
import sqlite3, hashlib   #enable control of an sqlite database




def encrypt_password(password):
    encrypted_pass = hashlib.sha1(password.encode('utf-8')).hexdigest()
    return encrypted_pass


DATABASE = os.path.dirname(__file__) or '.'
DATABASE+="/../data/elevators.db"
db = sqlite3.connect(DATABASE, check_same_thread=False)
db.create_function('encrypt', 1, encrypt_password)
c = db.cursor()    #facilitate db ops
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

db.commit() #save changes
#db.close()  #close database
