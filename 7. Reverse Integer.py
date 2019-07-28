'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

By : shenqiti
2019/7/28

'''




class Solution:
    def reverse(self, x):
        if x > 0:  # handle positive numbers
            a =  int(str(x)[::-1])
        if x <=0:  # handle negative numbers
            a = -1 * int(str(x*-1)[::-1])
        # handle 32 bit overflow
        mina = -2**31
        maxa = 2**31 - 1
        if a not in range(mina, maxa):
            return 0
        else:
            return a



dd = Solution()
x = -1230000
result = dd.reverse(x)
print(result)

#
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#         while x % 10 == 0:
#             x /= 10
#
#         string_x = str(int(x))
#         if string_x[0] != '-':
#             rever_x = string_x[::-1]
#             return (rever_x)
#         else:
#             string_x = str(abs(int(x)))
#             rever_x = string_x[::-1]
#             return ("-"+ rever_x)
