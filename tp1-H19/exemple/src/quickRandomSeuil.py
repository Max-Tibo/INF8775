from random import randint

def quickSortRandomSeuil(array, start, end):
    rand = randint(start, end)
    if (end - start) <= 5:
        pivot = array[rand]
        index = start
        for i in range (start + 1, end + 1):            
            if array[i] < pivot:
                index += 1
                array[index], array[i] = array[i], array[index]

        array[start], array[index] = array[index], array[start]
        quickSortRandomSeuil(array, start, index - 1)
        quickSortRandomSeuil(array, index + 1, end)
    else:
        insertionSort(array, start, end)

# https://www.geeksforgeeks.org/insertion-sort/
def insertionSort(array, start, end): 
    for i in range(start + 1, end + 1): 
        pivot = array[i] 
        j = i - 1
        while j >= 0 and pivot < array[j] : 
            array[j + 1] = array[j] 
            j -= 1
        array[j + 1] = pivot
