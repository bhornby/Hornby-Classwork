
#menu display subroutine
def displayMenu():
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")
#end function
choice = displayMenu()    


user_choice =(input("Enter your choice: ")) 

name_list = [1,2,3,4,5,6,7,8,9,10]
### SRC - When you are doing validation, you need to have a
### loop. Something like while choice not valid:
if int(user_choice)>3 and int(user_choice)<1:
    user_choice =(input("Invalid choice - please re-enter: "))
    
elif user_choice == 1: ### SRC - user_choice is still a string and you are comparing to an interger
    print("Enter the name to be added to the list")
    name = input()
    print("Enter the name to be added to the list to insert the name (1 - 10):")
    posititon = input()
    ### SRC - Don't use insert. Use name_list[position] = name
    name_list.insert(position, name)
    
elif user_choice == 2:
    for nam in name_list:
        print(nam)
    #end for
        
elif user_choice == 3:
    print("program terminating")



    
    
    