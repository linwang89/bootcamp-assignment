#Sum of root to leaf binary numbers
#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0

        cur = root.val
        vals = []
        stack = []
        if not root.left and not root.right:
            return cur
        if root.left:
            stack.append(root.left)
            vals.append(cur)
        if root.right:
            stack.append(root.right)
            vals.append(cur)
        while stack:
            print
            vals
            print
            res
            x = stack.pop()
            cur = vals.pop()
            cur = cur * 2 + x.val
            if not x.left and not x.right:
                res = res + cur
            else:
                if x.left:
                    stack.append(x.left)
                    vals.append(cur)

                if x.right:
                    stack.append(x.right)
                    vals.append(cur)

        return res