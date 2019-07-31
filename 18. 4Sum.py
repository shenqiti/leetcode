'''

18. 4Sum
Given an array nums of n integers and an integer target, are there elements a, b, c,
and d in nums such that a + b + c + d = target? Find all unique quadruplets
in the array which gives the sum of target.

By:shenqiti
2019/7/31
'''


class Solution:


    def fourSum(self, nums,target):
        nums = sorted(nums)

        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    if target < nums[i] + nums[j] + nums[k] + nums[l]:
                        l -= 1
                    elif target > nums[i] + nums[j] + nums[k] + nums[l]:
                        k += 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        l -= 1
                        k += 1

        res1 = []
        for i in res:
            if i not in res1:
                res1.append(i)

        return res1

dd = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = dd.fourSum(nums,target)
print(result)
