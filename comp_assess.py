import sqlite3
import bcrypt
from datetime import date
import csv
import os


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
sel_manager_id = ''

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
manager_id = ''

activeyn = ''
full_name = ''

query = ''
values = ''

break_quest = 0
logout_quest = 0
quit_quest = 0


while True:
    if quit_quest == 1:
        break
    print(f'{'Welcome!':^20}\n')
    email_login = input('Email: ')
    password_login = input('Password: ')

    query = 'SELECT * FROM Users WHERE email = ? AND password = ?'
    values = (email_login, password_login)

    login_attempt = cursor.execute(query, values).fetchone()

    if login_attempt == () or login_attempt[9] != 1:
        print('\nLogin Unsuccessful.\nPlease Try Again.\n')
    else:
        logout_quest = 0
        
        user1 = User('','','','','','','')
        user1.load(login_attempt[0])

        while True:
            if logout_quest == 1:
                break
            if user1.role.lower() == admin:
                user_response = input('''
What Would You Like To Do?
(1) View Records
(2) Create Records
(3) Edit Records
(4) Search Users
(5) Get User Competency Summary
(6) Get Competency Results Summary
(7) Import Competency Assessment Results
(8) Logout
(9) Quit
>>> ''')
                print('')
                if user_response not in ['1','2','3','4','5','6','7','8', '9']:
                    print('Please Enter a Valid Input.\n')
                elif user_response == '9':
                    logout_quest = 1
                    quit_quest = 1
                elif user_response == '8':
                    logout_quest = 1
                elif user_response == '1':
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
                                query = 'SELECT * FROM Users WHERE user_id = ?'
                                value = (user_response,)
                                row = cursor.execute(query, value).fetchone()
                                if row == ():
                                    print('No Such User in Database.')
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
                                    

                                    print('''User ID: {row[0]}
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
                            if row = ():
                                print('\nPlease Enter a Valid ID.\n')
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

                elif user_response == '2':
                    user_response = input('''
(1) Create New User
(2) Create New Competency
(3) Create New Assessment
(4) Create New Competency Assessment Result
(5) Return to Main Menu
>>> ''')
                    if user_response not in ['1','2','3','4','5']:
                        print('\nPlease Enter a Valid Input.\n')
                    elif user_response == '5':
                        continue
                    elif user_response == '1':
                        print('')

                        first_name = input('First Name: ')
                        last_name = input('Last Name: ')
                        phone = input('Phone: ')
                        email = input('Email: ')
                        password = input('Password: ')
                        hire_date = input('Hire Date: ')
                        role = input('Role: (1) User or (2) Admin: ')
                        while True:
                            if first_name == '':
                                print('\nFirst Name Must Not Be Null.')
                                first_name = input('First Name: ')
                            elif email == '':
                                print('\nEmail Must Not Be Null.')
                                email = input('Email: ')
                            elif password == '':
                                print('\nPassword Must Not Be Null.')
                                password = input('Password: ')
                            elif role not in ['1','2']:
                                print('\nRole Must Be 1 or 2.')
                                role = input('Role: (1) User or (2) Admin: ')
                            else:
                                break
                        if role == '1':
                            role = 'User'
                        elif role == '2':
                            role = 'Admin'
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
                        query = 'INSERT INTO Competencies (name, description) VALUES (?, ?)'
                        values = (name, description)
                        if integ(query, values) == True:
                            con.commit()
                        else:
                            print('\nIntegrity Error: name must not be null.\n')
                    elif user_response == '3':
                        competency_id = input('Competency ID: ')
                        name = input('Name: ')
                        query = 'INSERT INTO Assessments (competency_id, name, date_created) VALUES (?, ?, ?)'
                        values = (competency_id, name, today_str)
                        if integ(query, values) == True:
                            con.commit()
                        else:
                            print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                        elif user_response == '4':
                        user_id = input('User ID: ')
                        assessment_id = input('Assessment ID: ')
                        score = input('Score: ')
                        date_taken = input('Date Taken: ')
                        manager_id = input('Manager ID: ')
                        query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score, date_taken, manager_id) VALUES (?, ?, ?, ?, ?)'
                        values = (user_id, assessment_id, score, date_taken, manager_id)
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
                        print('\nPlease Enter a Valid Input.\n')
                    elif user_response == '5':
                        continue
                    elif user_response == '1':
                        user_response = input('\nPlease Enter the User ID: ')
                        query = 'SELECT * FROM Users WHERE user_id = ?'
                        value = (user_response,)
                        row = cursor.execute(query, value).fetchone()
                        if row == ():
                            print('No Such User in Database.')
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
                            
                            print('What Would You Like to Change?')
                            print('''(0) User ID: {row[0]}
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
                            query = 'UPDATE Users SET ? = ? WHERE user_id = ?'
                            if user_response not in ['0','1','2','3','4','5','6','7','8','9']:
                                print('\nPlease Enter a Valid Input.\n')
                            elif user_response == '0':
                                user_response = input('\nNew User ID: ')
                                values = ('user_id', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '1':
                                user_response = input('\nNew First Name: ')
                                values = ('first_name', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '2':
                                user_response = input('\nNew Last Name: ')
                                values = ('last_name', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '3':
                                user_response = input('\nNew Phone: ')
                                values = ('phone', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '4':
                                user_response = input('\nNew Email: ')
                                values = ('email', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '5':
                                password = new_password(saved_password)
                                if password != False:
                                    values = ('password', password, user_id)
                                    if integ(query,values) == True:
                                        con.commit()
                                    else:
                                        print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '6':
                                user_response = input('\nNew Hire Date: ')
                                values = ('hire_date', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '7':
                                user_response = input('\nNew Date Created: ')
                                values = ('date_created', user_response, user_id)
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure all fields meet their constraints.\n')
                            elif user_response == '8':
                                user_response = input('\n(1) Admin\n(2) User\n>>> ')
                                while True:
                                    if user_response not in ['1','2']:
                                        print('\nPlease Enter a Valid Input.')
                                        user_response = input('(1) Admin\n(2) User\n>>> ')
                                    else:
                                        if user_response == '1':
                                            values = ('role', 'Admin', user_id)
                                        elif user_response == '2':
                                            values = ('role', 'User', user_id)
                                        break
                                if integ(query,values) == True:
                                    con.commit()
                                else:
                                    print('\nIntegrity Error: please make sure field meets its constraints.\n')

                            elif user_response == '1'

                elif user_response == '4':
                    print('\nSearching Users By Name...')
                    user_response = input('Search: ')
                    query = 'SELECT user_id, first_name, last_name, date_hired, role, email FROM Users WHERE first_name LIKE ? or last_name LIKE ?'
                    values = (f'%{user_response}%', f'%{user_response}%')
                    rows = cursor.execute(query,values).fetchall()
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
                            print('No Such User in Database.')
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
                            

                            print('''User ID: {row[0]}
First Name: {row[1]}
Last Name: {sel_last_name}
Phone: {sel_phone}
Email: {row[4]}
Hire Date: {sel_hire_date}
Date Created: {sel_date_created}
Role: {row[8]}
Active: {activeyn}

''')'
                elif user_response == '5':
                    user_response = input('\nPlease Enter a User ID: ')
                    query = 'SELECT * FROM Users WHERE user_id = ?'
                    values = (user_response,)
                    row = cursor.execute(query, values).fetchone()
                    if row == ():
                        print('\nPlease Enter a Valid ID.\n')
                    elif row != ():
                        query = 'SELECT c.competency_id as competency_id, c.name as competency_name, result_id, score, date_taken, manager_id, u.user_id as user_id, first_name, last_name, email FROM Competencies as c JOIN Assessments as a ON a.competency_id = c.competency_id JOIN Competency_Assessment_Results as car ON a.assessment_id = car.assessment_id JOIN Users as u ON u.user_id = car.user_id WHERE u.user_id = ? GROUP BY competency_name ORDER BY c.competency_id, date_taken DESC'
                        values = (user_response,)
                        rows = cursor.execute(query, values).fetchall()
                        count = 0
                        total = 0
                        divider = 0
                        for row in rows:
                            full_name = f'{row[7]} {row[8]}'
                            if count = 0:
                                count = 1
                                user_id = row[6]
                                print(f'Name: {full_name}\nUser ID: {row[6]}\nEmail: {row[9]}\n')
                                print(f'{'Competency ID':<15}{'Competency Name':<20}{'Result ID':<12}{'Score':<8}Date Taken')
                            total += int(row[3])
                            divider += 1   
                            print(f'{row[0]:<15}{row[1]:<20}{row[2]:<12}{row[3]:<8}{row[4]}')
                        average = total / divider
                        print(f'\nAverage Score: {round(average, 2)}\n')
                        while True:
                            user_response = input('\nExport as CSV? [Y / N]\n>>> ')
                            if user_response.lower() not in ['y','n']:
                                print('\nInvalid Input.')
                            elif user_response.lower() == 'n':
                                break
                            elif user_response.lower() == 'y':
                                query = 'SELECT * FROM Competency_Assessment_Results WHERE user_id = ?'
                                values = (user_id,)
                                rows = cursor.execute(query, values).fetchall()
                                file_name = input('\nFile Name: ')
                                if '.csv' not in file_name:
                                    file_name += '.csv'
                                if os.path.isfile(file_name) == True:
                                    print('\nFile With This Name Already Exists.\n')
                                user_response = input('Export With Result ID? [Y / N]\n>>> ')
                                if user_response.lower() not in ['y', 'n']:
                                    print('\nInvalid Input.\n')
                                elif user_response.lower() == 'y':
                                    with open(file_name, 'w', newline='') as write_file:
                                        writer = csv.writer(write_file)
                                        writer.writerow(['result_id', 'user_id', 'assessment_id', 'score', 'date_taken', 'manager_id'])
                                        for row in rows:
                                            if row[5] == None:
                                                manager_id = ''
                                            elif row[5] != None:
                                                manager_id = row[6]
                                            data = [row[0], row[1], row[2], row[3], row[4], manager_id]
                                            writer.writerow(data)
                                elif user_response.lower() == 'n':
                                    with open(file_name, 'w', newline='') as write_file:
                                        writer = csv.write(write_file)
                                        writer.writerow(['user_id', 'assessment_id', 'score', 'date_taken', 'manager_id'])
                                        for row in rows:
                                            if row[5] == None:
                                                manager_id = ''
                                            elif row[5] != None:
                                                manager_id = row[6]
                                            data = [row[1], row[2], row[3], row[4], manager_id]
                                            writer.writerow(data)

                elif user_response == '6':
                    
                
                elif user_response == '7':
                    file_name = input('Please Enter the CSV File You Would Like to Import: ')
                    if '.csv' not in file_name:
                        file_name += '.csv'
                        print('')
                    if os.path.isfile(file_name) == True:
                        with open(file_name, 'r') as read_file:
                            csvreader = csv.reader(read_file)
                            header = next(csvreader)
                            if header != ['user_id', 'assessment_id','score', 'date_taken', 'manager_id'] or header != ['user_id', 'assessment_id','score', 'date_taken']:
                                print('Header Must Be user_id,assessment_id,score,date_taken,manager_id\nor\nuser_id,assessment_id,score,date_taken\n')
                            elif header == ['user_id', 'assessment_id','score', 'date_taken', 'manager_id']:
                                query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score,date_taken, manager_id) VALUES = (?, ?, ?, ?, ?)'
                                for row in csvreader:
                                    values = (row[0], row[1], row[2], row[3], row[4])
                                    if integ(query, values) = True:
                                        con.commit()
                                    else:
                                        print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}] Raised an Integrity Error.\n')

                            elif header == ['user_id', 'assessment_id','score', 'date_taken']:
                                query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score,date_taken) VALUES = (?, ?, ?, ?)'
                                for row in csvreader:
                                    values = (row[0], row[1], row[2], row[3])
                                    if integ(query, values) = True:
                                        con.commit()
                                    else:
                                        print(f'Record [{row[0]}, {row[1]}, {row[2]}, {row[3]}] Raised an Integrity Error.\n')



            elif user1.role.lower() == user:
                user_response = input('''
What Would You Like To Do?
(1) View Your Profile
(2) Edit Your Profile
(3) View Your User Competency Summary
(4) Export Your User Competency Summary
(5) Logout
(6) Quit
>>> ''')
                if user_response not in ['1','2','3','4','5','6']:
                    print('Please Enter a Valid Input.\n')
                elif user_response == '5':
                    logout_quest = 1
                    quit_quest = 1
                elif user_response == '6':
                    logout_quest = 1