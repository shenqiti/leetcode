'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


By : shenqiti
2019/7/30

'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs: return ''
        first = strs[0]

        for i in range(0,len(first)+1):
            for each in strs:
                try:
                    if each[i] != first[i]:
                        return first[:i]
                except:
                    return first[:i]


dd = Solution()
strs = ["aca", "ac", 'acs']
result = dd.longestCommonPrefix(strs)
print(result)
