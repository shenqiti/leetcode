'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container,
such that the container contains the most water.


By : shenqiti
2019/7/29


'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        head = 0
        tail = len(height) - 1

        for cnt in range(len(height)):

            width = abs(head - tail)

            if height[head] < height[tail]:
                res = width * height[head]
                head += 1
            else:
                res = width * height[tail]
                tail -= 1

            if res > water:
                water = res

        return water




dd = Solution()
height = [1,8,6,2,5,4,8,3,7]
result = dd.maxArea(height)
print(result)



# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         temp = 0
#         for i in range(0,len(height)):
#             for j in range(i,len(height)):
#                 Area = (j-i)*min(height[i],height[j])
#                 if Area >= temp:
#                     temp = Area
#         return temp
