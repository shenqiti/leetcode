'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

By : shenqiti
2019/7/30
'''




class Solution:
    def isValid(self, s: str) -> bool:
        stack, bracket_hash = [], {"(":")", "[":"]", "{":"}"}
        for item in s:
            if item in bracket_hash:
                stack.append(bracket_hash[item])
            elif not stack or stack.pop() != item: 
                return False
        return len(stack) == 0

dd = Solution()
s = "()"
result = dd.isValid(s)
print(result)


# class Solution:
#     def isValid(self, s):
#         #if len(s) % 2 != 0:
#         #    return False
#         stack = []
#         map_list = {')':'(', '}':'{', ']':'['}
#         for c in s:
#             if c in map_list.keys():
#                 if len(stack) == 0:
#                     return False
#                 elif stack[-1] == map_list[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
#         if len(stack) == 0:
#             return True
#         else:
#             return False
