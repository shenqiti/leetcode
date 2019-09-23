'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


By:shenqiti
2019/9/23


'''
from collections import Counter

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        N1 = Counter(nums1)
        N2 = Counter(nums2)
        intersection = []
        for each in N1:
            if each in N2:
                intersection.append(each)
        return intersection
dd = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = dd.intersection(nums1,nums2)
print(result)
