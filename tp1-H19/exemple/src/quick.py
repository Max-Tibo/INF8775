import sys
import time

def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

def quickSort(array, start, end):
    if start < end:
        pivot = array[start]
        index = start
        for i in range (start + 1, end + 1):            
            if array[i] < pivot:
                index += 1
                array[index], array[i] = array[i], array[index]

        array[start], array[index] = array[index], array[start]
        quickSort(array, start, index - 1)
        quickSort(array, index + 1, end)

ex_path = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]
# Algo ici
file = ex_path
# execute the algorithms 
# quickSort
sortTime = 0.0
array = read_integers(file)
startTime = time.time()
quickSort(array, 0, len(array) - 1)
endTime = time.time()
sortTime = endTime - startTime

if '-p' in options: # On imprime les nombres triés
    print(array)
if '-t' in options: # On imprime le temps d'exécution
    print(round(sortTime, 10))