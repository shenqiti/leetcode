'''
16. 3Sum Closest
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

By : shenqiti
2019/7/30
'''



class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        last_i = None

        distance = nums[0]+nums[1]+nums[2]-target
        if distance == 0:
            return distance + target

        for i in range(0, len(nums)-2):
            if nums[i] == last_i:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
            	rest = nums[i]+nums[l]+nums[r]-target
            	if rest == 0:
            		return target
            	elif abs(rest) < abs(distance):
            		distance = rest

            	if rest < 0:
            		l += 1
            	else:
            		r -= 1
            last_i = nums[i]
        return distance+target

dd = Solution()
nums = [-1, 2, 1, -2]
target = 1
result = dd.threeSumClosest(nums,target)
print(result)
