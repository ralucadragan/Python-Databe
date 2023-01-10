import sqlite3

# creaza baza de date
conection = sqlite3.connect('Nia_Salon.db')

# cream un cursor = ii spune bazei de date ce sa faca
cursor = conection.cursor()

# cream un tabel - trebuie sa declarat tipul de date de pe coloenele create (null, integer, real, text, blob)
cursor.execute("""DROP TABLE clients""") # - SE STERGE TABELUL DE FIECARE DATA !!!! SA NU MAI TREBUIASCA MANUAL :))))
cursor.execute(""" CREATE TABLE IF NOT EXISTS clients (
                FirstName TEXT,
                LastName TEXT,
                Age INTIGER,
                Gender TEXT,
                Telephone INTIGER unique,
                E_mail TEXT,
                Id_client INTIGER PRIMARY KEY)
                """)
# inseram mai multe randuri
many_clients = [
    ('Raluca', 'Dragan', 39, 'F', 722940071, 'raluca@gmail.com', 10),
    ('Tom', 'Thomson', 45, 'M', 723456789, 'tom.t@gmail.com', 20),
    ('Dan', 'Negru', 15, 'M', 727789456, 'dan156@gmail.com', 30),
    ('Ioana', 'Jurcau', 35, 'F', 745123789, 'ioana.j@gmail.com', 40),
    ('Maia', 'Laslau', 24, 'F', 745678912, 'maia.24@gmail.com', 50)
]
cursor.executemany("INSERT INTO clients VALUES(?, ?, ?, ?, ?, ?, ?)", many_clients)

# vedem datele introduse in tablel
cursor.execute("SELECT rowid, * FROM clients")
items = cursor.fetchall()
for i in items:
    print(i)

# commit our comand
conection.commit()
#close our connection
conection.close()