# LC 26 — Two Sum
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approach: Loop through the array, check if the current element
# is different from the previous one, and update the array.
# Time: O(n)
# status: sloved in 6 min 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i +=1
                nums[i] = nums[j]
        return i + 1
