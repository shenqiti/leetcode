'''
数组和动态数组系列：

73. Set Matrix Zeroes
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

By : shenqiti
2019/7/31

'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        position = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    position.append([i,j])

        for each in position:
            for i in range(0,len(matrix[each[0]])):
                matrix[each[0]][i]= 0
            for j in range(0,len(matrix)):
                matrix[j][each[1]] = 0
        return matrix




dd = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
result = dd.setZeroes(matrix)
print(result)
