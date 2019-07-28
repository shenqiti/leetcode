'''
Given a string, find the length of the longest substring without repeating characters.

__________________________________________________
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
_________________________________________________
By : shenqiti
2019/7/28

'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

dd = Solution()
s = 'ababcde'
result = dd.lengthOfLongestSubstring(s)
print(result)



# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         biggest_len = 0
#         for n in range(len(s)):
#             string_list = []
#             for m in range(n,len(s)):
#                 if s[m] not in string_list:
#                     string_list.append(s[m])
#                 else:
#                     break
#             length = len(string_list)
#             if length >= biggest_len:
#                 biggest_len = length
#         return biggest_len
#


