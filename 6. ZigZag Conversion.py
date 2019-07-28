'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R


By : shenqiti
2019/7/28

'''


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2*numRows - 2
        strlist = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                strlist.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                    strlist.append(s[j+cycle-2*i])
        newstr = ''.join(strlist)
        return newstr



dd = Solution()
s = "PAYPALISHIRING"
numRows = 3
result = dd.convert(s,numRows)
print(result)
