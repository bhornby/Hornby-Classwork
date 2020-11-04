'''
for i in range(10):
    print('* ', end='')
#nexti
print('')
for i  in range(5):
    print('* ', end='')
#nexti
print('')
for i in range(20):
    print('* ', end= '')
#nexti
'''
'''
for i in range(10):
    print('')
    print('* ',end='')
    for x in range(10):
        print('* ',end='')
    #nextx
#nexti
'''
'''
for i in range(10):
    print('')
    print('* ',end='')
    for x in range(5):
        print('* ',end='')
    #nextx
#nexti
'''
'''
for x in range(10):
    for y in range(10):
        print(x, end="") # using x will result in vertical columns and using y will give horisontal rows
    # next y
    print()
#next x
'''
'''
for i in range(10):
    for j in range(i + 1):
            print(j,end = '')
    print('')
'''
'''
for row in range(10):
    
    for j in range(10-row):
        print(j,end='')
    
    for i in range(row):
        print('',end='')
        
    print('')
#next row
'''
'''
for row in range(10):
 
    for j in range(row):
        print (" ",end=" ")
 
    for j in range(10-row):
        print (j,end=" ")
 
    print()
'''
'''
for i in range(1,10):
    for j in range(1,10):
        #extra space
        if i*j < 10:
            print(' ',end='')
        
        print(i*j,end = ' ')
    #nextj
    print()
    
'''
'''
for i in range(1,10):
    for j in range(1,10):
        # Extra space?
        if i*j < 10:
            print (" ",end="")
 
        print (i*j,end=" " )
 
    # Move down to the next row
    print()
'''

for i in range(1,10):
    for j in range(1+i):
        print(j,end='')
    print()
    
    
