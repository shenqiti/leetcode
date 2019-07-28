'''

1.Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
________________________________________
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
_________________________________________
By : shenqiti
2019/7/28

'''



class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,n in enumerate(nums):
            temp = target - n
            if temp in d:
                return (d[temp],i)
            else:
                d[n] = i

dd = Solution()
nums = [2,7,11,15]
target = 17
result = dd.twoSum(nums,target)
print(result)
