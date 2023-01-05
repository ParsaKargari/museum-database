import mysql.connector
from mysql.connector import errorcode # LOGIN ERRORS
#this imports the sql database and the queries.
import museum_menus as mm
#imports the museum_menus python file.

from tabulate import tabulate

def login_user():
    print(' - Loading SQL... - ')
    print(' - Please Login to your account - ')
# this is the part where the user is asked their login info.
def give_role():
    role_id = mm.select_role()
    if role_id == '1':
        return 'ADMIN'
    elif role_id == '2':
        return 'DATAENTRY'
    elif role_id == '3':
        return 'GUEST'

def output_fetch():
    output_show = cursor.fetchall()
    for i in output_show:
        print(i)

def sql_file_execute(filename):
    while(True):
        try:
            fi = open(filename, 'r')
        except:
            print('Couldnt find the file!')
            filename = input('Enter the new file location -> ')
        else:
            break

    sqlReadFile = fi.read()
    fi.close()
    sqlReadFile = sqlReadFile.split(';')
    for query in sqlReadFile:
        try:
            cursor.execute(query)
        except:
            print(f'(ERROR) Skipped a command -> {query}')

        splited_query = query.split()
        print()
        print(f'Output for ->')
        print(query)
        print()
        try:
            if (splited_query[0]).capitalize() in ['Insert' , 'Delete' , 'Update']:
                cnx.commit()
        except:
            pass
            
        try:
            if (splited_query[0]).capitalize() == ('Select'):
                    
                output_fetch()
        except:
            pass
        print()
        
        

def string_list(table):
    for i in table:
                string = ''
                for x in i:
                    if x.isalpha() == True:
                        string += x
                table_list2.append(string.capitalize())

def tabulate_result(res, heads):
    print(tabulate(res, headers=heads, tablefmt='psql'))

def list_to_string_wstr(lis):
    return '\', \''.join(lis)

def list_to_string(lis):
    return ', '.join(lis)



# LOGIN THE USER
user_role = give_role()
if user_role == 'ADMIN' or user_role == 'DATAENTRY':
    while(True):
        login_user()

        username_entry = input('Enter your username: ')
        password_entry = input('Enter your Password: ') or None
        host_entry = "127.0.0.1"
