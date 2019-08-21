'''
139. Word Break


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

By:shenqiti
2019/8/21

'''


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True]+[False]*len(s)

        for i in range(len(s)):
            #flag start
            if dp[i]:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        dp[j+1] = True
        return dp[-1]

dd = Solution()
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
result = dd.wordBreak(s,wordDict)
print(result)
