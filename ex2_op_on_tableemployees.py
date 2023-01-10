import sqlite3
from prettytable import PrettyTable
'''
def show_all_employees():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM employees")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'FirstName', 'LastName', 'ID_employee', 'Telephone', 'E_mail', 'Service','ID_service']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    table.align['FirstName'] = 'l'
    table.align['LastName'] = 'l'
    table.align['E_mail'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def show_one_employee(serv):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM employees WHERE service = (?)", (serv,))
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'FirstName', 'LastName','ID_employee', 'Telephone', 'E_mail', 'Service','ID_service']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    table.align['FirstName'] = 'l'
    table.align['LastName'] = 'l'
    table.align['E_mail'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()


# add a new record to the table
def add_employee(firstName, lastName, id_e,telephone, e_mail, service, id_s):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?)", (firstName, lastName, id_e, telephone, e_mail, service, id_s))

    conection.commit()
    conection.close()

# delete record to the table
def delete_employee(firstName, lastName):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("DELETE FROM employees WHERE firstName = (?) OR firstName = (?) ", (firstName, lastName))

    conection.commit()
    conection.close()
'''
