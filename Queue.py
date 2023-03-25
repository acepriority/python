from collections import deque

class Queue:
    def __init__(self):
        self.item = deque()
    def enqueue(self, item):
        self.item.append(item)
    def dequeue(self, item):
        self.item.popleft(item)
    def get_size(self):
        return len(self.item)


my_queue = Queue()
my_queue.enqueue(5)
# my_queue.dequeue()
print(my_queue.get_size())


        