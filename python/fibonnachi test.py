### SRC - This looks good. What kind of performance difference did you get?
import time
starttime1 = time.perf_counter()
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    #end if
#end function
endtime1 = time.perf_counter()

starttime2 = time.perf_counter()
def fib2(n):
    fibNumbers = (0,1)
    for i in range(2,n):
        fibNumbers.appends(fibNumbers[i-1] + fibNumbers[i - 2])
    #next i
    return fibNumbers[n]
#end function
endtime2 = time.perf_counter()

fib(30)
fib2(30)
print(endtime2 - starttime2)

print(endtime1 - starttime1)
