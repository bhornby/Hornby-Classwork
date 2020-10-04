import time

'''startTime1 = time.time()

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
endTime1 = time.time()
print(endTime1 - startTime1)'''    


startTime2 = time.time()

def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
    # now append the sum of the two previous numbers to the list    
    for i in range(2,n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])       
    return fibNumbers[n]

endTime2 = time.time()
print(endTime2 - startTime2) 


#(fib(10))
(fibonacci2(10))

# def fib = 9.5367431640625e-07
# def fibonacci2 = 1.1920928955078125e-06