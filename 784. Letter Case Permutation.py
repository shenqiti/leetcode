'''
784. Letter Case Permutation
递归专题
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create.

By:shenqiti
2019/8/2

'''


class Solution(object):
    def letterCasePermutation(self, S):
        def backtrack(S, step, curr, res):
            # already go through the entire string, S
            if step == len(S):
                res.append(curr)
                return

            # not alphabets => one backtrack case
            if S[step].lower() == S[step].upper():
                backtrack(S, step + 1, curr + S[step], res)

            # having upper and lower letters => two backtrack cases
            else:
                backtrack(S, step + 1, curr + S[step].lower(), res)
                backtrack(S, step + 1, curr + S[step].upper(), res)

        res = []
        backtrack(S, 0, "", res)
        return res



dd= Solution()
S = "a1b2"
result = dd.letterCasePermutation(S)
print(result)
