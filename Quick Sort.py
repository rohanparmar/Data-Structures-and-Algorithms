def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        
        lesser = [i for i in array[1:] if i<=pivot]
        
        greater = [i for i in array[1:] if i>pivot]
        
        return quicksort(lesser) + [pivot] + quicksort(greater)
    
print(quicksort([0,1,5,3,9,15,2,19,17,24,11,6]))