# Example Python program that finds the largest n elements

# from a Python iterable

from heapq import nlargest

 

iterable = [6,1,7,9,3,5,4]

selectCount = 4

largests = nlargest(selectCount, iterable)

print(largests)