from random import randint
import sys
import time

def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

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

ex_path = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]
# Algo ici
file = ex_path
# execute the algorithms 
# quickSortRandomSeuil
for i in range(0, 10):
    sortTime = 0.0
    array = read_integers(file)
    startTime = time.time()
    quickSortRandomSeuil(array, 0, len(array) - 1)
    endTime = time.time()
    sortTime += endTime - startTime
sortTime = round(sortTime/10, 10)

if '-p' in options: # On imprime les nombres triés
    print(array)
if '-t' in options: # On imprime le temps d'exécution
    print(sortTime)