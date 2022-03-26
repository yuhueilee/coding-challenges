'''
Solution: https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829/Python-Easy-Iterative-and-Recursive-Solution
'''


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        """Find the kth smallest node in the binary search tree by 
        doing in-order traversal

        Args:
            root (TreeNode): node
            k (int): integer

        Returns:
            int: value of the k th smallest node in BST
        
        Time complexity:
            Best O(logN) for balanced BST
            Worst O(N) for not balanced BST
            where N is the total numner of nodes in tree
            (maximum depth of recursion)
        
        Space complexity:
            Best and Worst O(N)
            where N is the total numner of nodes in tree
        """
        # Store all the visited nodes (in-order traversal)
        stack = []
        while root is not None or stack != []:
            # Visit all the nodes in the left subtree
            while root is not None:
                stack.append(root)
                root = root.left
            # Pop the most recent visited node
            root = stack.pop()
            # Decrement counter
            k -= 1
            # Check the counter
            if k == 0:
                return root.val
            # Visit all the nodes in the right subtree
            root = root.right
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

sol = Solution()
root = TreeNode(val=3, left=TreeNode(val=1, right=TreeNode(val=2)), right=TreeNode(val=4))
sol.kthSmallest(root, 1)