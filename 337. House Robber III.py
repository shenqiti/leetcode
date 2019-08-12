'''
37. House Robber III


The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root." Besides the root,
each house has one and only one parent house. After a tour,
the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.


Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.


For each node, we record the maximum benefits of robbing it or not separately, [not rob, rob].
 Consider the current node, if you decide to rob it, you cannot rob its direct children, 
 thus, you can obtain root.val+left[not rob]+right[not rob]; while if you decide not to rob it, 
 it doesn't matter whether you rob or not rob its children, so just find the maximum values from the children, 
 thus you obtain max(left[rob], left[not rob])+max(right[rob], right[not rob]). Finally, return the maximum value. 
 Hope this helps.

class So

By:shenqiti
2019/8/12

'''
#Way 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
    def helper(self, root):
        if root is None:
            return (0,0)
        lc=self.helper(root.left)
        rc=self.helper(root.right)
        return (max(lc)+max(rc), root.val+lc[0]+rc[0])




#Way 2

# class Solution(object):
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """

#         def superrob(node):
#             # returns tuple of size two (now, later)
#             # now: max money earned if input node is robbed
#             # later: max money earned if input node is not robbed

#             # base case
#             if not node: return (0, 0)

#             # get values
#             left, right = superrob(node.left), superrob(node.right)

#             # rob now
#             now = node.val + left[1] + right[1]

#             # rob later
#             later = max(left) + max(right)

#             return (now, later)

#         return max(superrob(root))
