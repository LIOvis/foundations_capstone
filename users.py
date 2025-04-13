import sqlite3
import bcrypt
from datetime import date

con = sqlite3.connect('competency.db')
cursor = con.cursor()


today = date.today()
today_str = today.strftime('%Y-%m-%d')

first_name = ['Ms.', 'Prof.', 'Zim', 'Gir', 'Minimoose', 'Dib', 'Gaz', 'Zita', 'Gretchen', 'Poonchy,', 'The Letter']

last_name = ['Bitters', 'Membrane', 'Invader of Irk', 'Mighty Robot', 'T.P.S.M.', 'Membrane', 'Membrane', 'Spitz', 'Sobremordida', 'Drinker of Hate', '"M"']

phone = ['1-800-BITTERS', '1-800-SCIENCE', '1-800-INVADER', '1-800-INVADER', '1-800-INVADER', '1-800-MOTHMAN', '1-800-GODFRFR', '1-800-MSBSFAV', '1-800-TEEEETH', '1-800-H8JUICE', '1-800-LETTERM']

email = ['bitters@skool.edu','theprofessor@mlabs.org','iamzim!!!@skool.edu', 'mytaquitos!!!@sir.org', 'toolofdoom@sir.org', 'notaclone@skool.edu', 'headgaurd@mlabs.org', 'eyelessthorns@skool.edu', 'braced@skool.edu', 'accidentaloverlord@skool.edu','notcocofange@skool.edu']

password = ['moral_outrage', 'my_poor_insane_son', 'a_genius!!', 'i_dont_know', 'temporarily_pizzalessless', 'zim_is_an_alien!!!', 'emissary_of_the_shadowhog', 'mash_potato_hater', 'can_i_have_a_soda?', 'hate_in_a_cup', 'gnafococmai']

hire_date = ['2001-03-30', '2001-03-30', '2001-03-30', '2001-03-30', '2002-12-10', '2001-03-30', '2001-03-30', '2001-03-30', '2001-04-13', '2001-09-28', '2001-10-26',]

role = ['Admin', 'Admin', 'User', 'User', 'Admin', 'User', 'Admin', 'User', 'User', 'User', 'User']

query = 'INSERT INTO Users (user_id, first_name, last_name, phone, email, password, hire_date, date_created, role, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
values = ()

for i in range(0,11):
    values = (i+1,first_name[i], last_name[i], phone[i], email[i], bcrypt.hashpw(password[i].encode('utf-8'), bcrypt.gensalt()), hire_date[i], today_str, role[i], 1)
    cursor.execute(query, values)
    con.commit()
    
