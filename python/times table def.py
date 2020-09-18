def multiples(table:int,start_num:int,end_num:int,pupil_name:str): #something called type hints 
    
    print("Hi "+ pupil_name + " ... Here is your times table")
    
    for i in range(start_num, end_num+1):
        print(table, 'x', i, '=', table*i)
    #next value 
#end procedure

#main program
pupil_name = input("What is your name? ")

table = int(input("Enter Times Table "))
start_num = int(input("Enter Start Number "))
end_num =int(input("Enter End Number "))

multiples(table,start_num,end_num,pupil_name)


        