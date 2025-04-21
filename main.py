import sqlite3
import bcrypt
from datetime import date
import csv
import os

def str_to_int(str_value):
    try:
        int_value = int(str_value)
        return int_value
    except ValueError:
        return False

def integ(a,b):
    try:
        cursor.execute(a, b)
    except sqlite3.IntegrityError:
        return False
    return True

def check_password(saved_password, user_attempt_password):

    if bcrypt.checkpw(user_attempt_password.encode('utf-8'), saved_password):
        return True
    return False

def new_password(saved_password):
    user_attempt_password = input('\nCurrent Password: ')
    new = input('\nNew Password: ')
    if new == '':
        new = 'NULL'
    if check_password(saved_password, user_attempt_password):
        password = bcrypt.hashpw(new.encode('utf-8'), bcrypt.gensalt())
        return password
    else:
        print('\nAttempt does not match password.\n')
        return False


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
sel_admin_id = ''

user_id = ''
first_name = ''
last_name = ''
phone = ''
email = ''
password = ''
hire_date = ''
date_created = ''
role = ''
competency_id = ''
name = ''
description = ''
result_id = ''
assessment_id = ''
score = ''
date_taken = ''
admin_id = ''

activeyn = ''
full_name = ''
saved_password = ''
is_file = ''

query = ''
values = ''

logout_quest = 0
quit_quest = 0
specific_quest = 0
export_users_quest = 0
overwrite_quest = 0


