import ex1_op_on_tableclients

# show the database
print('')
print('SHOW THE INITIAL DATEBASE WITH ALL CLIENTS')
ex1_op_on_tableclients.show_all_clients()
print('')

# show one client
print('SHOW ONE CLIENT FROM DATABESE')
ex1_op_on_tableclients.show_one_client(727789456)
print('')

# add a new record to database
print('ADD A NEW CLIENT TO THE DATABASE')
ex1_op_on_tableclients.add_client('Bella', 'Miau', 14, 'F', 722940896, 'bella@gmail.com', 60)
ex1_op_on_tableclients.show_all_clients()
print('')

# delete record to database
print('DELETE A CLIENT FROM DATABASE')
ex1_op_on_tableclients.delete_client('Bella', 'Miau', '724567145')
ex1_op_on_tableclients.show_all_clients()
print('')



'''
# add a new record to database INPUT
print('ADD A NEW CLIENT TO THE DATABASE')

while True:

    while True:
        firstName = input('Enter the client First Name: ')
        if not firstName.isalpha():
            print('Not all the letter in text are text format! ')
        else:
            first_letter = firstName[0]
            if not first_letter.isupper():
                print('The first letter has to be a upper letter!')
            else:
                break

    while True:
        lastName = input('Enter the client Last Name: ')
        if not lastName.isalpha():
            print('Not all the letter in text are text format! ')
        else:
            first_letter = lastName[0]
            if not first_letter.isupper():
                print('The first letter has to be a upper letter!')
            else:
                break

    while True:
        age = input('Enter the client Age: ')
        if not age.isnumeric():
            print('The - Age - input has to be number format! ')
        else:
            if age[0] == '0':
                print('The age cant start with number - 0 -!')
                continue
            if len(age) > 2:
                ask = input('Wowww! The client is varry old! Are you sure the age is corect? y/n : ')
                if ask == 'y':
                    print(f'Ok. Wowww!!! The new client is old! The final age is: {age}')
                    break
                elif ask == 'n':
                    print('Ok. You have to reenter the age! ')
                    continue
            break

    while True:
        gender = input('Enter the client Gender (F/M): ')
        if (gender != 'F') and (gender != 'M'):
            print('The gender has to be - F - or - M - (upper cases):')
        else:
            break

    while True:
        telephone = input('Enter the client telephone number:'
                          '\nThe format is 7xx xx xx xx (len = 9) : ')
        if not telephone.isnumeric():
            print('The - Telephone number - input has to be number format! ')
        else:
            if len(telephone) != 9:
                print('The lenght of telephone number has to be 9 digit!!! Try again ')
                continue
            if telephone[0] != '7':
                print('The first digit has to be -7-. Try again! ')
            else:
                break

    while True:
        email = input('Enter the client e-mail: ')

        length_of_email = len(email)
        number_of_at_characters = email.count("@")
        number_of_dot_characters = email.count(".")
        position_of_at = email.find("@")
        position_of_first_dot = email.find(".")
        position_of_last_dot = email.rfind(".")
        position_of_first_dot_after_the_at = email.find(".", position_of_at)

        # "hello.worldcom"    => An email address has to contain a '@' character!
        if number_of_at_characters == 0:
            error_message_no_at = "An email address has to contain a '@' character!"
            print(error_message_no_at)
            continue

        # "he@llo@world.com"  => An email address cannot contain more than one '@' characters!
        elif number_of_at_characters > 1:
            error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
            print((error_message_too_many_at))
            continue

        # "@world.com"        => The username before the '@' character cannot be empty!
        elif position_of_at == 0:
            error_message_no_username = "The username before the '@' character cannot be empty!"
            print(error_message_no_username)
            continue

        # "hello@"            => The domain after the '@' character cannot be empty!
        elif length_of_email - position_of_at == 1:
            error_message_no_domain = "The domain after the '@' character cannot be empty!"
            print(error_message_no_domain)
            continue

        # "hello@worldcom"    => An email address has to contain at least one '.' character!
        elif number_of_dot_characters == 0:
            error_message_no_dot = "An email address has to contain at least one '.' character!"
            print(error_message_no_dot)
            continue

        # "hell.o@worldcom"   => The domain has to contain at least one '.' character!
        elif position_of_first_dot_after_the_at == -1:
            error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
            print(error_message_no_dot_in_domain)
            continue

        # "he.llo@worldcom."  => The top-level domain cannot be empty!
        elif position_of_last_dot == length_of_email - 1:
            error_message_no_tld = "The top-level domain cannot be empty!"
            print(error_message_no_tld)
            continue

        # "he.llo@worldco.m"  => The top-level domain has to be at least two characters long!
        elif position_of_first_dot_after_the_at == 14:
            error_message_short_tld = "The top-level domain has to be at least two characters long!"
            print(error_message_short_tld)
            continue

        # ".hello@world.com"  => The username cannot start with a '.' character!
        elif position_of_first_dot == 0:
            error_message_invalid_username = "The username cannot start with a '.' character!"
            print(error_message_invalid_username)
            continue

        # "he.llo@.world.com" => The domain cannot start with a '.' character!
        elif position_of_at == position_of_first_dot_after_the_at - 1:
            error_message_no_server_name = "The domain cannot start with a '.' character!"
            print(error_message_no_server_name)
            continue

        # "hello@world.com"   => Valid email address :)
        else:
            print("Valid email address :)")
            break

    while True:
        id = input('Enter the client ID: ')
        if not id.isnumeric():
            print('The - ID - input has to be number format! ')
        else:
            if id[0] == '0':
                print('The ID cant start with number - 0 -!')
                continue
            if len(id) > 2:
                print( 'The ID numeber has to have 2 caharcter: ')
                continue
            else:
                break

    ex1_op_on_tableclients.add_client_input(firstName, lastName, age.format(int), gender, telephone.format(int), email, id.format(int))

    print('')
    check = input('Do you want to introduce another client? '
                  'To CONTINUE and introduce another client press - y - and to QUIT press - q - : ')
    if check == 'y':
        print('Ok. Introduce another new client !')
        print('')
    elif check == 'q':
        print('Ok. Have a nice day!')
        break

ex1_op_on_tableclients.show_all_clients()
print('')
'''
