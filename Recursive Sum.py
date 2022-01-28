# Recursive addition
# Basic idea: Go down the recursive function till the last element is reached
# Recursively add it in return statements

def sum(arr):
    if(len(arr) == 1):
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

print(sum([1,2,3]))