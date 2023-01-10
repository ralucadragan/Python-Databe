import ex35_op_tableservices

# show the database
print('')
print('SHOW THE INITIAL DATEBASE WITH ALL THE SERVICES')
ex35_op_tableservices.show_all_services()
print('')


# show a specific service
print('SHOW ALL SUB-SERVICES FROM A SERVICE')
ex35_op_tableservices.show_specific_service('Masaj')
print('')

# show update of a service price
print('')
print('SHOW THE SERVICE WITH THE PRICE UPDATE')
ex35_op_tableservices.update_a_price()
print('')

# show update of multiple service prices - crestere de 10 % a preturilor
print('')
print('SHOW THE SERVICES WITH PRICE UPDATE')
ex35_op_tableservices.updat_multiple_prices()
print('')

# show specific columns
print('')
print('DISPLAY SPECIFIC COLUMNS')
ex35_op_tableservices.display_specific_columns()
print('')
