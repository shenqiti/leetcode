'''
66. Plus One

数组和动态数组系列：
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.


By:shenqiti
2019/8/1
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number = ""
        List = []
        for each in digits:
            number += str(each)
        number = str(int(number) + 1)
        for each in number:
            List.append(int(each))

        return List

dd = Solution()
digits = [1,2,3]
result = dd.plusOne(digits)
print(result)




# class Solution:
#     def plusOne(self, digits):
#         # Adding 1 to the last element of the list.
#         digits[-1] += 1
#
#         # Lets iterate over all the elements of in reverse order.
#         for i in range(len(digits) - 1, -1, -1):
#             # calculate the carry that should be added to the element before this
#             carry = digits[i] // 10
#
#             # Replace the digit in the current position so that only one digit is present.
#             digits[i] %= 10
#
#             # if carry is not 0(means it is 1) and the index is not 0 (means we can simply add the carry to the previous element
#             if carry != 0 and i != 0:
#                 digits[i - 1] += carry
#
#         # we have finished traversing the entire list but we still hold a carry.
#         # Create a new list node and insert it before 0th index. The valye in the node is 'carry'
#         if carry:
#             digits.insert(0, carry)
#         return digits
