from random import randint
import time

t0 = time.time()
processtime = time.time()-t0

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

array = [randint(0, 1000) for i in range(1000)]


insertion_sort(array)

print(processtime)

print(time.time()-t0-processtime)

