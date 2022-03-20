# CODE for Binary Search using Recursion 

def binary_search(list, to_find):
    
    mid = len(list)//2
    
    if len(list) == 1:
        return mid if list[mid] == to_find else None
    
    if list[mid] == to_find:
        return mid
    
    else:
        
        if list[mid] < to_find:
            return(mid + binary_search(list[mid:], to_find)) if binary_search(list[mid:], to_find) is not None else None
    
        else:
            return(binary_search(list[:mid], to_find))

sample_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(binary_search(sample_list, 7))