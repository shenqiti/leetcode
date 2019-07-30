'''

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
		# Empty list
		if not strs: return ""
		firstword=strs[0]
		for i in range(len(firstword)+1):
			for word in strs:
				try:
					# if difference is found, return up until that difference
					if firstword[i]!=word[i]:
						return firstword[:i]
				except IndexError: # String lengths are not consistent.
					return firstword[:i]


dd = Solution()
strs = ["aca","aba",'sbs']
result = dd.longestCommonPrefix(strs)
print(result)
