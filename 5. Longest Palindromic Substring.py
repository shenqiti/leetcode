'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
___________________________________________
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"
__________________________________________
By : shenqiti
2019/7/28

'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ''

        for i in range(len(s)):
            len1 = len(self.getlongestpalindrome(s,i,i))

            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s,i,i)

            len2 = len(self.getlongestpalindrome(s, i, i+1))

            if len2 > len(palindrome):
                 palindrome = self.getlongestpalindrome(s, i, i+1)
        return palindrome

    def getlongestpalindrome(self,s,l,r):
        while l>=0 and r< len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]



dd = Solution()
s = "babad"
result = dd.longestPalindrome(s)
print(result)
