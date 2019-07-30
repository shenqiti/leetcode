'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

By : shenqiti
2019/7/30
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums = sorted(nums)

        last_number = None

        for i in range(0,len(nums)):
            if nums[i]>0:
                break
            elif nums[i] == last_number:
                continue

            l,r = i+1,len(nums)-1

            while l<r:
                rest = nums[i] + nums[l] + nums[r]
                if rest <0:
                    l += 1
                elif rest>0:
                    r -=1
                else:
                    solution.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
            last_number = nums[i]

        return solution


dd = Solution()
nums = [0,0,0,0]
result = dd.threeSum(nums)
print(result)



