"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Time: O(n)
Space: O(n)

"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashMap = dict()
    for i in range(len(nums)):
        if (target - nums[i]) in hashMap:
            return [i, hashMap[target -nums[i]]]
        else:
            hashMap[nums[i]] = i

nums = [2,7,11,15]
target = 9

res = twoSum(nums, target)
print(res)