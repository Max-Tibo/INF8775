import sys
import time

def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

def countingSort(array):
    maxValue = max(array)
    tempArray = [0 for x in range(maxValue + 1)]

    for value in array:
        tempArray[value] += 1
    
    array.clear()
    for i in range(maxValue + 1):
        for j in range(tempArray[i]):
            array.append(i)

if len(sys.argv) > 1:
    ex_path = sys.argv[1] # Path de l'exemplaire
    options = sys.argv[2:]
    # Algo ici
    file = ex_path
    # execute the algorithms 
    # countingSort
    sortTime = 0.0
    array = read_integers(file)
    startTime = time.time()
    countingSort(array)
    endTime = time.time()
    sortTime = endTime - startTime

    if '-p' in options: # On imprime les nombres triés
        print(array)
    if '-t' in options: # On imprime le temps d'exécution
        print(round(sortTime, 10))