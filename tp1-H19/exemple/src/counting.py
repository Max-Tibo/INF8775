def countingSort(array):
    maxValue = max(array)
    tempArray = [0 for x in range(maxValue + 1)]

    for value in array:
        tempArray[value] += 1
    
    array.clear()
    for i in range(maxValue + 1):
        for j in range(tempArray[i]):
            array.append(i)