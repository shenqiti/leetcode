'''
414. Third Maximum Number
数组和动态数组系列：
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).

By : shenqiti
2019/7/31

'''


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = {}.fromkeys(nums).keys()
        nums = list(nums)
        if len(nums)<3:
            return max(nums)
        else:
            nums.pop(nums.index(max(nums)))
            nums.pop(nums.index(max(nums)))
            return (nums.pop(nums.index(max(nums))))


dd = Solution()
nums = [3, 2, 2,1]
result = dd.thirdMax(nums)
print(result)
