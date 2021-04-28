from random import randint
import time

t0 = time.time()
processtime = time.time()-t0
n = 0
p = 1*10^6

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        _item = array[i]
        j = i - 1
    

        while j >= 0 and array[j] > _item:
    
            array[j + 1] = array[j]
            j -= 1
    
        array[j + 1] = _item
    #next i
    return array

array = [n,p]


insertion_sort(array)
print("insertion sort:")
print("processing time = " + str(processtime))

print("run time = " + str(time.time()-t0-processtime))

