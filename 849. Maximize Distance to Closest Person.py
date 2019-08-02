'''
849. Maximize Distance to Closest Person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

By:shenqiti
2019/8/2

'''

class Solution:
    def maxDistToClosest(self, seats):
    	L = len(seats)
    	S = [i for i in range(L) if seats[i]]
    	d = [S[i+1]-S[i] for i in range(len(S)-1)] if len(S) > 1 else [0]
    	return max(max(d)//2, S[0], L-1-S[-1])





dd = Solution()
seats = [0,1,0,1]
result = dd.maxDistToClosest(seats)
print(result)

#
# class Solution(object):
#     def maxDistToClosest(self, seats):
#         """
#         :type seats: List[int]
#         :rtype: int
#         """
#         dic = {}
#         cnt = 0
#         temp = 0
#         for i in range(len(seats)):
#
#             if seats[i] == 1:
#                 dic[cnt] = i
#                 cnt += 1
#         if len(dic) == 1:
#             return max(len(seats[dic[0]:])-1,len(seats[:dic[0]]))
#
#         for i in range(1,len(dic)):
#             cnt = (dic[i-1] + dic[i])//2
#             if dic[i-1] !=0:
#                 dis = cnt - dic[i-1] + 1
#             else: dis = cnt-dic[i-1]
#
#             if temp<= dis:
#                 temp = dis
#         return temp
#有点问题
