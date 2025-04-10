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
            
            sel_last_name = row[2]
            sel_phone = row[3]
            sel_hire_date = row[6]
            sel_date_created = row[7]
            if sel_last_name == None:
                sel_last_name = 'n/a'
            if sel_phone == None:
                sel_phone = 'n/a'
            if sel_hire_date == None:
                sel_hire_date = 'n/a'
            if sel_date_created == None:
                sel_date_created = 'n/a'
            

            return f'''User ID: {row[0]}
First Name: {row[1]}
Last Name: {sel_last_name}
Phone: {sel_phone}
Email: {row[4]}
Hire Date: {sel_hire_date}
Date Created: {sel_date_created}
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


    def load_all_records(self):
        user_response = input('''Which table would you like to view?
(1) Users
(2) Competencies
(3) Assessments
(4) Competency Assessment Results
(5) Return to Main Menu
>>> ''')
        if user_response not in ['1', '2', '3', '4', '5']:
            print('\nPlease enter a valid response.\n')
        elif user_response == '1':
            user_response = input('''
(1) View All Users
(2) View All Active Users
(3) View All Inactive Users
(4) Return to Main Menu
>>> ''')
            if user_response not in ['1', '2', '3', '4']:
                print('\nPlease enter a valid response.\n')
            elif user_response == '4':
                continue
            else:
                if user_response == '1':
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
                            sel_last_name = 'n/a'
                        if sel_hire_date == None:
                            sel_hire_date = 'n/a'
                        full_name = f'{sel_first_name} {sel_last_name}'

                        print(f'{sel_user_id:<5}{full_name:<35}{sel_hire_date:<15}{sel_role:<15}{sel_email}')
                    
                elif user_response == '2':
                    rows = cursor.execute('SELECT user_id, first_name, last_name, date_hired, role, email FROM Users WHERE active = 1').fetchall()
                    print(f'\n{'ID':<5}{'Name':<35}{'Hire Date':<15}{'Role':<15}Email')
                    for row in rows:
                        sel_user_id = row[0]
                        sel_first_name = row[1]
                        sel_last_name = row[2]
                        sel_hire_date = row[3]
                        sel_role = row[4]
                        sel_email = row[5]
                        if sel_last_name == None:
                            sel_last_name = 'n/a'
                        if sel_hire_date == None:
                            sel_hire_date = 'n/a'
                        full_name = f'{sel_first_name} {sel_last_name}'

                        print(f'{sel_user_id:<5}{full_name:<35}{sel_hire_date:<15}{sel_role:<15}{sel_email}')
                    
                elif user_response == '3':
                    rows = cursor.execute('SELECT user_id, first_name, last_name, date_hired, role, email FROM Users WHERE active != 1').fetchall()
                    print(f'\n{'ID':<5}{'Name':<35}{'Hire Date':<15}{'Role':<15}Email')
                    for row in rows:
                        sel_user_id = row[0]
                        sel_first_name = row[1]
                        sel_last_name = row[2]
                        sel_hire_date = row[3]
                        sel_role = row[4]
                        sel_email = row[5]
                        if sel_last_name == None:
                            sel_last_name = 'n/a'
                        if sel_hire_date == None:
                            sel_hire_date = 'n/a'
                        full_name = f'{sel_first_name} {sel_last_name}'

                        print(f'{sel_user_id:<5}{full_name:<35}{sel_hire_date:<15}{sel_role:<15}{sel_email}')
                    
                user_response = input('\nEnter an ID to View a User.\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

                if user_response == '':
                    continue
                else:
                    user1.select(user_response)
                    print('')
                
                

        elif user_response == '2':
            rows = cursor.execute('SELECT competency_id, name FROM Competencies').fetchall()
            print(f'\n{'ID':<5}{'Name'}')
            for row in rows:
                print(f'{row[0]:<5}{row[1]}')
            
            user_response = input('\nEnter an ID to View a Competency.\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

            if user_response == '':
                continue
            else:
                query = 'SELECT * FROM Competencies where competency_id = ?'
                values = user_response

                row = cursor.execute(query, values).fetchone()
                if row = ():
                    print('\nPlease Enter a Valid ID.\n')
                else:
                    sel_description = row[2]
                    if sel_description == None:
                        sel_description = 'n/a'
                    print(f'''
Competency ID: {row[0]}
Name: {row[1]}
Description:
{sel_description}
''')

        elif user_response == '3':
            rows = cursor.execute('SELECT assessment_id, competency_id, name FROM Assessments').fetchall()
            print(f'\n{'Assessment ID':<15}{'Competency ID':<15}{'Name'}')
            for row in rows:
                print(f'{row[0]:^15}{row[1]:^15}{row[3]}')
             
            user_response = input('\nEnter an ID to View an Assessment\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

            if user_response == '':
                continue
            else:
                query = 'SELECT * FROM Assessments where assessment_id = ?'
                values = user_response

                row = cursor.execute(query, values).fetchone()
                if row = ():
                    print('\nPlease Enter a Valid ID.\n')
                elif row != ():
                    if row[3] == None:
                        sel_description = 'n/a'
                    else:
                        sel_description = row[3]
                    print(f'''
