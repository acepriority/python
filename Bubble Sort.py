# REPEAT number of items in the list -1 times
#     FOR each adjacent pair of items in the list
#         IF first of the pair > second of pair THEN 
#             Swap positions 
#         END IF 
#     NEXT pair of Items
# END REPEAT

def BubbleSort(list_a):   #this is an enhanced alternative bubble sort using a Boolean value.
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i]
        return list_a

list_a = [9, 12, 4, 3]

a = BubbleSort(list_a)

print(a)




