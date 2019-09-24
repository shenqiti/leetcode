'''
350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]


By:shenqiti
2019/9/24

'''

from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        NUM1 = Counter(nums1)
        NUM2 = Counter(nums2)
        intersection = []
        for each in NUM2:
            if each in NUM1:
                for i in range(0,min(NUM2[each],NUM1[each])):
                    intersection.append(each)
        return intersection


dd = Solution()
nums1 = [9,4,9,8,4]
nums2 = [4,9,5]
result = dd.intersect(nums1,nums2)
print(result)
