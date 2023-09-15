"""
Given an array A of n objects with Boolean-valued keys, reorder the array
so that objects that have the key false appear first.
The relative ordering of objects with key true should not change
Use O(1) additional space and O(n) time.

Time: O(n)
Space: O(1)
"""
"""
Analysis START FORM THE BACK

A[:k1]  = Unclassified
[k1:k2] = key1
[k2:] = key2
"""

def partition_boolean_order_matters(keys, A):
    i1, i2 = len(A) - 1, len(A) - 1
    while i1 >= 0:
        if A[i1] == keys[0]:
            i1 -= 1
        elif A[i1] == keys[1]:
            A[i1], A[i2] = A[i2], A[i1]
            i1 -= 1
            i2 -= 1

A = [True,False,True,False,False, True, False]
keys = [False, True]

partition_boolean_order_matters(keys, A)
print(A)