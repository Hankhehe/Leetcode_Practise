
from Leetcode import Leetcode
import time




class Node :
    def __init__(self,value) -> None:
        self.val = value
        self.next = None

class Linked :
    def __init__(self) -> None:
        self.top = None
        self.tall = None

    def add(self,val)-> None:
        if not self.top:
            self.tall = Node(val)
            self.top = self.tall
        else:
            self.tall.next = Node(val)
            self.tall = self.tall.next


linkednode = Linked()

for i in range(40):
    linkednode.add(i)

l2 = linkednode.top

while linkednode.top :
    print(linkednode.top.val)
    linkednode.top = linkednode.top.next
    
pass