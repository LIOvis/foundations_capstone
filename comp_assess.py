import sqlite3
import bcrypt
from datetime import date


def integ(a,b):
    try:
        cursor.execute(a, b)
    except sqlite3.IntegrityError:
        return False
    return True


class User:
    def __init__(self, user_id, first_name, last_name, phone, email, password, date_hired, date_created, role, active):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.date_hired = date_hired
        self.date_created = date_created
        self.role = role
        self.active = active


    def check_password(self, user_attempt_password):
        saved_password = self.password

        if bcrypt.checkpw(user_attempt_password.encode('utf-8'), saved_password):
            return True
        return False

    def new_password(self):
        attempt = input('\nCurrent Password: ')
        new = input('New Password: ')
        if self.check_password(attempt):
            self.password = bcrypt.hashpw(new.encode('utf-8'), bcrypt.gensalt()) 
            return f'\nNew Password: {new}'
        return 'Attempt does not match password.'

    def new_email(self):
        email = input('\nNew Email: ')
        self.email = email
        return f'\nNew Email: {self.email}'

    def __repr__(self):
        return '''User ID: %s
First Name: %s
Last Name: %s
Phone: %s
Email: %s
Password: %s
Date Hired: %s
Date Created: %s
Role: %s''' % (self.user_id, self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, self.role)
        
    def select(self):
        query = 'SELECT * FROM Users WHERE user_id = ?'
        value = (self.user_id,)
        row = cursor.execute(query, value).fetchone()
        if row == []:
            return 'No such user in database.'
        elif row != []:
            if row[9] == 0 or row[9] == None:
                activeyn = 'No'
            else:
                activeyn = 'Yes'
            
            for i in range(0,9):
                if row[i] == None:
                    row[i] == ''
            return f'''User ID: {row[0]}
First Name: {row[1]}
Last Name: {row[2]}
Phone: {row[3]}
Email: {row[4]}
Password: {row[5]}
Date Hired: {row[6]}
Date Created: {row[7]}
Role: {row[8]}
Active: {activeyn}
'''

    def save(self):
        query = 'SELECT * FROM Users WHERE user_id = ?'
        value = (self.user_id,)
        row = cursor.execute(query, value).fetchone()
        print(row)
        if row == () or row == None:
            query = 'INSERT INTO Users (user_id, first_name, last_name, phone, email, password, date_hired, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            values = self.user_id, self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, self.active
            if integ(query, values) == True:
                con.commit()
            else:
                print('Integrity Error: please make sure all fields meet their constraints.')
        else:
            query = 'UPDATE Users SET first_name = ?, last_name = ?, phone = ?, date_hired = ?, date_created = ?, role = ?, email = ?, password = ?, date_created = ? WHERE user_id = ?'
            values = self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, self.active, self.user_id
            if integ(query, values) == True:
                con.commit()
            else:
                print('Integrity Error: please make sure all fields meet their constraints.')

    def load(self, user_id):
        query = 'SELECT * FROM Users WHERE user_id = ?'
        value = (user_id,)
        row = cursor.execute(query, value).fetchone()
        self.user_id = row[0]
        self.first_name = row[1]
        self.last_name = row[2]
        self.phone = row[3]
        self.email = row[4]
        self.password = row[5]
        self.date_hired = row[6]
        self.date_created = row[7]
        self.role = row[8]


con = sqlite3.connect('competency.db')
cursor = con.cursor()


today = date.today()
today_str = today.strftime('%Y-%m-%d')


activeyn