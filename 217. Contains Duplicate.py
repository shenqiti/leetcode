'''
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true


By:shenqiti
2019/9/26

'''


class Solution:
	def containsDuplicate(self, nums):
		if not nums:
			return False

		return len(set(nums)) != len(nums)      # set cuts duplicates so len will be smaller if there are any


dd = Solution()
# nums = [1,1,1,3,3,4,3,2,4,2]
nums = []
result = dd.containsDuplicate(nums)
print(result)
