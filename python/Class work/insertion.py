from random import randint
import time

n = 10^9
array = [randint(0,n) for i in range(0,n)]

start_time = time.time()


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

duration = time.time() - start_time
print(array)
insertion_sort(array)
print("insertion sort:")
print("run time = " + str(duration))
print(array)