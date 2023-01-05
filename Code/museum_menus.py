def main_menu():
    print('(1) Admin Interface')
    print('(2) Data Entry Interface')
    print('(3) Browsing Interface')
    i = input('Select from the choices above: ')
    return i
# this is the main menu that will appear on the screens of the users when the code is ran with 3 options which the user then selects.
def admin_menu():
    print('(1) Run SQL Command')
    print('(2) Run a Script')
    print('(3) Exit Program')
    i = input('Select from the choices above: ')
    return i
# if the user chooses the first option i.e. is the admin interface it will give the 2 options mentioned above.
def DataEntry_menu():
    print('(1) Lookup Information')
    print('(2) Insert new Tuple')
    print('(3) Update/Delete')
    print('(4) Exit Program')
    i = input('Select from the choices above: ')
    return i
# if the user chooses the second option i.e. dataentry_menu it will give the 3 options mentioned above.
def Browsing_menu():
    print('(ANY KEY) Look-up Data')
    print('(2) Exit Program')
    i = input('Select from the choices above: ')
    return i
# if the user chooses browsing interface then this menu will open for the user.
def select_role():
    print('(1) Data Admin Role')
    print('(2) Data Entry Role')
    print('(3) Guest Role')
    
    i = input('Select from the roles above: ')
    return i
# this allows the user to select their roles from the 3 options and whatever they choose is inputed into the system.