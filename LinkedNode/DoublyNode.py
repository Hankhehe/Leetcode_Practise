class DoublyNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class DoublyLinkedNode:
    def __init__(self) -> None:
        self.head = None
        self.tall = self.head

    def AddTop(self,val) -> None:
        node = DoublyNode(val)
        if self.head:
            node.right = self.head
            self.head.left = node
            self.head = node
        else:
            self.head = node
            self.tall = self.head

    def Append(self,val) -> None:
        node = DoublyNode(val)
        if self.tall:
            node.left = self.tall
            self.tall.right = node
            self.tall = node
        else:
            self.head = node
            self.tall = self.head
    
    def Insert(self,val,index) -> None:
        node = self.head
        for i in range(index -1):
            node = node.right
        temp = DoublyNode(val)
        temp.right = node
        temp.left = node.left
        temppre = node.left
        node.left = temp
        temppre.right = temp
    
    def Delete(self,index) -> None:
        node = self.head
        for i in range(index -1):
            node = node.right
        pre = node.left
        post = node.right
        pre.right = node.right
        post.left = node.left

    def Travel(self,node=None) -> list | None:
        if not node:
            node = self.head
        result = []
        while node :
            result.append(node.val)
            node = node.right
        return result
    
    def TravelReversed(self,node=None) -> list | None:
        if not node:
            node = self.tall
        result = []
        while node :
            result.append(node.val)
            node = node.left
        return result

class Tree:
    def __init__(self):
        self.root = None

    def Add(self,val) -> None:
        # 為樹加入節點
        node  = DoublyNode(val)
        if not self.root:        #如果樹為空，就對根節點賦值
            self.root = node
        else:
            myQueue = []
            treeNode = self.root
            myQueue.append(treeNode)
            while myQueue:              #對已有的節點進行層次遍歷
                treeNode = myQueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myQueue.append(treeNode.left)
                    myQueue.append(treeNode.right)
 
    def Pre_Order_Stack(self) -> list | None:
        if not self.root: return
        result = []
        myStack = []
        node = self.root
        while myStack or node:
            while node:       #從根節點開始，一直尋找他的左子樹
                result.append(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()    #while結束表示當前節點node為空，即前一個節點沒有左子樹了
            node = node.right       #開始檢視它的右子樹
        return result

    def In_Order_Stack(self) -> list | None:
        if not self.root: return
        result = []
        myStack = []
        node = self.root
        while myStack or node:     #從根節點開始，一直尋找它的左子樹
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            result.append(node.val)
            node = node.right
        return result
  
    def Post_Order_Stack(self) -> list | None:
        # 先遍歷根節點，再遍歷右子樹，最後是左子樹，這樣就可以轉化為和先序遍歷一個型別了，最後只把遍歷結果逆序輸出就OK了。
        if not self.root: return
        result = []
        myStack1 = []
        myStack2 = []
        node = self.root
        while myStack1 or node:
            while node:
                myStack2.append(node)
                myStack1.append(node)
                node = node.right
            node = myStack1.pop()
            node = node.left
        while myStack2:
            result.append(myStack2.pop().val)
        return result
 
    def Level_Order_Queue(self) -> list | None:       #佇列實現層次遍歷
        if not self.root : return
        result = []
        myQueue = []
        node = self.root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            result.append(node.val)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
        return result



    #region 遞迴運算
    def Pre_Order_Recursion(self,node):     #遞迴實現前序遍歷
        if not node: return
        print (str(node.val) + ',',end='')
        self.Pre_Order_Recursion(node.left)
        self.Pre_Order_Recursion(node.right)

    def In_Order_Recursion(self,node):      #遞迴實現中序遍歷
        if not node: return
        self.In_Order_Recursion(node.left)
        print(str(node.val) + ',',end='')
        self.In_Order_Recursion(node.right)

    def Post_Order_Recursion(self,node):     #遞迴實現後序遍歷
        if not node: return
        self.Post_Order_Recursion(node.left)
        self.Post_Order_Recursion(node.right)
        print(str(node.val) + ',' ,end='')

    #endregion