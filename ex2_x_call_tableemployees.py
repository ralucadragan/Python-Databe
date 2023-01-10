import ex2_op_on_tableemployees
'''
# show the database
print('')
print('SHOW THE INITIAL DATEBASE WITH ALL EMPLOYEES')
ex2_op_on_tableemployees.show_all_employees()
print('')

# show one client
print('SHOW ONE EMPLOYEE FROM DATABESE')
ex2_op_on_tableemployees.show_one_employee('Masaj')
print('')

# add a new record to database
print('ADD A NEW EMPLOYEE TO THE DATABASE')
ex2_op_on_tableemployees.add_employee('Cris', 'Jau', 60, 725663552, 'crisss@gmail.com', 'Manichiura', 582)
ex2_op_on_tableemployees.show_all_employees()
print('')

# delete record to database
print('DELETE A EMPLOYEE FROM DATABASE')
ex2_op_on_tableemployees.delete_employee('Maria', 'Balota')
ex2_op_on_tableemployees.show_all_employees()
print('')

# add a new record to database
print('ADD A NEW EMPLOYEE TO THE DATABASE')
ex2_op_on_tableemployees.add_employee('Nalu', 'Guci', 72, 725033247, 'nalunalu@gmail.com', 'Frizerie femei', 728)
ex2_op_on_tableemployees.show_all_employees()
print('')

'''