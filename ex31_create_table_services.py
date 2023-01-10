import sqlite3

conection = sqlite3.connect('Nia_Salon.db')
cursor = conection.cursor()

cursor.execute("""DROP TABLE services""") # - SE STERGE TABELUL DE FIECARE DATA !!!! SA NU MAI TREBUIASCA MANUAL :))))
cursor.execute("""CREATE TABLE IF NOT EXISTS services(
                    Sub_Service TEXT,
                    Service TEXT,
                    Price REAL,
                    Id INTIGER,
                    FOREIGN KEY(Id) REFERENCES employees(Id_service))
                     """)


# vedem datele introduse in tablel
cursor.execute("SELECT rowid, * FROM services")
items = cursor.fetchall()
for i in items:
    print(i)

conection.commit()
conection.close()