"""
Given an array A of n objects with Boolean-valued keys, reorder the array
so that objects that have the key false appear first.
Use O(1) additional space and O(n) time.

Time: O(n)
Space: O(1)
"""
"""
Analysis

A[:k1]  = key1
[k1:k2] = Unclassified
[k2:] = key2
"""

def partition_boolean(keys, A):
    i1, i2 = 0, len(A) - 1
    while i1 <= i2:
        if A[i1] == keys[0]:
            i1 += 1
        elif A[i1] == keys[1]:
            A[i1], A[i2] = A[i2], A[i1]
            i2 -= 1


A = [True,False,True,False,False]
keys = [False, True]

partition_boolean(keys, A)
print(A)