# this option arrives only when the user selects either roleid 1 or 2  
# then they are asked for their login info which then is ran through mysql to check whether the info is right or not
        try:
            cnx = mysql.connector.connect(
            user = username_entry,
            password = password_entry,
            host = host_entry,
            database = 'museum_db'
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Username / Password is incorrect!')
                print('Try checking your Username and Password...')
                print('')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
# if the information entered by the user is wrong it tells the user that it's incorrect and asks the user to check their information
# if they manage to enter their information wrong multiple time then it gives an error                
        else:
            print()
            print('Connected Succesfully!')
            print()
            print('-' * 30)
            break
#if the user enters their data correct then they login succesfully and get connected to the server
else:
    
    cnx = mysql.connector.connect(
            user = 'guest',
            password = None,
            host = "127.0.0.1",
            database = 'museum_db'
            )

cursor = cnx.cursor()
logout = 0
while (True):
    if logout == '1':
        break
    if user_role == 'ADMIN':
        admin_choice = mm.admin_menu()
        if admin_choice == '1':
            execute_admincmd = input('Enter a MySQL command: ')
            try:
                cursor.execute(execute_admincmd)
            except:
                print('SQL Could not Execute that command :(')
            
            
            execute_admincmd_LIST = (execute_admincmd).split()
            
            try:
                if (execute_admincmd_LIST[0]).capitalize() in ['Insert' , 'Delete' , 'Update']:
                
                    cnx.commit()
            except:
                pass
                    
            try:
                if (execute_admincmd_LIST[0]).capitalize() == ('Select'):
                    output_fetch()
            except:
                pass
            
            print()
            input('ENTER to continue...')
        
        if admin_choice == '2':
            filename = input('Enter the file location -> ')
            sql_file_execute(filename)
        
        if admin_choice == '3':
            break


    elif user_role == 'DATAENTRY':
        table_list = []
        table_list2 = []
        temp_list = []
        num =0
        data_entry_choice = mm.DataEntry_menu()

        if data_entry_choice == '1':
            cursor.execute("show tables")
            
            for tableN in cursor:
                table_list.append(tableN)
            print()
            print('Look up data from the following tables: ')
            string_list(table_list)
            for i in table_list2:
                num+=1
                print(f'({num}) {i.capitalize()}')
                
            print()
            table_choice = input('Enter the table name to look up: ')

            while(True):
                if table_choice.capitalize() not in table_list2:
                    print('That Table name was not found, try again.')
                    table_choice = input('Enter the table name to look up: ')
                else:
                    break

            print(f'Attributes in {table_choice.capitalize()} table:')
            cursor.execute(f'SELECT * FROM {table_choice}')
            col_names = cursor.column_names
            num = 0
            for i in col_names:
                num+=1
                print(num, i)
            print()
            
            print('Tabulated Result: ')
            tabulate_result(cursor.fetchall(), col_names)
            input("ENTER to continue...")
            
        if data_entry_choice == '2':
            cursor.execute("show tables")
            
            for tableN in cursor:
                table_list.append(tableN)
            print()
            print('Look up data from the following tables: ')
            string_list(table_list)
            for i in table_list2:
                num+=1
                print(f'({num}) {i.capitalize()}')
                
            print()
            table_choice = input('Enter the table name you want to insert a tuple to: ')
            while(True):
                if table_choice.capitalize() not in table_list2:
                    print('That Table name was not found, try again.')
                    table_choice = input('Enter the table name to look up: ')
                else:
                    break
            
            cursor.execute(f'SELECT * FROM {table_choice}')
            
            col_names = cursor.column_names
            print()

            print(f'Now adding tuple into \"{table_choice}\" table.')
            print('MAKE SURE YOU SURROUND THE STRINGS WITH QUOTATIONS AND INTEGERS WITHOUT')
            for cols in col_names:
                append_data = input(f'Enter value for attribute "{cols}" -> ')
                temp_list.append(append_data)
            columns_str = list_to_string(col_names)
            values_str = list_to_string(temp_list)
            
            results = cursor.fetchall()
            
            
            
            while(True):
                try:
                    print("INSERT INTO " + table_choice + " (" + columns_str + ") VALUES ("+ values_str +")")
                    cursor.execute("INSERT INTO " + table_choice + " (" + columns_str + ") VALUES (" +values_str +")")
                    break
                except:
                    print(f"Error Inserting data into {table_choice}. ")
                    temp_list = []
                    for cols in col_names:
                        append_data = input(f'Enter value for attribute "{cols}" -> ')
                        temp_list.append(append_data)
                    values_str = list_to_string(temp_list)
            cnx.commit()
            print(f'Data succesfully added to {table_choice}!')
            print()
        if data_entry_choice == '3':
            cursor.execute("show tables")
            
            for tableN in cursor:
                table_list.append(tableN)
            print()
            print('Look up data from the following tables: ')
            string_list(table_list)
            for i in table_list2:
                num+=1
                print(f'({num}) {i.capitalize()}')
                
            print()
            table_choice = input('Enter the table name you want to insert a tuple to: ')
            print('MAKE SURE YOU SURROUND THE STRINGS/DATES WITH QUOTATIONS AND INTEGERS WITHOUT')
            while(True):
                if table_choice.capitalize() not in table_list2:
                    print('That Table name was not found, try again.')
                    table_choice = input('Enter the table name to look up: ')
                else:
                    break
            
            cursor.execute(f'SELECT * FROM {table_choice}')
            
            col_names = cursor.column_names
            results = cursor.fetchall()
            print()
            tabulate_result(results, col_names)
            print('Enter 1 for Delete')
            print('Enter 2 for Update')
            delorup = input('Choice: ')
            while(delorup != '1' and delorup != '2'):
                print('Enter a valid choice!')
                print()
                print('Enter 1 for Delete')
                print('Enter 2 for Update')
                delorup = input('Choice: ')

            if delorup == '1':
                
                x = 1
                sqlqr = ''
                apd = ''
                
                
                while(True):
                    try:
                        for i in  col_names:
                            apd = input(f'Enter the values to be deleted under the attribute "{i}": ')
                            sqlqr += i
                            sqlqr += '='
                            sqlqr += apd
                            if(x<len(col_names)):
                                sqlqr += ' AND '
                            x+=1
                    
                        cursor.execute("DELETE FROM " + table_choice + " WHERE " + '('+sqlqr+');')
                        break
                    except:
                        print('Error, could not delete the entry :(')
                        print('Try again!')
                        print()
                        sqlqr = ''
                        x = 1
                print(f'DELETE SUCCESS FROM {table_choice}!') 
                cnx.commit()

            if delorup == '2':
                x = 1
                sqlqr = ''
                apd = ''
                
                
                while(True):
                    print('MAKE SURE YOU SURROUND THE STRINGS WITH QUOTATIONS AND INTEGERS WITHOUT')
                    try:
                        for i in  col_names:
                            apd = input(f'Enter the values of the tuple that needs to be updated under the attribute  "{i}": ')
                            
                            sqlqr += i
                            sqlqr += '='
                            sqlqr += apd
                            if(x<len(col_names)):
                                sqlqr += ' AND '
                            x+=1
                        attrname = input('Enter the attribute name: ')
                        attrnewnVal = input('Enter the new attribute value: ')
                        cursor.execute("UPDATE " + table_choice + " SET " + attrname + " = '" + attrnewnVal + "' WHERE " + '('+sqlqr+');')
                        break
                    except:
                        print('Error, could not update the entry :(')
                        print('Try again!')
                        print()
                        sqlqr = ''
                        x = 1
                print(f'UPDATE SUCCESS FROM {table_choice}!') 
                cnx.commit()
        elif data_entry_choice == '4':
            break

    elif user_role == 'GUEST':

        while(True):
            cursor.execute("show tables")
            table_list = []
            table_list2 = []
            temp_list = []
            num =0
            guest_choice = mm.Browsing_menu()
            if guest_choice == '2':
                logout = '1'
                break
            for tableN in cursor:
                table_list.append(tableN)
            print()
            print('Look up data from the following tables: ')
            string_list(table_list)
            for i in table_list2:
                num+=1
                print(f'({num}) {i.capitalize()}')
                
            print()
            table_choice = input('Enter the table name to look up (00 to go back): ')
            if table_choice == "00":
                cursor.fetchall()
                break
            while(True):
                while(True):
                    if table_choice.capitalize() not in table_list2:
                        print('That Table name was not found, try again.')
                        table_choice = input('Enter the table name to look up: ')
                    else:
                        break

                print(f'Attributes in {table_choice.capitalize()} table:')
                cursor.execute(f'SELECT * FROM {table_choice}')
                col_names = cursor.column_names
                num = 0
                for i in col_names:
                    num+=1
                    print(num, i)
                print()
                
                print('Tabulated Result: ')
                tabulate_result(cursor.fetchall(), col_names)
                input("ENTER to continue...")
                cursor.fetchall()
                break