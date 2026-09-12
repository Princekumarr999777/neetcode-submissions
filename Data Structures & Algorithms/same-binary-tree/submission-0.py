# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def count_node(p,q):
            if p==None and q==None:
                return True
            if p==None or q ==None:
                return False
            


            if p.val != q.val:

                return False
            return count_node(p.left,q.left)  and count_node(p.right,q.right)
            
           
        return count_node(p,q)
        