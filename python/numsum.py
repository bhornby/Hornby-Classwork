def numsum(n):
    if n > 0:
        total =0
        total = total + n
        numsum(n - 2)
    else:
        print(total)
    #end if
#end procedure
        
#numsum(6)

def calcsum(n):
    if n==0:
        return n
    return n +calcsum(n-2)

sum = calcsum(10)
print(sum)