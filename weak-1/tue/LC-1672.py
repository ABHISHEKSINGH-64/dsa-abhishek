# LC 1672 — Two Sum
# https://leetcode.com/problems/richest-customer-wealth/description/
# Approach: Loop through the matrix, find the sum of each row, compare it with richest, and update richest.
# Time: O(m * n)
# Space: O(1)/iam used AI to to get space complexcity
# Status: solved in 12 min


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0

        for customer in accounts:
            wealth = 0

            for money in customer:
                wealth += money

            if wealth > richest:
                richest = wealth

        return richest


# Approach

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:

#         richest = 0

#         for customer in accounts:
#             richest = max(richest, sum(customer))

#         return richest
    