# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
# Iterative Pre/Post/In Order Solutions.
class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        next = [root]
        preorderTraversal_list = []
        while next:
            n = next.pop()
            if n:
                # For iterative right comes first then left.
		        preorderTraversal_list.append(n.val)
                next.append(n.right)
                next.append(n.left)
        return preorderTraversal_list

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        next = [root]
        inorderTraversal_list = []
        while next:
            n = next.pop()
            if n:
                # For iterative right comes first then left.
                next.append(n.right)
                inorderTraversal_list.append(n.val)
                next.append(n.left)
        return inorderTraversal_list

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        next = [root]
        postorderTraversal_list = []
        while next:
            n = next.pop()
            if n:
                # For iterative right comes first then left.
                next.append(n.right)
                next.append(n.left)
                postorderTraversal_list.append(n.val)
        return postorderTraversal_list
