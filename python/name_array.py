def display_menu():
    menu = '1. Add name\n'\
           '2. Display name\n'\
           '3. Quit\n'
    choice = -1
    while choice < 1 or choice > 3:
        choice = int(input(menu))
    # end while
    return choice
# end function

name_list=['1','2','3','4','5','6','7','8','9','10']

def display_g():
    for name in name_list:# [5:] says using the name list but only from te fifth variable
        print(name)
    #next name
#end procedure
        
def display(my_name_list):
    for name in my_name_list:
        print(name)
    #next name
#end procedure

choice = display_menu()

if choice == 2:
    display(name_list)
#end if
    
