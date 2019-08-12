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

By:shenqiti
2019/8/12

'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # four nums: max value when
        # first is robbed, last is robbed
        # first is robbed, last is not robbed
        # first is not robbed, last is robbed
        # first is not robbed, last is not robbed
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2 or n ==3:
            return max(nums)
        ans = [nums[0]+nums[2],nums[0],nums[2],nums[1]]
        for i in range(3,n):
            temp = [0,0,0,0]
            temp[0] = ans[1]+nums[i]
            temp[1] = max(ans[0],ans[1])
            temp[2] = ans[3]+nums[i]
            temp[3] = max(ans[2],ans[3])
            ans,temp = temp,ans
        return max(ans[1:])



dd = Solution()
nums = [2,3,2]
result = dd.rob(nums)
print(result)
