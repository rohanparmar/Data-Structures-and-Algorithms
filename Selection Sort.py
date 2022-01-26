# Selection Sort 
# Very good for Sorting when memory write is a costly operation in terms of time or hardware durability
# It performs very well on small lists.
# It is an in-place algorithm. It does not require a lot of space for sorting. Only one extra space is required for holding the temporal variable.
# It performs well on items that have already been sorted.

# Selection Sort runs in Quadratic time
# -> O(n^2) notation

def findSmallest(arr): 
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i] 
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print (selectionSort([5, 3, 6, 2, 10]))