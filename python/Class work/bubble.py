import time

t0 = time.time()
processtime = time.time()-t0
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that terminates early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

              
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array
array = [randint(0, 1000) for i in range(1000)]

bubble_sort(array)

print(processtime)

print(time.time()-t0-processtime)
