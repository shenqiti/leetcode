'''
448. Find All Numbers Disappeared in an Array


Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
________________________________________________
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

_______________________________________________
By:shenqiti
2019/8/1
'''


class Solution:
    def findDisappearedNumbers(self, nums):
        '''
        Sets are very fast Python data structures. Whenever order isnt important you can use them to speed-up run-time.
        Firstly it creates a set of numbers from 1 to n and then difference method returns a list of missing numbers.
        '''
        return set(range(1, len(nums) + 1)).difference(set(nums))


dd = Solution()
nums = [4,3,2,7,8,2,3,1]
result = dd.findDisappearedNumbers(nums)
print(result)
