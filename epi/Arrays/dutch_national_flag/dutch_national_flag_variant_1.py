"""
Assuming that keys take one of three values, reorder the array so that all objects with
the same key appear together. The order of subarrays is not important.
Use O(1) additional space and O(n) time.

Time: O(n)
Space: O(1)
"""
"""
Analysis

A[:k1]  = key1
[k1:k2] = key2
[k2:k3] = Unclassified
[k3:] = key3
"""

def partition_3_keys(keys, A):
    i1, i2, i3 = 0, 0, len(A)-1
    while i2 <= i3:
        if A[i2] == keys[0]:
            A[i1], A[i2] = A[i2], A[i1]
            i1 += 1
            i2 += 1
        elif A[i2] == keys[1]:
            i2 += 1
        elif A[i2] == keys[2]:
            A[i2], A[i3] = A[i3], A[i2]
            i3 -= 1

A = [0, 0, 2, 1, 2, 1]
keys = [0,1,2]

partition_3_keys(keys, A)
print(A)