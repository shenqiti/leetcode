'''
8. String to Integer (atoi)

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found
. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits
as possible, and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.
If no valid conversion could be performed, a zero value is returned.


By : shenqiti
2019/7/29


'''

class Solution(object):
    """
    :type str: str
    :rtype: int
    """
    def myAtoi(self, string):

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        string = string.strip()
        result = "0"
        negative = 0

        if len(string) == 0:
            return 0

        if string[0] == '-':
            negative = 1
            string = string[1:]

        elif string[0] == '+':
            string = string[1:]

        for i in string:
            if i not in "0123456789":
                break
            result += i

        total = int(result)
        if negative:
            total = -total
        return max(min(INT_MAX, total), INT_MIN)



dd = Solution()
string = "-+5-"
result = dd.myAtoi(string)
print(result)



# class Solution(object):
#     def myAtoi(self, String):
#         """
#         :type str: str
#         :rtype: int
#         """
#         list_num = [str(i) for i in range(10)]
#         sign = ['-','+']
#         string = ""
#         List = list(String)
#
#
#         for i in range(len(List)):
#
#             if List[0] in sign and len(List) == 1:
#                 return 0
#             elif List[i] != '-' and List[i] != '+' and List[i] not in list_num:
#                 break
#             elif List[i] in sign and List[i+1] in sign:
#                 return 0
#             elif List[i] == ' ':
#                 continue
#
#             elif List[i] in list_num:
#                 string += List[i]
#         if '-' in List:
#             string = '-'+string
#             if string == '-':
#                 return 0
#         elif '+' in List:
#             string = '+' + string
#             if string == "+":
#                return 0
#
#         if '+' in List:
#             string = string.replace("+",'')
#         if string != '':
#             if int(string)< -2**31 :
#                 return -2147483648
#             elif int(string)>2**31:
#                 return 2147483648
#             else:
#                 return int(string)
#         else:
#             return 0
