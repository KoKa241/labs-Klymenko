class QueueError(Exception):   
    pass


class Queue:
    def __init__(self):
        self.list_queue = []

    def put(self, elem):
        self.list_queue.append(elem)

    def get(self):
        if not len(self.list_queue):
            raise QueueError
        else:
            elem = self.list_queue.pop(0)
        return elem

    def is_empty(self):
        return not len(self.list_queue)

que = Queue()
que.put(1)
que.put("dog")
que.put(False)

print(que.is_empty())  

try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")


print(que.is_empty()) 
