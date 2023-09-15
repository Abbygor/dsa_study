"""
Write a program which takes as input an array of digits encoding a nonnegative decimal integer D
and updates the array to represent the integer D + 1.
For example if the input is [1,2,0] then you should update the array to [1,3,0]

Time: O(n)
Space: O(1)
"""
"""
Analysis

[1,2,9]
Start with the less significant digit -> 9
so you can reverse the array to -> [9, 2, 1]
in this case if you need to add one more digit for example [9,9,9] + 1 -> [1,0,0,0]
you only need to append a [0] to the end (append is constant time)

"""

def plus_one(D):
    D[-1] += 1
    # only iterate until start + 1
    for i in (range(len(D) - 1, 0, -1)):
        if D[i] != 10:
            break
        D[i] = 0
        D[i - 1] += 1
    if D[0] == 10:
        D[0] = 1
        D.append(0)
 

D = [1,2,9]
E = [9,9,9]

plus_one(D)
plus_one(E)
print(D)
print(E)