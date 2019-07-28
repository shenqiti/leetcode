'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
_______________________________________________________
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

________________________________________________________
By : shenqiti
2019/7/28

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num_list = nums1 + nums2
        num_list_rev = sorted(num_list)
        a = num_list_rev[len(num_list_rev)//2 - 1]
        b = num_list_rev[len(num_list_rev)//2 ]
        if len(num_list_rev)%2 == 0:
            return ((a+b)/2)
        else:
            return b


dd = Solution()
nums1 = [1,2]
nums2 = [3,4]
result = dd.findMedianSortedArrays(nums1,nums2)
print(result)
