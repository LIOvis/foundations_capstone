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
    def __init__(self, first_name, last_name, phone, email, password, date_hired, role, active):
        self.user_id = ''
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.date_hired = date.today().strftime('%Y-%m-%d')
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
        if self.active == 1 or self.active == '1':
            activeyn = 'Yes'
        else:
            activeyn = 'No'
        return '''User ID: %s
First Name: %s
Last Name: %s
Phone: %s
Email: %s
Password: %s
Date Hired: %s
Date Created: %s
Role: %s
Active: %s''' % (self.user_id, self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, activeyn)
        
    def select(self, user_id = self.user_id):
        query = 'SELECT * FROM Users WHERE user_id = ?'
        value = (user_id,)
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
Hire Date: {row[6]}
Date Created: {row[7]}
Role: {row[8]}
Active: {activeyn}
'''

    def save(self):
        query = 'SELECT * FROM Users WHERE email = ?'
        value = (self.email,)
        row = cursor.execute(query, value).fetchone()
        print(row)
        if row == () or row == None:
            query = 'INSERT INTO Users (first_name, last_name, phone, email, password, date_hired, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
            values = (self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, self.active)
            if integ(query, values) == True:
                con.commit()
            else:
                print('Integrity Error: please make sure all fields meet their constraints.')
        else:
            query = 'UPDATE Users SET first_name = ?, last_name = ?, phone = ?, date_hired = ?, date_created = ?, role = ?, email = ?, password = ?, date_created = ? WHERE user_id = ?'
            values = (self.first_name, self.last_name, self.phone, self.email, self.password, self.date_hired, self.date_created, self.role, self.active, self.user_id)
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
        self.active = row[9]

    
class Admin(User):
    def __init__(self, first_name, last_name, phone, email, password, date_hired, active):
        User.__init__(first_name, last_name, phone, email, password, date_hired, 'Admin', active)


    def load_all_records():
        user_response = input('''Which table would you like to view?
(1) Users
(2) Competencies
(3) Assessments
(4) Competency Assessment Results
(5) Return to Main Menu''')
        if user_response not in ['1', '2', '3', '4', '5']:
            print('Please enter a valid response.')
        elif user_response == '1':
            rows = cursor.execute('SELECT user_id, first_name, last_name, date_hired, role, email FROM Users').fetchall()
            print(f'\n{'ID':<5}{'Name':<35}{'Hire Date':<15}{'Role':<15}Email')
            for row in rows:
                sel_user_id = row[0]
                sel_first_name = row[1]
                sel_last_name = row[2]
                sel_hire_date = row[3]
                sel_role = row[4]
                sel_email = row[5]
                if sel_last_name == None:
                    sel_last_name = ''
                if sel_hire_date == None:
                    sel_hire_date = ''
                full_name = f'{sel_first_name} {sel_last_name}'

                print(f'{sel_user_id:<5}{full_name:<35}{sel_hire_date:<15}{sel_role:<15}{sel_email}')
            
            user_response = input('\nEnter an ID to View a User.\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

            if user_response == '':
                continue
            else:
                user1.select(user_response)
                
                

        elif user_response == '2':
            rows = cursor.execute('SELECT competency_id, name FROM Competencies').fetchall()
        elif user_response == '3':
            rows = cursor.execute('SELECT assessment_id, competency_id, name FROM Assessments').fetchall()
        elif user_response == '4':
            rows = cursor.execute('SELECT result_id, user_id, assessment_id, score, date_taken FROM Competency_Assessment_Results').fetchall()

        print('\n')



con = sqlite3.connect('competency.db')
cursor = con.cursor()


today = date.today()
today_str = today.strftime('%Y-%m-%d')

sel_user_id = ''
sel_first_name = ''
sel_last_name = ''
sel_phone = ''
sel_email = ''
sel_password = ''
sel_hire_date = ''
sel_date_created = ''
sel_role = ''

activeyn = 0
full_name = ''

query = ''
values = ''

print(f'{'Welcome!':^20}')
email_login = input('Email: ')
password_login = input('Password: ')

query = 'SELECT * FROM Users WHERE email = ? AND password = ?'
values = (email_login, password_login)

login_attempt = cursor.execute(query, values).fetchone()

if login_attempt == ():
    print('\nLogin Unsuccessful.\nPlease Try Again.\n')
else:
    if login_attempt[8].lower == 'admin':
        user1 = Admin('','','','','','','','')
        user1.load(login_attempt[0])

query = 'INSERT INTO Users (first_name, last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
values = (user2.first_name, user2.last_name, user2.phone, user2.email, user2.password, user2.hire_date, user2.date_created, user2.role, user2.active)