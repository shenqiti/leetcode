'''

96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?


DP, catalan number

By:shenqiti
2019/8/13
'''


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]



dd = Solution()
n = 3
result = dd.numTrees(n)
print(result)






# class Solution(object):
#     def numTrees(self, n):
#         T = [1, 1, 2] + [0]*(n - 2)
#         for m in range(3, n + 1):
#             for i in range(m):
#                 T[m] += T[i] * T[m - 1 - i]
#         return T[n]
#
#     """
#     Faster version below takes advantage of symmetry (half as many iterations)
#     """
#     def numTreesFaster(self, n):
#         T = [1, 1, 2] + [0]*(n - 2)
#         for m in range(3, n + 1):
#             mid, remainder = divmod(m, 2)
#             for i in range(mid):
#                 T[m] += T[i] * T[m - 1 - i]
#             T[m] *= 2
#             if remainder: T[m] += T[mid] * T[mid]
#         return T[n]


'''

The pattern is simply:
T(0) = 1 (defined for convenience)
T(1) = 1 (number of binary search trees possible with one node)
T(2) = 2 (number of binary search trees possible with two nodes)
T(3) = T(0)*T(2) + T(1)*T(1) + T(2)*T(0) (1st term: lowest number is root, 2nd term: middle number is root, 3rd term: biggest number is root)
T(4) = T(0)*T(3) + T(1)*T(2) + T(2)*T(1) + T(3)*T(0)
T(5) = T(0)*T(4) + T(1)*T(3) + T(2)*T(2) + T(3)*T(1) + T(4)*T(0)
'''



'''
The total number of BSTs is described by the function: (2n)! / ((n+1)! n!)

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return factorial(2 * n) / (factorial(n+1) * factorial(n))
    
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

'''
