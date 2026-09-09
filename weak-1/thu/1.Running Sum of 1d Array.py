# LC 1480- Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Approach: Prefix sum
# Time: O(n)
# Status: solved in 15 min


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums