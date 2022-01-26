# Binary Search eliminates half a list each iteration
# Very good for searching ordered list of elements
# Could be good for searching products on eCommerce Websites?

# Binary Search runs in Logarithmic time
# -> O(log n) notation
# 100 items -> 7 Guesses
# 4,000,000,000 items -> 32 Guesses

def binary_search(list, item): 
    
    low = 0
    high = len(list) - 1
    
    while low <= high: 
        mid = (low + high) 
        guess = list[mid] 
        
        if guess == item:
            return mid
        
        if guess > item: 
            high = mid - 1

        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print()
print("Starting the program: ")
print()
print("Searching for : 3 ")
print(binary_search(my_list, 3)) # => 1 
print("Searching for : -1 ")
print (binary_search(my_list, -1)) # => None