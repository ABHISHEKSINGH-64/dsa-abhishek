# LC-217 Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Approach: Store each number in a set and check if it is already there.
# Time: O(n)
# Space: O(n)
# status: sloved in 14 min


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        target = set()

        for num in nums:
            if num in target:
                return True
            target.add(num)
        return False
