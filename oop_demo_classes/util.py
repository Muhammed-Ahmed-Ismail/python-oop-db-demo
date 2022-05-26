import re
import os

import mysql.connector


# bad


def email_checker(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if re.fullmatch(regex, email):
        return True
    else:
        return False


def formate_email(sender, to, sub, receiver_name, body):
    return f'''
            from:{sender}
            to:{to}
            subject:{sub}
            
            Dear {receiver_name},
            
            {body}
            
            BestRegards 
            
    '''


def write_email(email):
    file = open('email', 'w')
    file.write(email)
    file.close()


def get_db_curser():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="muhammedahmed",
        database='pydb'
    )
    return mydb,mydb.cursor()

def prepare_data_base():
    db,cur=get_db_curser()
    cur.execute('''drop table if exists employees''')
    cur.execute('''
    create table employees (id int AUTO_INCREMENT primary key  , name varchar(50),is_manager bit,age int) ''')

