'''
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
By: shenqiti
2019/7/30
'''


class Solution:
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        counter = 0
        i = 0

        # adding all the values up

        for i in range(len(s)):
            counter += values[s[i]]

            # skipping the first element as we're counting backwords

            if i == 0: continue

            # removing any characters that are suppose to be subtracted.
            # Since I already added them once, I'll remove the twice

            if values[s[i]] > values[s[i - 1]]:
                counter -= values[s[i - 1]] * 2

        return counter



dd = Solution()
s = "IV"
result = dd.romanToInt(s)
print(result)
