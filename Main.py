from Leetcode import Leetcode,SingleNode,DoublyNode
from LinkedNode.SingleNode import SingleLinkedNode
from LinkedNode.DoublyNode import Tree,DoublyLinkedNode
import time


#單向連結串列
node = SingleLinkedNode()
for i in range(30):
    node.Append(i)  #建立單向連結串列
print(node.Travel())
node.AddTop(888)
print(node.Travel())
node.Insert(999,3)
print(node.Travel())
node.Delete(4)
print(node.Travel())
node.CutNodeByIndex(node.SearchNodeIndexbyValue(999))
print(node.Travel())
pass

#雙向連結串列
node = DoublyLinkedNode(0)
for i in range(1,10):
    node.Append(i)
print(node.Travel())
print(node.TravelReversed())
node.Insert(999,3)
print(node.Travel())
print(node.TravelReversed())
node.Delete(3)
print(node.Travel())
print(node.TravelReversed())
pass

#二元樹
node = Tree(0)
for i in range(1,10):
    node.Add(i)
print(node.Pre_Order_Stack())
print(node.Post_Order_Stack())
print(node.Level_Order_Queue())
pass


#二元樹遞迴取值
nodecpoy = node.root
node.Pre_Order_Recursion(nodecpoy)
node.In_Order_Recursion(nodecpoy)
node.Post_Order_Recursion(nodecpoy)
pass







