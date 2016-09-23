from random import randint

def partition(array, p, r):
    x = array[r]
    i = p-1

    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[r] = array[r], array[i+1]
    return i+1

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1, r)
    return array

def random_partition(array, p, r):
    i = randint(p,r)
    array[r], array[i] = array[i], array[r]
    return partition(array, p, r)

def random_quicksort(array, p, r):
    if p < r:
        q = random_partition(array, p, r)
        random_quicksort(array, p, q-1)
        random_quicksort(array, q+1, r)
    return array
