'''

213. House Robber II
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
 determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

In House Robber, we can calculate the maximum loot using odd and even indices. Similarly, we can approach this. Only catch in this problem is that the first and last houses cannot be robbed together. Think of it like a circle. So, essentially, you cannot rob adjacent houses.

So, we run two passes.
First pass, start from the first house but ignore the last house. [0:len(nums)-1]
Second pass, start from the second house till the last house. [1:len(nums)]
In this way, we never loot the first and last houses together.

Finally, just return the maximum of both.


By:shenqiti
2019/8/12

'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))

dd = Solution()
nums = [1,2,3,4,5]
result = dd.rob(nums)
print(result)
