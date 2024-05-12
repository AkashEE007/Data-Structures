from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.items = LinkedList()
        
    def is_empty(self):
        return self.size() == 0
    
    def enqueue(self,data):
        self.items.prepend(data)

    def dequeue(self):
        return self.items.pop().data
    
    def size(self):
        return self.items.size()
    
    def __repr__(self):
        queue_list = []
        queue_size = self.size()
        current = self.items.head

        while queue_size > 0:
            queue_size -= 1
            queue_list.append(str(current.data))
            current = current.next_node

        return "\n".join(queue_list)
    
queue = Queue()
print(queue.is_empty())
queue.enqueue("Akash")
queue.enqueue("Suresh")
queue.enqueue("Hema")
queue.enqueue(24)
print(queue)
print(queue.dequeue())
print(queue)