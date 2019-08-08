'''
By:shenqiti
2019/8/8
Find the number of all daffodils in n digits
'''

class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """

    def getNarcissisticNumbers(self, n):
        # write your code here
        result = []
        for t in range(pow(10,n-1), pow(10,n)):
            temp = []
            N = t
            while t:
                temp.append(t % 10)
                t = t // 10
            LIST = [pow(i, len(temp)) for i in temp]
            if N == sum(LIST):
                result.append(N)

        return result



DD = Solution()
n = 3
result = DD.getNarcissisticNumbers(n)
print(result)
