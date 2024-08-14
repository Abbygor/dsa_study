"""
https://www.codingninjas.com/studio/problems/count-inversions_615

For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] &gt; 'ARR[j]' 
2. 'i' &lt; 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').

Example:
ARR = [3,2,1]
Output: 3
Explanation: [3,2], [2,1], [3,1]

Example:
ARR = [2,5,1,3,4]
Output: 4
Explanation: [2,1], [5,1], [5,3], [5,4]

"""

def getInversions(arr, n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                print(arr[i], arr[j])
                count += 1
    return count

arr = [2,5,1,3,4]
n = 5
print(getInversions(arr, n))