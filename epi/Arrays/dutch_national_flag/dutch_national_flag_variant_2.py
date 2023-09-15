"""
Given an array A of n objects with keys that takes one of four values, reorder the array
so that all objects that have the same key appear together.
Use O(1) additional space and O(n) time.

Time: O(n)
Space: O(1)
"""
"""
Analysis

A[:k1]  = key1
[k1:k2] = key2
[k2:k3] = key3
[k3:k4] = Unclassified
[k3:]   = key4
"""

def partition_4_keys(keys, A):
    i1, i2, i3, i4 = 0, 0, 0, len(A)-1
    while i3 <= i4:
        if A[i3] == keys[0]:
            A[i1], A[i3] = A[i3], A[i1]
            i1 += 1
            i2 += 1
            i3 += 1
        elif A[i3] == keys[1]:
            A[i2], A[i3] = A[i3], A[i2]
            i2 += 1
            i3 += 1
        elif A[i3] == keys[2]:
            i3 += 1
        elif A[i3] == keys[3]:
            A[i3], A[i4] = A[i4], A[i3]
            i4 -= 1

A = [0, 0, 2, 1, 3, 3, 1, 2]
keys = [0,1,2,3]

partition_4_keys(keys, A)
print(A)