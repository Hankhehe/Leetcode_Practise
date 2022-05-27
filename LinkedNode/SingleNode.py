class SingleNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class SingleLinkedNode:
    def __init__(self) -> None:
        self.header = None
        self.length = 1

    # 1、判斷是否為空
    def Is_Empty(self) -> bool:
        if self.header == None:
            return True
        else:
            return False

    # 頭部插入
    def AddTop(self, val) -> None:
        node = SingleNode(val)
        # 如果為空
        if self.Is_Empty():
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.length += 1

    # 尾部插入
    def Append(self, val) -> None:
        node = SingleNode(val)
        current_Node = self.header
        if self.Is_Empty():
            self.AddTop(val)
        else:
            # 找到最後一個結點
            while (current_Node.next != None):
                current_Node = current_Node.next
            current_Node.next = node
            self.length += 1

    # 指定位置插入
    def Insert(self, val, index) -> None:
        node = SingleNode(val)
        current_Node = self.header
        
        if index > self.length + 1 or index <= 0:
            while (index > self.length + 1 or index <= 0):
                print("你要插入的位置不對，請重選位置:")
                index = eval(input())

        if index == 1:
            self.AddTop(val)
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
    def Travel(self,node=None) -> list:
        result = []
        if not node:
            node = self.header
        if not node: return result
        while node:
            result.append(node.val)
            node = node.next
        return result

    # 按索引刪除
    def Delete(self, index) -> None:
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
    def SearchNodeIndexbyValue(self, num) -> int | None:
        contain = 0
        current_Node = self.header
        for i in range(self.length):
            if current_Node.val == num:
                return i
            current_Node = current_Node.next
        return

