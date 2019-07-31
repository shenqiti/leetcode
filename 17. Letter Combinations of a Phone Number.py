'''
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
________________________________________________________________
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

________________________________________________________________

By:shenqiti
2019/7/31
'''

#
class Solution(object):


    def letterCombinations(self, digits):

        kvmaps = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
            }
        res = []

        def DFS(i, path):
            if i == len(digits):
                res.append(path)
                return
            for char in kvmaps[digits[i]]:
                DFS(i + 1, path + char)

        DFS(0, '')
        return res if digits else []


#         def letterCombinations(self, digits):
#             level = ['']
#             for num in digits:
#                 level = [l + char for l in level for char in kvmaps[num]]
#             return level if digits else []




dd = Solution()
digits = "234"
result = dd.letterCombinations(digits)
print(result)
