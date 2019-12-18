import sqlite3
from sqlite3 import Error
# Create the datbases for matric numbers and passwords
connect_matric = sqlite3.connect('matric.db')
connect_password = sqlite3.connect('password.db')

# Dummy entries to test the code 
a = 'QTS/2015/039' #Dummy username
b = "simi" # Dummy password

# cursors for each of the databases
cursor_matric = connect_matric.cursor()
cursor_password = connect_password.cursor()

# creating the tables for all the entries of matric numbers and passwords
# cursor_matric.execute("CREATE TABLE entries(matric_number text)")
# cursor_matric.execute("INSERT INTO entries VALUES('QTS/2015/039')" )
connect_matric.commit()
# cursor_password.execute("CREATE TABLE entries(password text)")
# cursor_password.execute("INSERT INTO entries VALUES('simi')")
# connect_password.commit()
# check if the matric number exists in the database
def validate():
    cursor_matric.execute("SELECT matric_number from entries WHERE matric_number = (?)", (a,))
    xxx = cursor_matric.fetchone()
    print(xxx)    
    if xxx != None:
        if a == xxx[0]:
            print('True')
            cursor_matric.execute("UPDATE entries set matric_number = (?) WHERE matric_number = (?)", (a +"voted", a,))
            connect_matric.commit()
    else:
        print("we couldn't find a match for matric number")
    
    cursor_password.execute("SELECT password from entries WHERE password = (?)", (b,))
    yyy = cursor_password.fetchone()
    print(yyy)    
    if yyy != None:
        if b == yyy[0]:
            print('True')
            cursor_password.execute("UPDATE entries set password = (?) WHERE password = (?)", (b +"voted", b,))
            connect_password.commit()
    else:
        print("we couldn't find a match for password")
validate()










# def sql_connection():
#     try:
#         con = sqlite3.connect('users.db')
#         return con
#     except Error:
#         print(Error)
# def table(con):
#     
#     cursorObj = con.cursor()
#     # cursorObj.execute("CREATE TABLE voters(matric_number text, password text)")
#     cursorObj.execute("INSERT INTO voters VALUES('QTS/2015/039', 'simi')")
#     cursorObj.execute("INSERT INTO voters VALUES('QTS/2015/038', 'olamide')")
#     cursorObj.execute("UPDATE voters SET matric_number = 'giran' where matric_number='QTS/2015/039' ")
#     cursorObj.execute("DROP TABLE voters")
#     con.commit()
#     cursorObj.execute("SELECT * from voters where matric_number = 'giran'")
#     xxx = cursorObj.fetchall()
#     print(xxx)
#     print(len(xxx))

#     con.commit()
# con = sql_connection()
# cursorObj = con.cursor()
# table(con)