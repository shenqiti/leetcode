'''
48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
By : shenqiti
2019/7/31

'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp
        return matrix
dd = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = dd.rotate(matrix)
print(result)





# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#             """
#         for i in range(0,len(matrix)//2):
#             temp= matrix[i]
#             matrix[i] = matrix[len(matrix)-1-i]
#             matrix[len(matrix)-1-i] = temp
#
#         for i in range(0,len(matrix)):
#             for j in range(0,len(matrix[i])):
#                 if i-j>=0:
#                     TEMP = matrix[i][i-j]
#                     matrix[i][i-j] = matrix[i-j][i]
#                     matrix[i-j][i] = TEMP
#                 else:continue
#         return matrix