while True:
    if quit_quest == 1:
        break
    print(f'\n{'Welcome!':^20}\n')
    email_login = input('Email: ')
    password_login = input('Password: ')
    

    query = 'SELECT * FROM Users WHERE email = ?'
    values = (email_login,)
    login_attempt = cursor.execute(query, values).fetchone()

    if login_attempt == () or login_attempt == None:
        print('\nLogin Unsuccessful.\nPlease Try Again.\n')
    elif check_password(login_attempt[5], password_login) == False:
        print('\nLogin Unsuccessful.\nPlease Try Again.\n')
    elif login_attempt[9] != 1:
        print('\nLogin Unsuccessful.\nPlease Try Again.\n')
    else:
        logout_quest = 0
        while True:
            if logout_quest == 1:
                break
            elif login_attempt[8].lower() == 'admin':
                user_response = input('''
Main Menu

(1) View Records
(2) Create Records
(3) Edit Records
(4) Search Users
(5) Get Reports
(6) Export CSVs
(7) Import CSVs
(8) Logout
(9) Quit
>>> ''')
                if user_response not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    print('\nInvalid Input.\n')
                elif user_response == '9':
                    logout_quest = 1
                    quit_quest = 1
                elif user_response == '8':
                    logout_quest = 1
                elif user_response == '1':
                    user_response = input('''
Which table would you like to view?

(1) View Users
(2) View Competencies
(3) View Assessments
(4) View Competency Assessment Results
(5) Return to Main Menu
>>> ''')
                    if user_response not in ['1', '2', '3', '4', '5']:
                        print('\nInvalid response.\n')
                    elif user_response == '1':
                        user_response = input('''
(1) View All Users
(2) View All Active Users
(3) View All Inactive Users
(4) Return to Main Menu
>>> ''')
                        if user_response not in ['1', '2', '3', '4']:
                            print('\nInvalid response.\n')
                        elif user_response == '4':
                            continue
                        else:
                            if user_response == '1':
                                rows = cursor.execute('SELECT user_id, first_name, last_name, hire_date, role, email FROM Users').fetchall()
                                if rows == [] or rows == None:
                                    print('\nNo Such Users.\n')
                                    specific_quest = 0
                                elif rows != [] or rows == None:
                                    specific_quest = 1
                                    print(f'\n{'ID':<5}{'Name':<35}{'Hire Date':<15}{'Role':<15}Email\n')
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
                                
                            elif user_response == '2':
                                rows = cursor.execute('SELECT user_id, first_name, last_name, hire_date, role, email FROM Users WHERE active = 1').fetchall()
                                if rows == [] or rows == None:
                                    print('\nNo Such Users')
                                    specific_quest = 0
                                elif rows != [] or rows != None:
                                    specific_quest = 1
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
                                    
                            elif user_response == '3':
                                rows = cursor.execute('SELECT user_id, first_name, last_name, hire_date, role, email FROM Users WHERE active != 1').fetchall()
                                print(rows)
                                if rows == [] or rows == None:
                                    print('\nNo Such Users\n')
                                    specific_quest = 0
                                elif rows != [] or rows != None:
                                    specific_quest = 1
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

                            if specific_quest == 1:
                                if user_response == '':
                                    continue
                                else:
                                    query = 'SELECT * FROM Users WHERE user_id = ?'
                                    value = (user_response,)
                                    row = cursor.execute(query, value).fetchone()
                                    if row == ():
                                        print('\nNo Such User in Database.\n')
                                    elif row != ():
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
                                        

                                        print(f'''
User ID: {row[0]}
First Name: {row[1]}
Last Name: {sel_last_name}
Phone: {sel_phone}
Email: {row[4]}
Hire Date: {sel_hire_date}
Date Created: {sel_date_created}
Role: {row[8]}
Active: {activeyn}''')
                            
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
                            if row == ():
                                print('\nInvalid ID.\n')
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
                        rows = cursor.execute('SELECT * FROM Assessments').fetchall()
                        print(f'\n{'Assessment ID':<15}{'Competency ID':<15}Name')
                        for row in rows:
                            print(f'{row[0]:^15}{row[1]:^15}{row[2]}')
                            
                        user_response = input('\nEnter an ID to View an Assessment\n(Press \'Enter\' to Return to Main Menu.)\n>>> ')

                        if user_response == '':
                            continue
                        else:
                            query = 'SELECT * FROM Assessments where assessment_id = ?'
                            values = user_response

                            row = cursor.execute(query, values).fetchone()
                            if row == ():
                                print('\nInvalid ID.\n')
                            elif row != ():
                                print(f'''
Assessment ID: {row[0]}
Competency ID: {row[1]}
Name: {row [2]}
Date Created: {row[3]}
''')

                    elif user_response == '4':
                        user_response = input('''
(1) View All Assessment Results
(2) View All Results of an Assessment
(3) View All Results of a User
(4) Return to Main Menu
>>> ''')
                        if user_response not in ['1', '2', '3', '4']:
                            print('\nInvalid response.\n')
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
                                    print('\nInvalid ID.\n')
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
                                    print('\nInvalid ID.\n')
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
                                    print('\nInvalid ID.\n')
                                elif row != ():
                                    if row[5] == None:
                                        sel_admin_id = 'n/a'
                                    else:
                                        sel_admin_id = row[5]
                                    print(f'''
Result ID: {row[0]}
User ID: {row[1]}
Assessment ID: {row[2]}
Score: {row[3]}
Date Taken: {row[4]}
Admin ID: {sel_admin_id}
''')
                                

                    print('\n')

                elif user_response == '2':
                    user_response = input('''
(1) Create New User
(2) Create New Competency
(3) Create New Assessment
(4) Create New Competency Assessment Result
(5) Return to Main Menu
>>> ''')
                    if user_response not in ['1', '2', '3', '4', '5']:
                        print('\nInvalid Input.\n')
                    elif user_response == '5':
                        continue
                    elif user_response == '1':
                        print('')

                        first_name = input('First Name: ')
                        last_name = input('Last Name: ')
                        phone = input('Phone: ')
                        email = input('Email: ')
                        password = input('Password: ')
                        hire_date = input('Hire Date (yyyy-mm-dd): ')
                        role = input('Role: (1) User or (2) Admin: ')
                        if first_name == '':
                            print('\nFirst Name Must Not Be Null.')
                            first_name = input('First Name: ')
                        if email == '':
                            print('\nEmail Must Not Be Null.')
                            email = input('Email: ')
                        if password == '':
                            print('\nPassword Must Not Be Null.')
                            password = input('Password: ')
                        if role not in ['1', '2']:
                            print('\nRole Must Be 1 or 2.')
                            role = input('Role: (1) User or (2) Admin: ')
                        if role == '1':
                            role = 'User'
                        elif role == '2':
                            role = 'Admin'
                        if last_name == '':
                            last_name = 'NULL'
                        if phone == '':
                            phone = 'NULL'
                        password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                        query = 'INSERT INTO Users (first_name, last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                        values = (first_name, last_name, phone, email, password, hire_date, today_str, role, 1)
                        if integ(query, values) == True:
                            con.commit()
                        else:
                            print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                    elif user_response == '2':
                        print('')
                        name = input('Name: ')
                        description = input('Description: ')
                        if description == '':
                            description = 'NULL'
                        query = 'INSERT INTO Competencies (name, description) VALUES (?, ?)'
                        values = (name, description)
                        if integ(query, values) == True:
                            con.commit()
                        else:
                            print('\nIntegrity Error: name must not be null.\n')
                    elif user_response == '3':
                        print('')
                        competency_id = input('Competency ID: ')
                        name = input('Name: ')
                        query = 'INSERT INTO Assessments (competency_id, name, date_created) VALUES (?, ?, ?)'
                        values = (competency_id, name, today_str)
                        if integ(query, values) == True:
                            con.commit()
                        else:
                            print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                    elif user_response == '4':
                        print('')
                        user_id = input('User ID: ')
                        assessment_id = input('Assessment ID: ')
                        score = input('Score: ')
                        date_taken = input('Date Taken (yyyy-mm-dd): ')
                        user_response = input('Admin ID: ')
                        count = 0
                        if admin_id == '':
                            admin_id = 'NULL'
                            count = 1
                        elif admin_id != '':
                            admin_id = str_to_int(user_response)
                            if admin_id == False:
                                print('\nInvalid Input.\n')
                            else:
                                rows = cursor.execute('SELECT user_id FROM Users WHERE role = \'Admin\'').fetchall()
                                rows = cursor.execute('SELECT * FROM Users WHERE role = Admin')
                                for row in rows:
                                    if admin_id in row:
                                        count = 1
                        if count != 1:
                            print('\nAdmin ID Does Not Belong to an Admin.\n')
                        elif count == 1:
                            query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score, date_taken, admin_id) VALUES (?, ?, ?, ?, ?)'
                            values = (user_id, assessment_id, score, date_taken, admin_id)
                            if integ(query, values) == True:
                                con.commit()
                            else:
                                print('\nIntegrity Error: please make sure all fields meet their constraints.')
                elif user_response == '3':
                    user_response = input('''
(1) Edit User
(2) Edit Competency
(3) Edit Assessment
(4) Edit Competency Assessment Result
(5) Return to Main Menu
>>> ''')
                    if user_response not in ['1', '2', '3', '4', '5']:
                        print('\nInvalid Input.\n')
                    elif user_response == '5':
                        continue
                    elif user_response == '1':
                        user_response = input('\nPlease Enter the User ID: ')
                        query = 'SELECT * FROM Users WHERE user_id = ?'
                        value = (user_response,)
                        row = cursor.execute(query, value).fetchone()
                        if row == ():
                            print('\nNo Such User in Database.\n')
                        elif row != ():
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
                            
                            print('\nWhat Would You Like to Change?\n')
                            print(f'''
(0) User ID: {row[0]}
(1) First Name: {row[1]}
(2) Last Name: {sel_last_name}
(3) Phone: {sel_phone}
(4) Email: {row[4]}
(5) Password
(6) Hire Date: {sel_hire_date}
(7) Date Created: {sel_date_created}
(8) Role: {row[8]}
(9) Active: {activeyn}''')
                            user_response = input('>>> ')
                            user_id = row[0]
                            saved_password = row[5]
                            if user_response not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                print('\nInvalid Input.\n')
                            elif user_response == '0':
                                query = 'UPDATE Users SET user_id = ? WHERE user_id = ?'
                                user_response = input('\nNew User ID: ')
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '1':
                                query = 'UPDATE Users SET first_name = ? WHERE user_id = ?'
                                user_response = input('\nNew First Name: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '2':
                                query = 'UPDATE Users SET last_name = ? WHERE user_id = ?'
                                user_response = input('\nNew Last Name: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '3':
                                query = 'UPDATE Users SET phone = ? WHERE user_id = ?'
                                user_response = input('\nNew Phone: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '4':
                                query = 'UPDATE Users SET email = ? WHERE user_id = ?'
                                user_response = input('\nNew Email: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query, values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '5':
                                query = 'UPDATE Users SET password = ? WHERE user_id = ?'
                                password = new_password(saved_password)
                                if password != False:
                                    values = (password, user_id)
                                    if integ(query,values) == True:
                                        print('')
                                        con.commit()
                                    else:
                                        print('\nIntegrity Error: please make sure all field meets its constraints.\n')
                            elif user_response == '6':
                                query = 'UPDATE Users SET hire_date = ? WHERE user_id = ?'
                                user_response = input('\nNew Hire Date (yyyy-mm-dd): ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '7':
                                query = 'UPDATE Users SET date_created = ? WHERE user_id = ?'
                                user_response = input('\nNew Date Created (yyyy-mm-dd): ')
                                if user_response == '':
                                    user_response = 'NULL'
                                values = (user_response, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '8':
                                query = 'UPDATE Users SET role = ? WHERE user_id = ?'
                                user_response = input('\n(1) Admin\n(2) User\n>>> ')
                                if user_response == '':
                                    user_response = 'NULL'
                                if user_response not in ['1', '2']:
                                    print('\nInvalid Input.\n')
                                    user_response = input('(1) Admin\n(2) User\n>>> ')
                                else:
                                    if user_response == '1':
                                        values = ('Admin', user_id)
                                    elif user_response == '2':
                                        values = ('User', user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '9':
                                query = 'UPDATE Users SET active = ? WHERE user_id = ?'
                                if activeyn == 'No':
                                    user_response = input('\nReactivate User?\n[Y / N]\n>>> ')
                                    if user_response.lower() not in ['y', 'n']:
                                        print('\nInvalid Input.')
                                    else:
                                        if user_response.lower() == 'y':
                                            values = (1, user_id)
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                                            
                                if activeyn == 'Yes':
                                    user_response = input('\nDeactivate User?\n[Y / N]\n>>> ')
                                    if user_response.lower() not in ['y', 'n']:
                                        print('\nInvalid Input.')
                                    else:
                                        if user_response.lower() == 'y':
                                            values = (0, user_id)
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                                        
                    elif user_response == '2':
                        user_response = input('\nPlease Enter the Competency ID: ')
                        query = 'SELECT * FROM Competencies where competency_id = ?'
                        competency_id = user_response
                        values = (user_response,)
                        row = cursor.execute(query, values).fetchone()
                        if row == () or row == None:
                            print('\nInvalid ID.\n')
                        elif row != () or row != None:
                            description = row[2]
                            if description == None:
                                description = 'n/a'
                            print('\nWhat Would You Like to Change?')
                            user_response = input(f'''
(1) Competency ID: {row[0]}
(2) Name: {row[1]}
(3) Description: {description}
>>> ''')
                            if user_response not in ['1', '2', '3']:
                                print('\nInvalid Input.\n')
                            elif user_response == '1':
                                user_response = input('\nNew Competency ID: ')   
                                query = 'UPDATE Competencies SET competency_id = ?WHERE competency_id = ?'
                                values = (user_response, competency_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '2':
                                user_response = input('\nNew Name: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competencies SET name = ? WHERE competency_id = ?'
                                values = (user_response, competency_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '3':
                                user_response = input('\nNew Description: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competencies SET description = ?'
                                values = (user_response, competency_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')

                    elif user_response == '3':
                        user_response = input('\nPlease Enter the Assessment ID: ')
                        query = 'SELECT * FROM Assessments WHERE assessment_id = ?'
                        values = (user_response,)
                        row = cursor.execute(query, values).fetchone()
                        if row == () or row == None:
                            print('\nInvalid ID.\n')
                        elif row != () or row != None:
                            assessment_id = row[0]
                            print('\nWhat Would You Like To Change?')
                            user_response = input(f'''
(1) Assessment ID: {row[0]}
(2) Competency ID: {row[1]}
(3) Name: {row[2]}
(4) Date Created: {row[3]}
>>> ''')
                            if user_response not in ['1', '2', '3', '4']:
                                print('\nInvalid Input.\n')
                            elif user_response == '1':
                                user_response = input('\nNew Assessment ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Assessments SET assessment_id = ? WHERE assessment_id = ?'
                                values = (user_response, assessment_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '2':
                                user_response = input('\nNew Competency ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Assessments SET competency_id = ? WHERE assessment_id = ?'
                                values = (user_response, assessment_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '3':
                                user_response = input('\nNew Name: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Assessments SET name = ? WHERE assessment_id = ?'
                                values = (user_response, assessment_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '4':
                                user_response = input('\nNew Date Created (yyyy-mm-dd): ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Assessments SET assessment_id = ? WHERE assessment_id = ?'
                                values = (user_response, assessment_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')

                    elif user_response == '4': 
                        user_response = input('\nPlease Enter the Result ID: ')
                        query = 'SELECT * FROM Competency_Assessment_Results WHERE result_id = ?'
                        values = (user_response,)
                        row = cursor.execute(query, values).fetchone()
                        if row == () or row == None:
                            print('\nInvalid ID.\n')
                        elif row != () or row != None:
                            result_id = row[0]
                            admin_id = row[5]
                            if admin_id == None:
                                admin_id = 'n/a'
                            print('\nWhat Would You Like To Change?')
                            user_response = input(f'''
(1) Result ID: {row[0]}
(2) User ID: {row[1]}
(3) Assessment ID: {row[2]}
(4) Score: {row[3]}
(5) Date Taken: {row[4]}
(6) Admin Id: {row[5]}
>>> ''')
                            if user_response not in ['1', '2', '3', '4', '5', '6']:
                                print('\nInvalid Input.\n')
                            elif user_response == '1':
                                user_response = input('\nNew Result ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competency_Assessment_Results SET result_id = ? WHERE result_id = ?'
                                values = (user_response, result_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '2':
                                user_response = input('\nNew User ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competency_Assessment_Results SET user_id = ? WHERE result_id = ?'
                                values = (user_response, result_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '3':
                                user_response = input('\nNew Assessment ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competency_Assessment_Results SET assessment_id = ? WHERE result_id = ?'
                                values = (user_response, result_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '4':
                                user_response = input('\nNew Score: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competency_Assessment_Results SET score = ? WHERE result_id = ?'
                                values = (user_response, result_id)
                                if score not in ['0', '1', '2', '3', '4']:
                                    print('\nScore Must Be 0-4.\n')
                                else:
                                    if integ(query,values) == True:
                                        print('')
                                        con.commit()
                                    else:
                                        print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '5':
                                user_response = input('\nNew Date Taken (yyyy-mm-dd): ')
                                if user_response == '':
                                    user_response = 'NULL'
                                query = 'UPDATE Competency_Assessment_Results SET date_taken = ? WHERE result_id = ?'
                                values = (user_response, result_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')
                            elif user_response == '6':
                                user_response = input('\nNew Admin ID: ')
                                if user_response == '':
                                    user_response = 'NULL'
                                rows = cursor.execute('SELECT user_id FROM Users WHERE role = \'Admin\'').fetchall()
                                admin_id = str_to_int(user_response)
                                if admin_id == False:
                                    print('\nInvalid Input.\n')
                                else:
                                    rows = cursor.execute('SELECT * FROM Users WHERE role = Admin')
                                    count = 0
                                    for row in rows:
                                        if admin_id in row:
                                            count = 1
                                    if count != 1:
                                        print('\nID Does Not Belong to an Admin.\n')
                                    elif count == 1:
                                        query = 'UPDATE Competency_Assessment_Results SET admin_id = ? WHERE result_id = ?'
                                        values = (user_response, result_id)
                                        if integ(query,values) == True:
                                            print('')
                                            con.commit()
                                        else:
                                            print('\nIntegrity Error: please make sure field meets its constraints.\n')

                elif user_response == '4':
                    print('\nSearching Users By First OR Last Name...')
                    user_response = input('Search: ')
                    query = 'SELECT user_id, first_name, last_name, hire_date, role, email FROM Users WHERE first_name LIKE ? or last_name LIKE ?'
                    values = (f'%{user_response}%', f'%{user_response}%')
                    rows = cursor.execute(query,values).fetchall()
                    if rows == () or rows == None:
                        print('\nNo Users Found.\n')
                    elif rows != () or rows != None:
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
                            query = 'SELECT * FROM Users WHERE user_id = ?'
                            value = (user_response,)
                            row = cursor.execute(query, value).fetchone()
                            if row == ():
                                print('\nNo Such User in Database.\n')
                            elif row != ():
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
                                

                                print(f'''
User ID: {row[0]}
First Name: {row[1]}
Last Name: {sel_last_name}
Phone: {sel_phone}
Email: {row[4]}
Hire Date: {sel_hire_date}
Date Created: {sel_date_created}
Role: {row[8]}
Active: {activeyn}

''')
                elif user_response == '5':
                    user_response = input('''
(1) Get User Competency Summary
(2) Get Competency Results Summary
(3) Return to Main Menu
>>> ''')
                    if user_response not in ['1', '2', '3']:
                        print('\nInvalid Input.\n')
                    elif user_response == '3':
                        continue
                    elif user_response == '1':
                        user_response = input('\nPlease Enter a User ID: ')
                        query = 'SELECT * FROM Users WHERE user_id = ?'
                        values = (user_response,)
                        row = cursor.execute(query, values).fetchone()
                        if row == ():
                            print('\nInvalid ID.\n')
                        elif row != ():
                            query = 'SELECT c.competency_id as competency_id, c.name as competency_name, result_id, score, MAX(date_taken) as date_taken, admin_id, u.user_id as user_id, first_name, last_name, email FROM Competencies as c JOIN Assessments as a ON a.competency_id = c.competency_id JOIN Competency_Assessment_Results as car ON a.assessment_id = car.assessment_id JOIN Users as u ON u.user_id = car.user_id WHERE u.user_id = ? GROUP BY competency_name ORDER BY c.competency_id'
                            values = (user_response,)
                            rows = cursor.execute(query, values).fetchall()
                            count = 0
                            total = 0
                            divider = 0
                            for row in rows:
                                full_name = f'{row[7]} {row[8]}'
                                if count == 0:
                                    count = 1
                                    user_id = row[6]
                                    print(f'\nName: {full_name}\nUser ID: {row[6]}\nEmail: {row[9]}\n')
                                    print(f'{'Competency ID':<15}{'Competency Name':<20}{'Result ID':<12}{'Score':<8}Date Taken\n')
                                total += int(row[3])
                                divider += 1   
                                print(f'{row[0]:<15}{row[1]:<20}{row[2]:<12}{row[3]:<8}{row[4]}')
                            average = total / divider
                            print(f'\nAverage Score: {round(average, 2)}\n')
                                    

                    elif user_response == '2':
                        user_response = input('\nPlease Enter a Competency ID: ')
                        query = 'SELECT name from Competencies where competency_id = ?'
                        values = (user_response,)
                        row = cursor.execute(query, values).fetchone()
                        if row == ():
                            print('\nInvalid Competency ID.\n')
                        elif row != ():
                            query = 'SELECT u.user_id as user_id, first_name, last_name, a.name as assessment_name, score, date_taken FROM Assessments a JOIN Competency_Assessment_Results car ON car.assessment_id = a.assessment_id AND a.competency_id = ? RIGHT JOIN Users u ON u.user_id = car.user_id GROUP BY u.user_id ORDER BY u.user_id ASC, date_taken DESC'
                            rows = cursor.execute(query, values).fetchall()
                            print(f'\n{row[0]}\n\n{'User ID':<9}{'Name':<25}{'Assessment Name':<33}{'Score':<8}Date Taken\n')
                            for row in rows:
                                full_name = f'{row[1]} {row[2]}'
                                assessment_name = row[3]
                                score = row[4]
                                date_taken = row[5]

                                if assessment_name == None:
                                    assessment_name = 'n/a'
                                if score == None:
                                    score = 'n/a'
                                if date_taken == None:
                                    date_taken = 'n/a'

                                print(f'{row[0]:<9}{full_name:<25}{assessment_name:<33}{score:<8}{date_taken}')
                            print('')

                elif user_response == '6':
                    user_response = input('''
(1) Export User Assessment Results
(2) Export Competency Assessment Results
(3) Export Users
(4) Export Competencies
(5) Export Assessments
(6) Return to Main Menu
>>> ''')
                    if user_response not in ['1', '2', '3', '4', '5', '6']:
                        print('\nInvalid Input.\n')
                    elif user_response == '6':
                        continue
                    elif user_response == '1':
                        user_response = input('\nUser ID: ')
                        overwrite_quest = 0
                        query = 'SELECT * FROM Competency_Assessment_Results WHERE user_id = ?'
                        values = (user_response,)
                        rows = cursor.execute(query, values).fetchall()
                        file_name = input('\nFile Name: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                        is_file = os.path.isfile(file_name)
                        if is_file == True:
                            print('\nFile With This Name Already Exists.\n')
                            user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                            if user_response not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                overwrite_quest = 1
                            elif user_response.lower() == 'n':
                                overwrite_quest = 0
                                continue
                        elif is_file != True:
                            overwrite_quest = 1
                        if overwrite_quest == 1:
                            user_response = input('\nExport With Result ID? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                    for row in rows:
                                        if row[5] == None:
                                            admin_id = ''
                                        elif row[5] != None:
                                            admin_id = row[5]
                                        data = [row[0], row[1], row[2], row[3], row[4], admin_id]
                                        writer.writerow(data)
                            elif user_response.lower() == 'n':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                    for row in rows:
                                        if row[5] == None:
                                            admin_id = ''
                                        elif row[5] != None:
                                            admin_id = row[5]
                                        data = [row[1], row[2], row[3], row[4], admin_id]
                                        writer.writerow(data)
                    elif user_response == '2':
                        user_response = input('\nCompetency ID: ')
                        overwrite_quest = 0
                        query = 'SELECT result_id, user_id, car.assessment_id, score, date_taken, admin_id FROM Competency_Assessment_Results car JOIN Assessments a ON car.assessment_id = a.assessment_id WHERE competency_id = ?'
                        values = (user_response,)
                        rows = cursor.execute(query, values).fetchall()
                        file_name = input('\nFile Name: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                        is_file = os.path.isfile(file_name)
                        if is_file == True:
                            print('\nFile With This Name Already Exists.\n')
                            user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                            if user_response not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                overwrite_quest = 1
                            elif user_response.lower() == 'n':
                                overwrite_quest = 0
                                continue
                        elif is_file != True:
                            overwrite_quest = 1
                        if overwrite_quest == 1:
                            user_response = input('\nExport With Result ID? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                    for row in rows:
                                        if row[5] == None:
                                            admin_id = ''
                                        elif row[5] != None:
                                            admin_id = row[5]
                                        data = [row[0], row[1], row[2], row[3], row[4], admin_id]
                                        writer.writerow(data)
                            elif user_response.lower() == 'n':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                    for row in rows:
                                        if row[5] == None:
                                            admin_id = ''
                                        elif row[5] != None:
                                            admin_id = row[5]
                                        data = [row[1], row[2], row[3], row[4], admin_id]
                                        writer.writerow(data)
                    elif user_response == '3':
                        overwrite_quest = 0
                        query = 'SELECT * FROM Users'
                        rows = cursor.execute(query).fetchall()
                        file_name = input('\nFile Name: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                        is_file = os.path.isfile(file_name)
                        if is_file == True:
                            print('\nFile With This Name Already Exists.\n')
                            user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                            if user_response not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                overwrite_quest = 1
                            elif user_response.lower() == 'n':
                                overwrite_quest = 0
                                continue
                        elif is_file != True:
                            overwrite_quest = 1
                        if overwrite_quest == 1:
                            user_response = input('\nExport With User ID? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['user_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active'])
                                    for row in rows:
                                        if row[2] == None:
                                            last_name = ''
                                        elif row[2] != None:
                                            last_name = row[2]
                                        if row[3] == None:
                                            phone = ''
                                        elif row[3] != None:
                                            phone = row[3]
                                        if row[6] == None:
                                            hire_date = ''
                                        elif row[6] != None:
                                            hire_date = row[6]
                                        if row[7] == None:
                                            date_created = ''
                                        elif row[7] != None:
                                            date_created = row[7]
                                        if row[9] == None:
                                            active = 0
                                        elif row[9] != None:
                                            active = row[9]
                                        data = [row[0], row[1], last_name, phone, row[4], row[5], hire_date, date_created, row[8], active]
                                        writer.writerow(data)
                            elif user_response.lower() == 'n':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active'])
                                    for row in rows:
                                        if row[2] == None:
                                            last_name = ''
                                        elif row[2] != None:
                                            last_name = row[2]
                                        if row[3] == None:
                                            phone = ''
                                        elif row[3] != None:
                                            phone = row[3]
                                        if row[6] == None:
                                            hire_date = ''
                                        elif row[6] != None:
                                            hire_date = row[6]
                                        if row[7] == None:
                                            date_created = ''
                                        elif row[7] != None:
                                            date_createde = row[7]
                                        if row[9] == None:
                                            active = 0
                                        elif row[9] != None:
                                            active = row[9]
                                        data = [row[1], last_name, phone, row[4], row[5], hire_date, date_created, row[8], active]
                                        writer.writerow(data)
                    elif user_response == '4':
                        overwrite_quest = 0
                        query = 'SELECT * FROM Competencies'
                        rows = cursor.execute(query).fetchall()
                        file_name = input('\nFile Name: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                        is_file = os.path.isfile(file_name)
                        if is_file == True:
                            print('\nFile With This Name Already Exists.\n')
                            user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                            if user_response not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                overwrite_quest = 1
                            elif user_response.lower() == 'n':
                                overwrite_quest = 0
                                continue
                        elif is_file != True:
                            overwrite_quest = 1
                        if overwrite_quest == 1:
                            user_response = input('\nExport With Competency ID? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['competency_id', 'name', 'description'])
                                    for row in rows:
                                        if row[2] == None:
                                            description = ''
                                        elif row[2] != None:
                                            description = row[2]
                                        data = [row[0], row[1], description]
                                        writer.writerow(data)
                            elif user_response.lower() == 'n':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['name', 'description'])
                                    for row in rows:
                                        if row[2] == None:
                                            description = ''
                                        elif row[2] != None:
                                            description = row[2]
                                        data = [row[1], description]
                                        writer.writerow(data)
                    elif user_response == '5':
                        overwrite_quest = 0
                        query = 'SELECT * FROM Assessments'
                        rows = cursor.execute(query).fetchall()
                        file_name = input('\nFile Name: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                        is_file = os.path.isfile(file_name)
                        if is_file == True:
                            print('\nFile With This Name Already Exists.\n')
                            user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                            if user_response not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                overwrite_quest = 1
                            elif user_response.lower() == 'n':
                                overwrite_quest = 0
                                continue
                        elif is_file != True:
                            overwrite_quest = 1
                        if overwrite_quest == 1:
                            user_response = input('\nExport With Assessment ID? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y', 'n']:
                                print('\nInvalid Input.\n')
                            elif user_response.lower() == 'y':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['assessment_id', 'competency_id', 'name', 'date_created'])
                                    for row in rows:
                                        data = [row[0], row[1], row[2], row[3]]
                                        writer.writerow(data)
                            elif user_response.lower() == 'n':
                                with open(file_name, 'w', newline='') as write_file:
                                    writer = csv.writer(write_file)
                                    writer.writerow(['competency_id', 'name', 'date_created'])
                                    for row in rows:
                                        data = [row[1], row[2], row[3]]
                                        writer.writerow(data)
                elif user_response == '7':
                    user_response = input('''
(1) Import Into Users
(2) Import Into Competencies
(3) Import Into Assessments
(4) Import Into Competency Assessment Results
(5) Return to Main Menu
>>> ''')
                    if user_response == '5':
                        continue
                    elif user_response == '1':
                        file_name = input('\nPlease Enter the CSV File You Would Like to Import: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                            print('')
                        is_file = os.path.isfile(file_name)
                        if is_file != True:
                            print('\nNo CSV File by That Name.\n')
                        elif is_file == True:
                            with open(file_name, 'r') as read_file:
                                csvreader = csv.reader(read_file)
                                header = next(csvreader)
                                if header != ['user_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active'] and header != ['first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active']:
                                    print('\nHeader Must Be user_id,first_namelast_name,phone,email,password,hire_date,date_created,role,active\nor\nfirst_namelast_name,phone,email,password,hire_date,date_created,role,active\n')
                                elif header == ['user_id', 'first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active']:
                                    query = 'INSERT INTO Users (user_id, first_name,last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
                                    user_response = input('\nAre Passwords Already Encrypted? [Y / N]\n>>> ')
                                    if user_response.lower() == 'n':
                                        for row in csvreader:
                                            password = bcrypt.hashpw(row[5].encode('utf-8'), bcrypt.gensalt())
                                            values = (row[0], row[1], row[2], row[3], row[4], password, row[6], row[7], row[8], row[9])
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {password}, {row[6]}, {row[5]}, {row[7]}, {row[8]}] Raised an Integrity Error.\n')
                                    elif user_response.lower() == 'y':
                                        for row in csvreader:
                                            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}] Raised an Integrity Error.\n')

                                elif header == ['first_name', 'last_name', 'phone', 'email', 'password', 'hire_date', 'date_created', 'role', 'active']:
                                    query = 'INSERT INTO Users (first_name,last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
                                    user_response = input('\nAre Passwords Already Encrypted? [Y / N]\n>>> ')
                                    if user_response.lower() == 'n':
                                        for row in csvreader:
                                            password = bcrypt.hashpw(row[5].encode('utf-8'), bcrypt.gensalt())
                                            values = (row[0], row[1], row[2], row[3], password, row[5], row[6], row[7], row[8])
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {password}, {row[6]}, {row[7]}, {row[8]}, {row[9]}] Raised an Integrity Error.\n')
                                    elif user_response.lower() == 'y':
                                        for row in csvreader:
                                            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                                            if integ(query, values) == True:
                                                con.commit()
                                            else:
                                                print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}] Raised an Integrity Error.\n')
                    elif user_response == '2':
                        file_name = input('\nPlease Enter the CSV File You Would Like to Import: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                            print('')
                        is_file = os.path.isfile(file_name)
                        if is_file != True:
                            print('\nNo CSV File by That Name.\n')
                        elif is_file == True:
                            with open(file_name, 'r') as read_file:
                                csvreader = csv.reader(read_file)
                                header = next(csvreader)
                                if header != ['competency_id', 'name', 'description'] and header != ['name', 'description']:
                                    print('\nHeader Must Be competecny_id,name,description\nor\nname,description\n')
                                elif header == ['competency_id', 'name', 'description']:
                                    query = 'INSERT INTO Competencies (competecny_id, name, description) VALUES (?, ?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1], row[2])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}, {row[2]}] Raised an Integrity Error.\n')

                                elif header == ['name', 'description']:
                                    query = 'INSERT INTO Competencies (name, description) VALUES (?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}] Raised an Integrity Error.\n')
                    elif user_response == '3':
                        file_name = input('\nPlease Enter the CSV File You Would Like to Import: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                            print('')
                        is_file = os.path.isfile(file_name)
                        if is_file != True:
                            print('\nNo CSV File by That Name.\n')
                        elif is_file == True:
                            with open(file_name, 'r') as read_file:
                                csvreader = csv.reader(read_file)
                                header = next(csvreader)
                                if header != ['assessment_id', 'competency_id', 'name', 'date_created'] and header != ['competency_id', 'name', 'date_created']:
                                    print('\nHeader Must Be assessment_id,competency_id,name,date_created\nor\ncompetency_id,name,date_created\n')
                                elif header == ['assessment_id', 'competency_id', 'name', 'date_created']:
                                    query = 'INSERT INTO Assessments (assessment_id, competency_id, name, date_created) VALUES (?, ?, ?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1], row[2], row[3])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}] Raised an Integrity Error.\n')

                                elif header == ['competency_id', 'name', 'date_created']:
                                    query = 'INSERT INTO Competency_Assessment_Results (competency_id, name, date_created) VALUES (?, ?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1], row[2])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}] Raised an Integrity Error.\n')
                    elif user_response == '4':
                        file_name = input('\nPlease Enter the CSV File You Would Like to Import: ')
                        if '.csv' not in file_name:
                            file_name += '.csv'
                            print('')
                        is_file = os.path.isfile(file_name)
                        if is_file != True:
                            print('\nNo CSV File by That Name.\n')
                        elif is_file == True:
                            with open(file_name, 'r') as read_file:
                                csvreader = csv.reader(read_file)
                                header = next(csvreader)
                                print(header)
                                if header != ['user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'] and header != ['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'admin_id']:
                                    print('\nHeader Must Be user_id,assessment_id,score,date_taken,admin_id\nor\nresult_id,user_id,assessment_id,score,date_taken,admin_id\n')
                                elif header == ['user_id', 'assessment_id', 'score', 'date_taken', 'admin_id']:
                                    query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score, date_taken, admin_id) VALUES (?, ?, ?, ?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1], row[2], row[3], row[4])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}] Raised an Integrity Error.\n')

                                elif header == ['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'admin_id']:
                                    query = 'INSERT INTO Competency_Assessment_Results (result_id, user_id, assessment_id, score, date_taken, admin_id) VALUES (?, ?, ?, ?, ?, ?)'
                                    for row in csvreader:
                                        values = (row[0], row[1], row[2], row[3], row[4], row[5])
                                        if integ(query, values) == True:
                                            con.commit()
                                        else:
                                            print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}] Raised an Integrity Error.\n')


            elif login_attempt[8].lower() == 'user':
                user_id = login_attempt[0]
                user_response = input('''
What Would You Like To Do?
(1) View Your Profile
(2) Edit Your Profile
(3) View Your User Competency Summary
(4) Logout
(5) Quit
>>> ''')
                if user_response not in ['1', '2', '3', '4', '5']:
                    print('\nInvalid Input.\n')
                elif user_response == '5':
                    logout_quest = 1
                    quit_quest = 1
                elif user_response == '4':
                    logout_quest = 1
                elif user_response == '1':
                    query = 'SELECT * FROM Users WHERE user_id = ?'
                    value = (user_id,)
                    row = cursor.execute(query, value).fetchone()
                    if row == ():
                        print('\nNo Such User in Database.\n')
                    elif row != ():
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
                        

                        print(f'''
User ID: {row[0]}
First Name: {row[1]}
Last Name: {sel_last_name}
Phone: {sel_phone}
Email: {row[4]}
Hire Date: {sel_hire_date}
Date Created: {sel_date_created}
Role: {row[8]}
Active: {activeyn}
''')
               
                elif user_response == '2':
                    query = 'SELECT * FROM Users WHERE user_id = ?'
                    value = (user_id,)
                    row = cursor.execute(query, value).fetchone()
                    if row == ():
                        print('\nNo Such User in Database.\n')
                    elif row != ():
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
                        
                        print('\nWhat Would You Like to Change?')
                        print(f'''
(1) First Name: {row[1]}
(2) Last Name: {sel_last_name}
(3) Phone: {sel_phone}
(4) Email: {row[4]}
(5) Password''')
                        user_response = input('>>> ')
                        saved_password = row[5]
                        query = 'UPDATE Users SET first_name = ? WHERE user_id = ?'
                        if user_response == '1':
                            user_response = input('\nNew First Name: ')
                            values = (user_response, user_id)
                            if integ(query,values) == True:
                                print('')
                                con.commit()
                            else:
                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                        elif user_response == '2':
                            query = 'UPDATE Users SET last_name = ? WHERE user_id = ?'
                            user_response = input('\nNew Last Name: ')
                            values = (user_response, user_id)
                            if integ(query,values) == True:
                                print('')
                                con.commit()
                            else:
                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                        elif user_response == '3':
                            query = 'UPDATE Users SET phone = ? WHERE user_id = ?'
                            user_response = input('\nNew Phone: ')
                            values = (user_response, user_id)
                            if integ(query,values) == True:
                                print('')
                                con.commit()
                            else:
                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                        elif user_response == '4':
                            query = 'UPDATE Users SET email = ? WHERE user_id = ?'
                            user_response = input('\nNew Email: ')
                            values = (user_response, user_id)
                            if integ(query, values) == True:
                                con.commit()
                            else:
                                print('\nIntegrity Error: please make sure field meets its constraints.\n')
                        elif user_response == '5':
                            query = 'UPDATE Users SET password = ? WHERE user_id = ?'
                            password = new_password(saved_password)
                            if password != False:
                                values = (password, user_id)
                                if integ(query,values) == True:
                                    print('')
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all field meets its constraints.\n')
                elif user_response == '3':
                    query = 'SELECT * FROM Users WHERE user_id = ?'
                    values = (user_id,)
                    row = cursor.execute(query, values).fetchone()
                    
                    if row != ():
                        query = 'SELECT c.competency_id as competency_id, c.name as competency_name, result_id, score, MAX(date_taken) as date_taken, admin_id, u.user_id as user_id, first_name, last_name, email FROM Competencies as c JOIN Assessments as a ON a.competency_id = c.competency_id JOIN Competency_Assessment_Results as car ON a.assessment_id = car.assessment_id JOIN Users as u ON u.user_id = car.user_id WHERE u.user_id = ? GROUP BY competency_name ORDER BY c.competency_id'
                        values = (user_response,)
                        rows = cursor.execute(query, values).fetchall()
                        count = 0
                        total = 0
                        divider = 0
                        for row in rows:
                            full_name = f'{row[7]} {row[8]}'
                            if count == 0:
                                count = 1
                                user_id = row[6]
                                print(f'\nName: {full_name}\nUser ID: {row[6]}\nEmail: {row[9]}\n')
                                print(f'{'Competency ID':<15}{'Competency Name':<20}{'Result ID':<12}{'Score':<8}Date Taken\n')
                            total += int(row[3])
                            divider += 1   
                            print(f'{row[0]:<15}{row[1]:<20}{row[2]:<12}{row[3]:<8}{row[4]}')
                        average = total / divider
                        print(f'\nAverage Score: {round(average, 2)}\n')

                        user_response = input('\nExport as CSV? [Y / N]\n>>> ')
                        if user_response.lower() not in ['y', 'n']:
                            print('\nInvalid Input.')
                        elif user_response.lower() == 'n':
                            continue
                        elif user_response.lower() == 'y':
                            query = 'SELECT * FROM Competency_Assessment_Results WHERE user_id = ?'
                            values = (user_id,)
                            rows = cursor.execute(query, values).fetchall()
                            file_name = input('\nFile Name: ')
                            if '.csv' not in file_name:
                                file_name += '.csv'
                            is_file = os.path.isfile(file_name)
                            if is_file == True:
                                print('\nFile With This Name Already Exists.\n')
                                user_response = input(f'Overwrite Current {file_name}? [Y / N]\n>>> ')
                                if user_response not in ['y', 'n']:
                                    print('\nInvalid Input.\n')
                                elif user_response.lower() == 'y':
                                    overwrite_quest = 1
                                elif user_response.lower() == 'n':
                                    continue
                            elif is_file != True:
                                overwrite_quest = 1
                            if overwrite_quest == 1:
                                user_response = input('\nExport With Result ID? [Y / N]\n>>> ')
                                if user_response.lower() not in ['y', 'n']:
                                    print('\nInvalid Input.\n')
                                elif user_response.lower() == 'y':
                                    with open(file_name, 'w', newline='') as write_file:
                                        writer = csv.writer(write_file)
                                        writer.writerow(['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                        for row in rows:
                                            if row[5] == None:
                                                admin_id = ''
                                            elif row[5] != None:
                                                admin_id = row[5]
                                            data = [row[0], row[1], row[2], row[3], row[4], admin_id]
                                            writer.writerow(data)
                                elif user_response.lower() == 'n':
                                    with open(file_name, 'w', newline='') as write_file:
                                        writer = csv.writer(write_file)
                                        writer.writerow(['user_id', 'assessment_id', 'score', 'date_taken', 'admin_id'])
                                        for row in rows:
                                            if row[5] == None:
                                                admin_id = ''
                                            elif row[5] != None:
                                                admin_id = row[5]
                                            data = [row[1], row[2], row[3], row[4], admin_id]
                                            writer.writerow(data)