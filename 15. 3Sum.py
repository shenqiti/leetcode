'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

By : shenqiti
2019/7/30
'''



class Solution:
    def threeSum(self, nums):
        nums.sort()
        last_number = None
        result = []

        for i in range(0, len(nums)):
            print(i)

            if nums[i] > 0:
                break
            elif nums[i] == last_number:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                rest = nums[i] + nums[l] + nums[r]
                if rest < 0:
                    l += 1
                elif rest > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
            last_number = nums[i]

        return result
dd = Solution()
nums = [-1, 0, 1, 2, -1, -4]
result = dd.threeSum(nums)
print(result)


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         solution = []
#         j = 1
#         i = 0
#         k = 2
#         while i<len(nums)-2 :
#             if nums[i] + nums[j] == -1*nums[k]:
#                 solution.append(sorted([nums[i],nums[j],nums[k]]))
#
#             if k == len(nums)-1:
#                 j += 1
#                 k = j
#             if j == len(nums)-1:
#                 i += 1
#                 j = i + 1
#                 k = j
#             k += 1
#         solution2 = []
#         for each in solution:
#             if each not in solution2:
#                 solution2.append(each)
#         return solution2
