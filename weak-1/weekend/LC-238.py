# LC-238 Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Approach: use prefix and suffix products; first store left product, then multiply by right product.
# Time: O(n)
# Space: O(1)
# Status: solved in 15 min


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        prefix = 1
        suffix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        for i  in range(n-1, -1, -1):
            answer[i] = suffix
            suffix *= nums[i]

        return answer
