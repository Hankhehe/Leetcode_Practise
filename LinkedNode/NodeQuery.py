class NodeQuery():
    def Pre_order_recursion(self,node) -> None:     #遞迴實現前序遍歷
        if not node:
            return
        print (node.val)
        self.Pre_order_recursion(node.left)
        self.Pre_order_recursion(node.right)
 
    def In_order_recursion(self,node) -> None:      #遞迴實現中序遍歷
        if not node:
            return
        self.In_order_recursion(node.left)
        print(node.val)
        self.In_order_recursion(node.right)
 
    def Post_order_recursion(self,node) -> None:     #遞迴實現後序遍歷
        if not node:
            return
        self.Post_order_recursion(node.left)
        self.Post_order_recursion(node.right)
        print(node.val)
 
    def Level_order_queue(self,node) -> None:       #佇列實現層次遍歷（非遞迴）
        if not node :
            return
        myQueue = []
        node = node
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)
    def Print_SingleNode(self,node) ->None:
        if not node:
            return
        while node:
            print(node.val)
            node = node.next

                