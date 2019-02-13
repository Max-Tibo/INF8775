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
