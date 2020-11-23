# to show which times table the user specifies
# tt =  times table
times_table = 0
valid_times_table = False
import time
valid_user_validation = False
# proper validation has no stings
        
        
# .issdigit is used to validate if a sting entered is a digit or not, this is a method
while not valid_times_table:
    times_table = input("what table [1-20]?")
    
    if times_table.isdigit() and int(times_table)> 0 and int(times_table)<=20:# valid interger test
        times_table = int(times_table)
        valid_times_table = True
        #end if
#end while
        
# vertification by user]
#uv = user vertification
while not valid_user_validation:
    user_validation = input("you have chosen the "+str(times_table)+" times table [yes or no]" )
        
    if user_validation == "yes" :
        valid_user_validation = True
    
    elif user_validation == "no":
        times_table = input("re-enter your desired times table [1-20]")
    
    else:
        print("please enter a valid answer!")
    
        
        
        
    #end if
        

times_table = int(times_table)        
 
#multiplication program
if times_table>0 and times_table<=20:
    for i in range(1, 21):
        print(times_table, 'x', i, '=', times_table*i)
    #end for
#end if




