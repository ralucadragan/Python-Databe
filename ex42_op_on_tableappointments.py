import sqlite3
from prettytable import PrettyTable

def show_initial_appointments():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM appointments")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Date', 'Time','Client', 'Id_employee', 'Sub_services', 'Id_service','Price']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    table.align['FirstName'] = 'l'
    table.align['Date'] = 'l'
    table.align['Client'] = 'l'
    table.align['Sub_services'] = 'l'
    print(table)

    conection.commit()
    conection.close()
