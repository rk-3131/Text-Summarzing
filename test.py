# Example Python program that finds the largest n elements

# from a Python iterable

import heapq

 

iterable = [6,1,7,9,3,5,4]

selectCount = 4

largests = heapq.nlargest(selectCount, iterable)

print(largests)