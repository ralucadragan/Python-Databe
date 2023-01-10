import sqlite3, csv

conection = sqlite3.connect('Nia_Salon.db')
cursor = conection.cursor()

with open('ex33_table_services.csv', 'r') as file:
    nr_rec = 0
    for row in file:
        cursor.execute("INSERT INTO services VALUES(?, ?, ?, ?)", row.split(','))
        conection.commit()
        nr_rec += 1
conection.close()
print('\n{} Records transfered: '.format({nr_rec}))