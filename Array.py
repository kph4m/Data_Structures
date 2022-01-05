# ARRAY IN PYTHON

# Array is a data structure that stores a fixed number of elements of the same data type in contiguous, adjacent memory.

# Usage: All elements are of the same type and not planning to expand array size

# Arrays can be created in Python using
    # List: can store any types of data
    # Array module: all elements are the same type (preferred)

# import Array module
import array as arr

# CREATION

# Creating Array with List
numList = [1,3,5]

# Creating Array with Array module
numArr = arr.array('i', [1,3,5])


# OPERATIONS

print('Original Array: ' + str(numArr))

# Access
# Time complexity: O(1)
print('Access Test: get index 1 element')
print('Expected Output: 3')
print('Actual Output: ' + str(numArr[1]))


# Insertion
# Time complexity: O(n)
numArr.insert(1,2)
print('Insertion Test: inserting 2 at index 1')
print('Expected Output: [1,2,3,5]')
print('Actual Output: ' + str(numArr))


# Deletion
# Time complexity: O(n)
numArr.remove(3)
print('Deletion Test: removing 3')
print('Expected Output: [1,2,5]')
print('Actual Output: ' + str(numArr))

# Update
# Output: [1,2,6]
# Time complexity: O(1)
numArr[2] = 6
print('Update Test: changing index 2 to 6')
print('Expected Output: [1,2,6]')
print('Actual Output: ' + str(numArr))

# Slicing
# Time complexity: O(n)
numArrSlice = numArr[0:2]
print('Slicing Test: getting values from index 0-1')
print('Expected Output: [1,2]')
print('Actual Output: ' + str(numArrSlice))

# Search
# Time complexity: O(n)
print('Search Test: find index position where 2 is located')
print('Expected Output: 1')
print('Actual Output: ' + str(numArr.index(2)))