class SingleLinkedNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class OperatorSingleLinkedNode(object):
    def __init__(self):
        self.header = None
        self.length = 0

    # 1、判斷是否為空
    def is_empty(self):
        if self.header == None:
            return True
        else:
            return False

    # 頭部插入
    def add(self, val):
        node = SingleLinkedNode(val)
        # 如果為空
        if self.is_empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.length += 1

    # 尾部插入
    def append(self, val):
        node = SingleLinkedNode(val)
        current_Node = self.header
        if self.is_empty():
            self.add(val)
        else:
            # 找到最後一個結點
            while (current_Node.next != None):
                current_Node = current_Node.next
            current_Node.next = node
            self.length += 1

    # 指定位置插入
    def insert(self, val, index):
        node = SingleLinkedNode(val)
        current_Node = self.header
        
        if index > self.length + 1 or index <= 0:
            while (index > self.length + 1 or index <= 0):
                print("你要插入的位置不對，請重選位置:")
                index = eval(input())

        if index == 1:
            self.add(val)
        elif index == 2:
            node.next = self.header.next
            self.header.next = node
            self.length += 1
        else:
            for i in range(1, index - 1):
                current_Node = current_Node.next
            node.next = current_Node.next
            current_Node.next = node
            self.length += 1

    # 遍歷
    def travel(self,node=None) -> list:
        data = []
        if not node:
            node = self.header
        if not node: return data
        while node:
            data.append(node.val)
            node = node.next
        return data

    # 按索引刪除
    def delete(self, index):
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你輸入的下標不對，請重新輸入需要刪除的值的下標：")
                index = eval(input())
                #   return
        else:
            if index == 1:
                self.header = self.header.next
                currentNode = self.header
            elif index == 2:
                current_Node = self.header
                current_Node.next = current_Node.next.next
            else:
                current_Node = self.header
                for i in range(1, index - 1):
                    current_Node = current_Node.next
                current_Node.next = current_Node.next.next
        self.length -= 1

    # 查詢 Value 的 Index
    def isContain(self, num):
        contain = 0
        current_Node = self.header
        for i in range(self.length):
            if current_Node.val == num:
                return i
            current_Node = current_Node.next
        return

    # 切斷指定 index 之前的 Node
    def searchNodeByIndex(self, index):
        current_Node = self.header
        if index <= 0 or index > self.length:
            while (index <= 0 or index > self.length):
                print("你輸入的下標不對，請重新輸入:")
                index = eval(input())
        if index > 0 or index <= self.length:
            for i in range(index):
                current_Node = current_Node.next
                self.header = current_Node
