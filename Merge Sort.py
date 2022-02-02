# Binary Search eliminates half a list each iteration
# Very good for searching ordered list of elements
# Could be good for searching products on eCommerce Websites?

# Binary Search runs in Logarithmic time
# -> O(log n) notation
# 100 items -> 7 Guesses
# 4,000,000,000 items -> 32 Guesses

def merge_sort(list, size): 
    left = 0
    right = size-1
    partition_list(list, left, right)
    return list
    
def partition_list(list, left, right):
    if(round(left) < round(right)):
        middle = (left + ((right-left)/2))
        partition_list(list, left, middle)
        partition_list(list, middle+1, right)
        merge_list(list, left, middle, right)
    else:
        return

def merge_list(list, left, middle, right):
    a = middle - left + 1
    b = right - middle

    left_list = []
    right_list = []

    for i in range(0,int(a)):
        left_list.append(list[int(left)+int(i)])
        left_list[i] = list[int(left)+int(i)]
        
    for j in range(0,int(b)):
        right_list.append(list[int(middle) + 1 + int(j)])
        right_list[j] = list[int(middle) + 1 + int(j)]

    k = int(0)
    l = int(0)
    m = int(left)

    while (k < int(a)) & (l < int(b)):
        if(left_list[k] <= right_list[l]):
            list[m] = left_list[k]
            k = k+1
        else:
            list[m] = right_list[l]
            l = l+1
        m = m+1
    
    while k < int(a):
        list[m] = left_list[k]
        k = k+1
        m = m+1

    while l < int(b):
        list[m] = right_list[l]
        l = l+1
        m = m+1
        

my_list = [3, 7, 9, 1, 5]

print()
print("Starting the program: ")
print()
print(my_list)
print("Merge Sorting....")
print(merge_sort(my_list, len(my_list))) # => 1 
