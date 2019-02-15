import sys
import time

def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

def sortingAlgo(array, start, end):
    if start < end:
        pivot = array[start]
        index = start
        for i in range (start + 1, end + 1):            
            if array[i] < pivot:
                index += 1
                array[index], array[i] = array[i], array[index]

        array[start], array[index] = array[index], array[start]
        sortingAlgo(array, start, index - 1)
        sortingAlgo(array, index + 1, end)

def quickSort(array):
    elapsedTime = 0.0
    startTime = time.time()
    sortingAlgo(array, 0, len(array) - 1)
    endTime = time.time()
    elapsedTime = endTime - startTime
    return elapsedTime

if len(sys.argv) > 1:
    ex_path = sys.argv[1] # Path de l'exemplaire
    options = sys.argv[2:]
    # Algo ici
    file = ex_path
    # execute the algorithms 
    # quickSort
    sortTime = 0.0
    array = read_integers(file)
    startTime = time.time()
    sortTime = quickSort(array)

    if '-p' in options: # On imprime les nombres triés
        print(array)
    if '-t' in options: # On imprime le temps d'exécution
        print(round(sortTime, 10))