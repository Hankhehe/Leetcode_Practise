class Node:
    def __init__(self, val): 
        self.val = val
        self.next = None
        return

class SingleLinkedNode:
    def __init__(self,val) -> None:
        self.head = Node(val)
        self.tall = self.head
    
    def Addtop(self,val:int)->None:
        temptop = Node(val)
        temptop.next = self.head
        self.head = temptop
    
    def Addtall(self,val:int)->None:
        temptall = Node(val)
        self.tall.next = temptall
        self.tall = temptall

    def InsertNode(self,index:int,val:int)->bool:
        tempnode = Node(val=0)
        tempnode.next = self.head
        for _ in range(index):
            if tempnode.next:
                tempnode = tempnode.next
            else:
                return False
        insertnode = tempnode.next
        tempnode.next = Node(val)
        tempnode.next.next = insertnode
        if not insertnode:
            self.tall = tempnode.next
        return True
    
    def DelNode(self,index:int)->bool:
        tempnode = Node(0)
        tempnode.next = self.head
        for _ in range(index):
            if tempnode:
                tempnode = tempnode.next
        if tempnode.next.next
            tempnode.next = tempnode.next.next

        
    
    def DelTop(self) -> None:
        if self.head:
            self.head = self.head.next
    
    def DelTall(self) ->None:
        if self.head.next:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            self.tall = temp
        else:
            self.head = None

    def Printnode(self)->None:
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next

nodelist = SingleLinkedNode(1)
nodelist.Addtop(0)
nodelist.Addtall(2)
nodelist.Addtall(3)
nodelist.Addtall(4)
nodelist.InsertNode(5,50)
nodelist.Addtall(51)
nodelist.DelTop()
nodelist.DelTall()
nodelist.Printnode()
print(nodelist.tall.val)

# pass
        

        