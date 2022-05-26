from Leetcode import Leetcode,SingleLinkedNode,TreeNode
from LinkedNode.SingleLinkedNode import OperatorSingleLinkedNode
import time

node = OperatorSingleLinkedNode()
for i in range(30):
    node.append(i)
print(node.travel())
node.add(888)
print(node.travel())
node.insert(999,3)
print(node.travel())
node.delete(4)
print(node.travel())
node.cutNodeByIndex(node.searchNodeIndexbyValue(999))
print(node.travel())
