from Leetcode import Leetcode,SingleNode,DoublyNode
from LinkedNode.SingleNode import SingleLinkedNode
from LinkedNode.DoublyNode import Tree,DoublyLinkedNode
import time,base64

leecodeCase = Leetcode()
aa = leecodeCase.isValid('aa(s){}[]')


APIpwd_ = base64.b64encode('QkIHIDPyeiIALps4IKGH+w=='.encode('UTF-8'))
APIpwd_ = base64.b64encode('Pixis1aB@'.encode('UTF-8'))
pass
numarry = []
numdic = set()

for i in range(99999):
    numarry.append(str(i))

for i in range(99999):
    numdic.add(str(i))

arrystarttime = time.time()
if '9999' in numarry:
    print(f'arry : {time.time() - arrystarttime}')
# for i in numarry:
#     if i == 999:
#         print(time.time() - arrystarttime)


dicstarttime = time.time()
if '9999' in numdic:
    print(f'dic : {time.time() - dicstarttime}')


pass

nums = [4,7,9,22,31,41]

for i , num in enumerate(nums):
    print(i,num)

aa = enumerate(nums)
pass

data = [0,1,2,3,4,5,6]

#單向連結串列
node = SingleLinkedNode()
for i in data:
    node.Append(i)  #建立單向連結串列
print(node.Travel())
node.AddTop(888)
print(node.Travel())
node.Insert(999,3)
print(node.Travel())
node.Delete(4)
print(node.Travel())
pass

#雙向連結串列
node = DoublyLinkedNode()
for i in data:
    node.Append(i)  #建立雙向連結串列
print(node.Travel())
print(node.TravelReversed())
node.Insert(999,3)
print(node.Travel())
print(node.TravelReversed())
node.Delete(3)
print(node.Travel())
print(node.TravelReversed())
pass

# 二元樹
node = Tree()
for i in data:
    node.Add(i)  #建立完整二元樹
print(node.Level_Order_Queue())
print(node.Pre_Order_Stack())
print(node.In_Order_Stack())
print(node.Post_Order_Stack())
pass

#二元樹遞迴取值
node = Tree()
for i in data:
    node.Add(i)  #建立完整二元樹
nodecpoy = node.root
print(node.Pre_Order_Recursion())
print(node.In_Order_Recursion())
print(node.Post_Order_Recursion())
pass







