import sqlite3
from prettytable import PrettyTable

def show_all_clients():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM clients")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'FirstName', 'LastName', 'Age', 'Gender', 'Telephone', 'E_mail', 'ID_client']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    table.align['FirstName'] = 'l'
    table.align['LastName'] = 'l'
    table.align['E_mail'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def show_one_client(telephone):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM clients WHERE telephone = (?)", (telephone,))
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'FirstName', 'LastName', 'Age', 'Gender', 'Telephone', 'E_mail', 'ID_client']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    table.align['FirstName'] = 'l'
    table.align['LastName'] = 'l'
    table.align['E_mail'] = 'l'
    print(table)

    conection.commit()
    conection.close()


# add a new record to the table
def add_client(firstName, lastName, age, gender, telephone, e_mail, id):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    try:
        cursor.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?)", (firstName, lastName, age, gender, telephone, e_mail, id))
    except:
        print('Sorry the phone number already exist!!!')

    conection.commit()
    conection.close()


# delete record to the table
def delete_client(firstName, lastName, telephone):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("DELETE FROM clients WHERE firstName = (?) OR firstName = (?) AND telephone = (?) ", (firstName, lastName, telephone))

    conection.commit()
    conection.close()


# add a new record to the table using input
def add_client_input(firstName, lastName, age, gender, telephone, e_mail, id):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    try:
        cursor.execute("INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?)", (firstName, lastName, age, gender, telephone, e_mail, id))
    except:
        print('Sorry! The phone number is already taken!!!')

    conection.commit()
    conection.close()