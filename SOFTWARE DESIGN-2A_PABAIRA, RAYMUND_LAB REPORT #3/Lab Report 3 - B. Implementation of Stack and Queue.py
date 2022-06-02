class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = self.rear = None
    def isEmpty(self):
        return self.front == None
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):

        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

if __name__ == '__main__':
    jay = Queue()
    jay.EnQueue(10)
    jay.EnQueue(20)
    jay.DeQueue()
    jay.DeQueue()
    jay.EnQueue(30)
    jay.EnQueue(40)
    jay.EnQueue(50)
    jay.DeQueue()
    print("Queue Front: " + str(jay.front.data))
    print("Queue Rear: " + str(jay.rear.data))



