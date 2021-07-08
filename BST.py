# linkedIn: https://www.linkedin.com/in/nirajpatel007

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data==None:
            self.data = data
        if self.data == data:
            return
        if data<self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.data == data:
            print("Data Found")
            return
        if data>self.data:
            if self.right:
                self.right.search(data)
            else:
                print("Data Not Found")
                return
        else:
            if self.left:
                self.left.search(data)
            else:
                print("Data Not Found")
                return

    def preOrder(self):
        print(self.data, end = " ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data, end = " ")

    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data, end = " ")
        if self.right:
            self.right.inOrder()

    def findMinNode(self):
        curr = self
        while curr.left:
            curr = curr.left
        return curr

    def Min(self):
        curr = self
        while curr.left:
            curr = curr.left
        print("Minimum Value: ",curr.data)

    def Max(self):
        curr = self
        while curr.right:
            curr = curr.right
        print("Maximum Value: ", curr.data)

    def delete(self, data):
        if self.data is None:
            print("Tree is Empty")
            return self
        if data<self.data:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Node is not Present")
        elif data>self.data:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Node is not Present")
        else:
            if not self.left and not self.right:
                self.data = None
                return None
            elif not self.left:
                self = self.right
            elif not self.right:
                self  = self.left
            else:
                temp = self.right.findMinNode()
                self.data = temp.data
                self.right = self.right.delete(temp.data)
                
        return self
                
                


root = BST(None)

data=[12, 10,5,23,24,11,55]
for i in data:
    root.insert(i)

root.inOrder()
print()
root.delete(23)
root.inOrder()
print()
root.Min()
root.Max()





            
        
