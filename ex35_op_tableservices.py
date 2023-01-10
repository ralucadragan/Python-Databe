import sqlite3
from prettytable import PrettyTable

def show_all_services():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM services")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Sub-Service', 'Service', 'Price', 'Service_ID']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4]])
    table.align['Sub-Service'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def show_specific_service(serv):
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, * FROM services WHERE service = (?)", (serv,))
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Sub-Service', 'Service', 'Price', 'Service_ID']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4]])
    table.align['Sub-Service'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def update_a_price():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()
    cursor.execute("""UPDATE services SET price = 156
                      WHERE  Sub_Service = 'Epilat axila' """)
    cursor.execute("SELECT rowid, * FROM services WHERE price = 156")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Sub-Service', 'Service', 'Price', 'Service_ID']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4]])
    table.align['Sub-Service'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def updat_multiple_prices():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()
    cursor.execute("""UPDATE services SET price = (price * 1.1)
                      WHERE ID = 582 """)
    cursor.execute("SELECT rowid, * FROM services")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Sub-Service', 'Service', 'Price', 'Service_ID']
    for i in items:
        table.add_row([i[0], i[1], i[2], i[3], i[4]])
    table.align['Sub-Service'] = 'l'
    table.align['Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()

def display_specific_columns():
    conection = sqlite3.connect('Nia_Salon.db')
    cursor = conection.cursor()

    cursor.execute("SELECT rowid, Sub_Service, Price FROM services")
    items = cursor.fetchall()

    table = PrettyTable()
    table.field_names = ['RowID', 'Sub-Service', 'Price']
    for i in items:
        table.add_row([i[0], i[1], i[2]])
    table.align['Sub-Service'] = 'l'
    print(table)

    conection.commit()
    conection.close()