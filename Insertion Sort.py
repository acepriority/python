# Set pointer to second item in the list
# Repeat
#     Select the first item in unsorted section and make it current
#     Repeat
#         Compare current item with next item in sorted section
#         Move sorted item one place to the right if bigger than current item
#     Until sorted item is smaller than current item or all sorted items checked
#     Insert current item into sorted section
#     Advance the pointer 
# Until unsorted section is empty

def InsertionSort(A): 
    for i in range(1, len(A)): 
        temp = A[i] 
        k = i 
        while k > 0 and temp < A[k - 1]: # temp > A[k - 1] will give you a desending order
            A[k] = A[k - 1] 
            k -= 1 
            A[k] =  temp

A= [54, 26, 93, 17, 77, 3, 44, 55, 20]
InsertionSort(A)
print(A)