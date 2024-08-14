"""
https://www.interviewbit.com/problems/repeat-and-missing-number-array/

You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.

Example:
Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

Time: O(n)
Space: O(n)
"""

def repeatedNumber(A):
    tmp = [0] * (len(A) + 1)
    for n in A:
        tmp[n] += 1
    res = [0,0]
    for i in range(len(tmp)):
        if tmp[i] > 1:
            res[0] = i
        if tmp[i] == 0:
            res[1] = i
    return res

A = [3,1,2,5,3]
print(repeatedNumber(A))

A = [3,1,2,5,4,4]
print(repeatedNumber(A))