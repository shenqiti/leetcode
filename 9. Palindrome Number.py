'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.



By : shenqiti
2019/7/29


'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        middle = len(x)//2
        if len(x) %2 ==0:
            x = x[:middle]+'0'+x[middle::]

        i = 0
        j = len(x)-1
        while i!=j and x[i]==x[j]:
            i += 1
            j -= 1
        if j==i:
            return 1
        else:return 0


dd = Solution()
x = 1111
result = dd.isPalindrome(x)
print(result)
