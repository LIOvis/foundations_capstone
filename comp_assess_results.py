import sqlite3
from datetime import date
import random

con = sqlite3.connect('competency.db')
cursor = con.cursor()

today = date.today()
today_str = today.strftime('%Y-%m-%d')

manager_id_list = []

user_id = 0
assessment_id = 0
score = 0
manager_id = 0

query = 'INSERT INTO Competency_Assessment_Results (user_id, assessment_id, score, date_taken, manager_id) VALUES (?, ?, ?, ?, ?)'
values = ()

for i in range(1,101):
    manager_id_list = [1, 2, 5, 7]
    user_id = random.randint(1, 11)
    assessment_id = random.randint(17,32)
    random_day = random.randint(13, 18)
    date = f'2025-04-{random_day}'
    if user_id == 1:
        manager_id_list = [2, 5, 7]
    if user_id == 2:
        manager_id_list = [1, 5]
    if user_id == 5: 
        manager_id_list = [1, 2, 7]
    if user_id == 7:
        manager_id_list = [1, 5]
    manager_id = random.choice(manager_id_list)
    
    if user_id == 1 or user_id == 2 or user_id == 5 or user_id == 7:
        score = random.randint(3,4)
    else:
        score = random.randint(0,4)
   
    values = (user_id, assessment_id, score, date, manager_id)
    cursor.execute(query, values)
    con.commit()
        
