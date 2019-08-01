'''
238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array

output such that output[i] is equal to the product of all the elements of nums except nums[i].

___________________________
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

__________________________

By:shenqiti
2019/8/1
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # The length of the input array 
        length = len(nums)

        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all 
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer






dd = Solution()
nums = [1,0,2]
result = dd.productExceptSelf(nums)
print(result)


# class Solution:
#     def productExceptSelf(self, nums):
#         res, l, r = [1] * len(nums), 1, 1
#         for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
#             res[i], l = res[i] * l, l * nums[i]
#             res[j], r = res[j] * r, r * nums[j]
#         return res

# class Solution(object):
# #     def productExceptSelf(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: List[int]
# #         """
# #         start, end, n = 1, 1, len(nums)
# #         out = [1]*n
# #         for i in range(len(nums)):
# #             out[i] *= start
# #             start *= nums[i]
# #             out[n-i-1] *= end
# #             end *= nums[n-i-1]
# #         return out



