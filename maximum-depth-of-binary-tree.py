from typing import Optional
null = None
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #import pdb; pdb.set_trace()
        depth = self.step(root, 0)
        return(depth)
        
    def step(self, root, depth):
        if root == None: return 0
        ldepth = depth
        rdepth = depth
        print(root.val)
        if root.val != None:
            ldepth += self.step(root.left, depth)
            rdepth += self.step(root.right, depth)
        return max(ldepth, rdepth) + 1

if 1:
    rnode0 = TreeNode(20, TreeNode(15),TreeNode(7)) 
    root = TreeNode(3,TreeNode(9),rnode0)
    s= Solution()
    d = s.maxDepth(root)
    print(d)
    assert d == 3

root = [1,null,2]
root = TreeNode(1,null,TreeNode(2,null,null))
s= Solution()
d = s.maxDepth(root)
assert d == 2

print("All OK")
