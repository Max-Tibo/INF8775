import sys
import time
import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from quick import quickSort
from quickSeuil import quickSortSeuil
from quickRandomSeuil import quickSortRandomSeuil
from counting import countingSort
from copy import deepcopy

def read_integers(filename):
    with open(filename) as f:
        array = list(map(int, f))
        return array

# create the power test from a results csv file
# based on the moodle "guide bash"
def power_test(csvfile, serie):
    df = pd.read_csv(csvfile).groupby(['Sample_Sizes','Algorithms']).mean().reset_index()

    g = sns.FacetGrid(df, hue='Algorithms', height=6, aspect=1)
    g = g.map(plt.plot, 'Sample_Sizes', 'Times')
    g.set(xscale='log')
    g.set(yscale='log')
    g.add_legend()
    plt.savefig('test_puissance' + serie)

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
with open('results' + input + '.csv', 'w', newline='') as myfile:
    columnTitles = ["Sample_Sizes", "Algorithms", "Times"]
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(columnTitles)

for size in sizes:
    sortTime1 = 0.0
    sortTime2 = 0.0
    sortTime3 = 0.0
    sortTime4 = 0.0
    for test in range(testset[0], testset[1]):
        file = "../../exemplaires/testset_" + str(size) + "_" + str(test) + ".txt"
        tempArray = read_integers(file)
        # execute the algorithms 
        # quickSort
        array1 = deepcopy(tempArray)
        sortTime1 = quickSort(array1)

        # quickSort with seuil
        array2 = deepcopy(tempArray)
        sortTime2 = quickSortSeuil(array2)

        # quickSort with seuil and random pivot
        for i in range(0, 10):
            array3 = deepcopy(tempArray)
            sortTime3 += quickSortRandomSeuil(array3)
        sortTime3 += (sortTime3/10)

        # countingSort
        array4 = deepcopy(tempArray)
        sortTime4 = countingSort(array4)
    
    sortTime1 = round(1000 * sortTime1/10, 3)
    times1.append(sortTime1)
    sortTime2 = round(1000 * sortTime2/10, 3)
    times2.append(sortTime2)
    sortTime3 = round(1000 * sortTime3/10, 3)
    times3.append(sortTime3)
    sortTime4 = round(1000 * sortTime4/10, 3)
    times4.append(sortTime4)

with open('results' + input + '.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range(0, len(sizes)):
        resultRow = []
        resultRow.append(sizes[i])
        resultRow.append("QuickSort")
        resultRow.append(times1[i])
        wr.writerow(resultRow)
        resultRow.clear()
        resultRow.append(sizes[i])
        resultRow.append("QuickSortSeuil")
        resultRow.append(times2[i])
        wr.writerow(resultRow)
        resultRow.clear()  
        resultRow.append(sizes[i])      
        resultRow.append("QuickSortRandomSeuil")
        resultRow.append(times3[i])
        wr.writerow(resultRow)
        resultRow.clear()
        resultRow.append(sizes[i])
        resultRow.append("CountingSort")
        resultRow.append(times4[i])
        wr.writerow(resultRow)
        resultRow.clear()        

power_test('results' + input + '.csv', input)