Assessment ID: {row[0]}
Competency ID: {row[1]}
Name: {row [2]}
Description:
{sel_description}
''')

        elif user_response == '4':
            user_response = input('''
(1) View All Assessment Results
(2) View All Results of an Assessment
(3) View All Results of a User
(4) Return to Main Menu
>>> ''')
            if user_response not in ['1', '2', '3', '4']:
                print('\nPlease enter a valid response.\n')
            elif user_response == '4':
                continue
            else:
                if user_response == '1':
                    rows = cursor.execute('SELECT result_id, user_id, assessment_id, score, date_taken FROM Competency_Assessment_Results').fetchall()
                    print(f'{'Result ID':<12}{'User ID':<10}{'Assessment ID':<15}{'Score':<8}Date Taken')
                    for row in rows:
                        print(f'{row[0]:<12}{row[1]:<10}{row[2]:<15}{row[3]:<8}{row[4]}')
                    print('')
                elif user_response == '2':
                    user_response = input('\nPlease Enter the Assessment ID: ')
                    query = 'SELECT result_id, assessment_id, user_id, score, date_taken FROM Competency_Assessment_Results WHERE assessment_id = ?'
                    values = (user_response,)
                    rows = cursor.execute(query, values).fetchall()
                    if rows == ():
                        print('\nPlease Enter a Valid ID.\n')
                    elif rows != ():
                        print(f'{'Result ID':<12}{'Assessment ID':<15}{'User ID':<10}{'Score':<8}Date Taken')
                        for row in rows:
                            print(f'{row[0]:<12}{row[1]:<15}{row[2]:<10}{row[3]:<8}{row[4]}')
                        print('')
                elif user_response == '3':
                    user_response = input('\nPlease Enter the User ID: ')
                    query = 'SELECT result_id, user_id, assessment_id, score, date_taken FROM Competency_Assessment_Results WHERE user_id = ?'
                    values = (user_response,)
                    rows = cursor.execute(query, values).fetchall()
                    if rows == ():
                        print('\nPlease Enter a Valid ID.\n')
                    elif rows != ():
                        print(f'{'Result ID':<12}{'User ID':<10}{'Assessment ID':<15}{'Score':<8}Date Taken')
                        for row in rows:
                            print(f'{row[0]:<12}{row[1]:<10}{row[2]:<15}{row[3]:<8}{row[4]}')
                        print('')
                user_response = input('\nEnter a Result ID to View a Competency Assessment Result\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

                if user_response == '':
                    continue
                else:
                    query = 'SELECT * FROM Competency_Assessment_Results where result_id = ?'
                    values = user_response

                    row = cursor.execute(query, values).fetchone()
                    if row == ():
                        print('\nPlease Enter a Valid ID.\n')
                    elif row != ():
                        if row[5] == None:
                            sel_manager_id = 'n/a'
                        else:
                            sel_manager_id = row[5]
                        print(f'''
Result ID: {row[0]}
User ID: {row[1]}
Assessment ID: {row[2]}
Score: {row[3]}
Date Taken: {row[4]}
Manager ID: {sel_manager_id}
''')
                    

        print('\n')



con = sqlite3.connect('competency.db')
cursor = con.cursor()


today = date.today()
today_str = today.strftime('%Y-%m-%d')


user_response = ''

sel_user_id = ''
sel_first_name = ''
sel_last_name = ''
sel_phone = ''
sel_email = ''
sel_password = ''
sel_hire_date = ''
sel_date_created = ''
sel_role = ''

sel_description = ''

sel_manager_id = ''

activeyn = ''
full_name = ''

query = ''
values = ''

print(f'{'Welcome!':^20}')
email_login = input('Email: ')
password_login = input('Password: ')

query = 'SELECT * FROM Users WHERE email = ? AND password = ?'
values = (email_login, password_login)

login_attempt = cursor.execute(query, values).fetchone()

if login_attempt == () or login_attempt[9] != 1:
    print('\nLogin Unsuccessful.\nPlease Try Again.\n')
else:
    if login_attempt[8].lower == 'admin':
        user1 = Admin('','','','','','','','')
        user1.load(login_attempt[0])

query = 'INSERT INTO Users (first_name, last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
values = (user2.first_name, user2.last_name, user2.phone, user2.email, user2.password, user2.hire_date, user2.date_created, user2.role, user2.active)