import sqlite3

conection = sqlite3.connect('Nia_Salon.db')
cursor = conection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS appointments (
                Date TEXT,
                Time INTIGER,
                Client TEXT,
                Id_client INTIGER,
                Sub_services TEXT,
                Id_service INTIGER,
                Price INTIGER)
                """)
# inseram mai multe randuri
many_appointments = [
    ('2023-01-10', 8, '', '', '', 123, ''),
    ('2023-01-10', 9, 'Maria',10, 'Epilat axila', 123, 25),
    ('2023-01-10',9, 'Maria',10, 'Epilat inghinal', 123, 45),
    ('2023-01-10', 10, '', '', '', 123, ''),
    ('2023-01-10', 11,  '', '', '', 123, ''),
    ('2023-01-10', 12,  '', '', '', 123, ''),
    ('2023-01-10', 13,  '', '', '', 123, ''),
    ('2023-01-10', 14,  '', '', '', 123, ''),
    ('2023-01-10', 15,'Maria',10, 'Epilat abdomen', 123, 30),
    ('2023-01-10', 16,  '', '', '', 123, ''),
    ('2023-01-10', 16,  '', '', '', 123, ''),

]
cursor.executemany("INSERT INTO  appointments VALUES(?, ?, ?, ?, ?, ?, ?)", many_appointments)

# vedem datele introduse in tablel
cursor.execute("SELECT rowid, * FROM appointments")
items = cursor.fetchall()
for i in items:
    print(i)

for x in items:
    print(f'Id_service:', x[6])
    print(f'Date:', x[1])
    print(f'Time:', x[2])
    print(f'Client:', x[3])
    print(f'Id_client:', x[4])
    print(f'Sub_services:', x[5])
    print(f'Price:', x[7])
    print('')

conection.commit()
conection.close()