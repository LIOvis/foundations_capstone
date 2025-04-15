import sqlite3

con = sqlite3.connect('competency.db')
cursor = con.cursor()

name_list = ['Computer Anatomy', 'Data Types', 'Variables', 'Functions', 'Boolean Logic', 'Conditionals', 'Loops', 'Data Structures', 'Lists', 'Dictionaries', 'Working with Files', 'Exception Handling', 'QA', 'OOP', 'Recursion', 'Databases']

description_list = ['The internal components that make up the machine, including hardware and software.', 'A particular kind of data item, as defined by the values it can take, the programming language used, or the operations that can be performed on it.', 'A named storage location that holds a value within a program', 'Reusable blocks of code that preform specific tasks.', 'A type of algebra dealing with values that can be either TRUE or FALSE. It uses four basic logical operators: NOT, AND, OR, and XOR', 'Fundamental tools that control the flow of a program\'s execution by allowing it to make decisions based on specific conditions.', 'A structure that allows a sequence of instructions to be executed repeatedly until a specified condition is met.', 'A specific way of organizing and storing data to enable efficient access and modification.', 'A fundamental data structure that organizes a collection of items in a specific order.', 'A data structure that stores data in the form a key-value pairs.', 'The process of creating, storing, retrieving, modifying, and deleting data stored within files.', 'The process of responding to unexpected events (exceptions) that disrupt a program\'s normal flow.', 'A systematic process for ensuring that software or hardware products meet defined standards and requirements.', 'A programming paradigm that organizes code around objects, which are data structures that contain both data (fields) and code (methods) that operate on that data.', 'A programming technique where a function calls itself to solve a problem by breaking it down into smaller, self-similar subproblems.', 'An organized collection of data designed for efficient storage, retrieval, and management.'] 

print(len(name_list))
print(len(description_list))

query = 'INSERT INTO Competencies (competency_id, name, description) VALUES (?, ?, ?)'
values = ()

# for i in range(0,16):
#     values = (i+1, name_list[i], description_list[i])
#     cursor.execute(query, values)
#     con.commit()

row = cursor.execute('SELECT * FROM Users').fetchone()
print(row)
