"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 
Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Link: https://leetcode.com/problems/range-sum-query-immutable/description/
Time = 
Space = 
"""
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        if left > 0:
            return self.nums[right] - self.nums[left - 1]
        else:
            return self.nums[right]



arr = [-2, 0, 3, -5, 2, -1]
# prefix = [-2, -2, 1, -4, -2, -3]
num_array = NumArray(arr)
print(num_array.sumRange(0, 2))
print(num_array.sumRange(2, 5))
print(num_array.sumRange(0, 5))



