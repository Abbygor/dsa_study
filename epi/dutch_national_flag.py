"""
Write a program that takes an array A and index i into A, and rearranges the elements such
that all elements less than A[i] (the pivot) appear firt, followed by elemments equal to the pivot,
followed by elements grater than the pivot

Time: O(n)
Space: O(1)

"""

from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller, equal, larger = 0,0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

A = [-3, 0,-1,1,1,1,-4,5,3,4,2]
pivot_index = 1

dutch_flag_partition(pivot_index, A)
print(A)