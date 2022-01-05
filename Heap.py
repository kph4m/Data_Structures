# HEAP
# Complete binary tree
# 2 types
#   Max Heap: parent node is greater than child nodes
#   Min Heap: parent node is less than child nodes
# Uses:
#   Priority Queues
#       Prim's  and Dijkstra's Algorithms
# TODO: Create Min Heap


# Heapify
# Used to create a max heap from a binary tree
# n - size of array
def heapify(arr, n, i):

    # set current element i as largest
    largest = i

    # index of left child = 2i+1
    leftChild = 2 * i + 1

    # index of right child = 2i+2
    rightChild = 2 * i + 2

    # if left child greater than current and less than size, set left child as largest
    if leftChild < n and arr[i] < arr[leftChild]:
        largest = leftChild

    # if right child greater than largest and less than size, set right child as largest
    if rightChild < n and arr[largest] < arr[rightChild]:
        largest = rightChild

    if largest != i:
        # swap largest with current element
        arr[i], arr[largest] = arr[largest], arr[i]

        # keep heapifying subtrees
        heapify(arr,n,largest)

# Insert
# Inserts element into the heap, following the heap properties
def insert(arr, data):
    size = len(arr)
    # If there is no root, add data
    if size == 0:
        arr.append(data)
    # If there is root
    else:
        # Insert the node at the end
        arr.append(data)
        # Heapify the array to follow heap properties
        for i in range((size//2)-1, -1, -1):
            heapify(arr, size, i)


# Delete
# Deletes element from heap, following the heap properties
def delete(arr, num):
    # Loop through to find position of num
    size = len(arr)
    i=0
    for i in range(0, size):
        if num == arr[i]:
            break
    
    # swap it with last element
    arr[i], arr[size-1] = arr[size-1], arr[i]

    # remove num
    arr.remove(num)

    # Heapify the array to follow heap properties
    for i in range((len(arr)//2)-1, -1, -1):
        heapify(arr, len(arr), i)


# TESTING

arr = []

# Insertion
insert(arr,3)
insert(arr,1)
insert(arr,5)
insert(arr,4)
insert(arr,2)

print("Expected output: 5, 4, 3, 1, 2")
print("Actual output: " + str(arr))

# Deletion
delete(arr, 3)
print("Expected output: 5, 4, 2, 1")
print("Actual output: " + str(arr))









