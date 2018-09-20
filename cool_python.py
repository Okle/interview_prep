# List of Strings to a String
listOfStrings = ['One', 'Two', 'Three']
strOfStrings = ''.join(listOfStrings)
print(strOfStrings)

# List Of Integers to a String
listOfNumbers = [1, 2, 3]
strOfNumbers = ''.join(str(n) for n in listOfNumbers)
print(strOfNumbers)


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(lambda x: x*x)(x) for x in myList])
# f = lambda x: x*x
# [f(x) for x in range(10)]

# Method to split up your lists into chunks
def chunks(list, chunkSize):
    """Yield successive chunkSize-sized chunks from list."""
    for i in range(0, len(list), chunkSize):
        yield list[i:i + chunkSize]

# Use your `chunks` function to print out chunks of the same size
import pprint
pprint.pprint(list(chunks(range(10, 75), 10)))

# Set up your list and chunk size
myList = range(0, 50)
chunk = 5

# Split up your list into chunks
[list[i:i + chunk] for i in range(0, len(list), chunk)]

# Your initial list of lists
myList = [[1,2],[3,4],[5,6]]

# Flatten out your original list of lists with `sum()`
sum(myList, [])

# You can reduce the lists of lists of lists like this
from functools import reduce
print(reduce(lambda x, y: x+y, myList))

# Or you can use list comprehension
print([item for sublist in myList for item in sublist])

# for sublist in myList:
#   for item in sublist:
#     list1.append(item)


list1 = [1, 6, 7, 10, 13, 28, 32, 41, 58, 63]
list2 = [[13, 17, 18, 21, 32], [7, 11, 13, 14, 28], [1, 5, 6, 8, 15, 16]]

# Intersect both lists with list comprehension
intersection = [list(filter(lambda x: x in list1, sublist)) for sublist in list2]

# Print the result of the intersection
print(intersection)


# An intersection of both lists, stored in `intersection`
intersection = [[x for x in sublist if x in list1] for sublist in list2]

# Print the result of the intersection
print(intersection)

# Note that for these two approaches to work, your list should not contain other lists
# Make use of the list and set data structures
print(list(set(list1) & set(list2)))

# Use `intersection()`
print(list(set(list1).intersection(list2)))