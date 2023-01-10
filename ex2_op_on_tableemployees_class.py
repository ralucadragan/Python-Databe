from prettytable import PrettyTable
from ex2_create_table_employees_class import Employees

# instatiate the class
data_base = Employees()

# we have columns 7 in the table and need 7 matching bits of data:
# introducem mai multi employees deodata
many_employees = [
    ('Stefania', 'Berenyi',10, 722940045, 'stefi.jau@gmail.com', 'Cosmetica', 123),
    ('Tom', 'Barb', 20,723123456, 'tom.b@gmail.com', 'Frizerie barbati', 456),
    ('Maria', 'Balota', 30, 745456321, 'b.maria.j@gmail.com', 'Frizerie femei', 728),
    ('Magdalena', 'Manu', 40,745005006, 'magda.m24@gmail.com', 'Masaj', 963)]
data_base.insert_multiple_employeee(many_employees)

# introducem un singur employee
item = ('Cris', 'Jau', 60, 725663552, 'crisss@gmail.com', 'Manichiura', 582)
data_base.insert_one_employee(item)
#for item in data_base.read():
    #print(item)


table = PrettyTable()
table.field_names = ['FirstName', 'LastName', 'ID_employee', 'Telephone', 'E_mail', 'Service', 'ID_service']
for i in data_base.read():
    table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6]])
table.align['FirstName'] = 'l'
table.align['LastName'] = 'l'
table.align['E_mail'] = 'l'
table.align['Service'] = 'l'
print('SHOW THE DATEBASE WITH ALL EMPLOYEES')
print(table)
print('')
