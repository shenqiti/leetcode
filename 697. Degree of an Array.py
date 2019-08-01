'''
697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

By:shenqiti
2019/8/1
'''

class Solution(object):
    def findShortestSubArray(self, nums):
            dic = {}
            for n,i in enumerate(nums):
                if i in dic:
                    dic[i][0] += 1
                    dic[i].append(n)
                else:
                    dic[i] = [1]
                    dic[i].append(n)
            maxx = 0
            for m in dic:
                if dic[m][0] > maxx:
                    maxx = dic[m][0]
                    t = m
                if dic[m][0] == maxx:
                    t_length = dic[t][len(dic[t])-1]-dic[t][1]+1
                    m_length = dic[m][len(dic[m])-1]-dic[m][1]+1
                    if t_length > m_length:
                        t = m
                    else:
                        pass;
            length = dic[t][len(dic[t])-1]-dic[t][1]+1
            return length


dd = Solution()
nums = [1,2,1]
result = dd.findShortestSubArray(nums)
print(result)



# class Solution(object):
#
#     def GetDegree(self,nums):
#
#         sett = set(nums)
#         dict = {}
#         for item in sett:
#             dict.update({item: nums.count(item)})
#         degree = max(dict.values())
#
#         return degree
#
#
#     def findShortestSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         a = Solution()
#         l = 0
#         r = 0
#
#         degree = a.GetDegree(nums)
#         if degree ==1:
#             return 1
#
#         while  len(list(nums[0:len(nums)-r])) != degree and a.GetDegree(list(nums[0:len(nums)-r]))== degree :
#             r += 1
#
#         while len(list(nums[l:len(nums)-r])) != degree and a.GetDegree(list(nums[l:len(nums)-r]))== degree:
#             l += 1
#
#         return len(nums[l:len(nums)-r])
# 有点问题
