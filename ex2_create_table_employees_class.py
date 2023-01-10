import sqlite3
from prettytable import PrettyTable
'''
# creaza baza de date
conection = sqlite3.connect('Nia_Salon.db')

# cream un cursor = ii spune bazei de date ce sa faca
cursor = conection.cursor()

# cream un tabel - trebuie sa declarat tipul de date de pe coloanele create (null, integer, real, text, blob)
# cursor.execute("""DROP TABLE employees""") # - SE STERGE TABELUL DE FIECARE DATA !!!! SA NU MAI TREBUIASCA MANUAL :))))
cursor.execute("""CREATE TABLE IF NOT EXISTS employees (
                FirstName TEXT,
                LastName TEXT,
                ID_employee INTIGER PRIMARY KEY,
                Telephone INTIGER unique,
                E_mail TEXT,
                Service TEXT,
                Id_service INTIGER )
                """)
# inseram mai multe randuri
many_employees = [
    ('Stefania', 'Berenyi',10, 722940045, 'stefi.jau@gmail.com', 'Cosmetica', 123),
    ('Tom', 'Barb', 20,723123456, 'tom.b@gmail.com', 'Frizerie barbati', 456),
    ('Maria', 'Balota', 30, 745456321, 'b.maria.j@gmail.com', 'Frizerie femei', 728),
    ('Magdalena', 'Manu', 40,745005006, 'magda.m24@gmail.com', 'Masaj', 963)
]
cursor.executemany("INSERT INTO  employees VALUES(?, ?, ?, ?, ?, ?, ?)", many_employees)

# vedem datele introduse in tablel
cursor.execute("SELECT rowid, * FROM employees")
items = cursor.fetchall()
for i in items:
    print(i)

# commit our comand
conection.commit()
#close our connection
conection.close()
'''

class Employees():
    def __init__(self):
        self.conection = sqlite3.connect('Nia_Salon.db')
        self.cursor = self.conection.cursor()
        self.create_tabele()

    def create_tabele(self):
        #self.cursor.execute("""DROP TABLE employees""") # - SE STERGE TABELUL DE FIECARE DATA !!!! SA NU MAI TREBUIASCA MANUAL :))))
        self.cursor.execute ("""CREATE TABLE IF NOT EXISTS employees (
                                            FirstName TEXT,
                                            LastName TEXT,
                                            ID_employee INTIGER PRIMARY KEY,
                                            Telephone INTIGER unique,
                                            E_mail TEXT,
                                            Service TEXT,
                                            Id_service INTIGER )
                                            """)
    def insert_multiple_employeee(self,many_employees):
        self.cursor.executemany("INSERT INTO  employees VALUES(?, ?, ?, ?, ?, ?, ?)", many_employees) # insereaza mai multi angajati deodata
        self.conection.commit()


    def insert_one_employee(self,item):
        self.cursor.execute("""INSERT OR IGNORE INTO employees VALUES(?, ?, ?, ?, ?, ?, ?)""", item) # insereaza un angajat
        self.conection.commit()

    def read(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        return rows



