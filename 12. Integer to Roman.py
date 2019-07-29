'''
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000



By : shenqiti
2019/7/29

'''


class Solution:
    def intToRoman(self, num):
	    # knowledge
        number = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        value = [1000, 500, 100, 50, 10, 5, 1]
        result = []

        for i in range(0, len(value)):
            times = int(num / value[i])
            if times == 4:
                if len(result) > 0 and result[-1] == number[value[i-1]]:
				    # 9
                    result[-1] = number[value[i]]
                    result.append(number[value[i-2]])
                else:
				    # 4
                    result.append(number[value[i]])
                    result.append(number[value[i-1]])
            else:
			    # other numbers
                for j in range(0, times):
                    result.append(number[value[i]])
            num = num % value[i]
        return ''.join(result)

dd = Solution()
num = 2981
result = dd.intToRoman(num)
print(result)
