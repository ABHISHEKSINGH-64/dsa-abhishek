# LC-283 Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Approach:- se i to check each element and j to keep the position for the next non-zero element; when a non-zero is found, swap it with nums[j] and move j forward.
# Time: O(n)
# Space: O(1)
# Status: solved in 5 min


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:

        n = len(nums)
        j = 0

        for i in range(n):

            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1