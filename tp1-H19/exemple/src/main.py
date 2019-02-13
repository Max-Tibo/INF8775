import sys
import time
import csv
from quick import quickSort
from quickSeuil import quickSortSeuil
from quickRandomSeuil import quickSortRandomSeuil
from counting import countingSort

#ex_path = sys.argv[1] # Path de l'exemplaire
def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

# Algo ici
sizes = [1000, 5000, 10000, 50000, 100000, 500000]
while True:
    input = input("Enter testset 1-3: ")
    testset = []
    if input == "1":
        testset = [0, 9]
        break
    elif input == "2":
        testset = [10, 19]
        break
    elif input == "3":
        testset = [20, 29]
        break
    else:
        print("Invalid testset!")

# temp matrix to store algo execution times
times1 = [] # quick
times2 = [] # quickSeuil
times3 = [] # quickRandomSeuil
times4 = [] # coutning

# open csv file to write results
with open('results.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(sizes)

for size in sizes:
    sortTime1 = 0
    sortTime2 = 0
    sortTime3 = 0
    sortTime4 = 0
    for test in range(testset[0], testset[1]):
        file = "exemplaires/testset_" + str(size) + "_" + str(test) + ".txt"
        # execute the algorithms 
        # quickSort
        array1 = read_integers(file)
        startTime1 = time.time()
        quickSort(array1, 0, len(array1) - 1)
        endTime1 = time.time()
        sortTime1 += endTime1 - startTime1

        # quickSort with seuil
        array2 = read_integers(file)
        startTime2 = time.time()
        quickSortSeuil(array1, 0, len(array1) - 1)
        endTime2 = time.time()
        sortTime2 = endTime2 - startTime2

        # quickSort with seuil and random pivot
        for i in range(0, 10):
            array3 = read_integers(file)
            startTime3 = time.time()
            quickSortRandomSeuil(array1, 0, len(array1) - 1)
            endTime3 = time.time()
            sortTime3 += endTime3 - startTime3
        sortTime3 += (sortTime3/10)

        # countingSort
        array4 = read_integers(file)
        startTime4 = time.time()
        countingSort(array4)
        endTime4 = time.time()
        sortTime4 += endTime4 - startTime4
    
    sortTime1 = round(sortTime1/10, 6)
    times1.append(sortTime1)
    sortTime2 = round(sortTime2/10, 6)
    times2.append(sortTime2)
    sortTime3 = round(sortTime3/10, 6)
    times3.append(sortTime3)
    sortTime4 = round(sortTime4/10, 6)
    times4.append(sortTime4)

with open('results.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(times1)
    wr.writerow(times2)
    wr.writerow(times3)
    wr.writerow(times4)


#options = sys.argv[2:]
#if '-p' in options: # On imprime les nombres triés
#    print("1 2 3 4 7") # Données bidon, mais output du bon format demandé
#if '-t' in options: # On imprime le temps d'exécution
#    print("4.1347628746") # Données bidon, mais output du bon format demandé