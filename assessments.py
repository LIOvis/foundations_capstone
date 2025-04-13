import sqlite3
from datetime import date

con = sqlite3.connect('competency.db')
cursor = con.cursor()

today = date.today()
today_str = today.strftime('%Y-%m-%d')

competency_id =[13, 4, 3, 6, 10, 11, 8, 2, 14, 5, 7, 1, 9, 15, 12, 16]

name = ['QA Assignment', 'Functions Assignment', 'Variables Quiz', 'FizzBuzz Assignment', 'Dictionaries Quiz', 'Working with Files Assignment', 'Data Structures Quiz', 'Data Types Quiz', 'Create a Class (OOP) Assignment', 'Boolean Logic Quiz', 'While & For Loops Assignment', 'Computer Anatomy Quiz', 'Lists Quiz', 'Recursion Assignment', 'Exception Handling Assignment', 'Databases Quiz']

query = 'INSERT INTO Assessments (competency_id, name, date_created) VALUES (?, ?, ?)'
values = ()


for i in range(0,16):
    values = (competency_id[i], name[i], today_str)
    cursor.execute(query, values)
    con.commit()

    

