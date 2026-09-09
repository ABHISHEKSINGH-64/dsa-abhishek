# LC 1470 — Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/submissions/2136695118/

# Approach: Split the array into two halves and add one element
# from each half one by one.
#
# Time: O(n)
# Space: O(n)
#
# Status: solved in 20 min / needed a hint / read the editorial



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        for i in range(n):
            result.append(nums[i])
            result.append(nums[i + n])

        return result