from Leetcode import Leetcode,SingleLinkedNode,TreeNode
from LinkedNode.SingleLinkedNode import OperatorSingleLinkedNode
import time

node = OperatorSingleLinkedNode()
for i in range(30):
    node.append(i)
node.insert(999,3)
print(node.travel())
node.delete(4)
print(node.travel())
node.searchNodeByIndex(5)
print( node.travel())
