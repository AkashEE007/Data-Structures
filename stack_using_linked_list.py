from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.items = LinkedList()

    def is_empty(self):
        return self.size() == 0
    
    def push(self,data):
        self.items.prepend(data)

    def pop(self):
        return self.items.remove_by_index(0)
    
    def peek(self):
        stack_size = self.size()
        current = self.items.head
        while stack_size > 1:
            current = current.next_node
            stack_size -= 1
        return current.data
            
    def size(self):
        return self.items.size()
    
    def __repr__(self):
        stack_list = []
        stack_size = self.size()
        current = self.items.head
        while stack_size > 0:
            stack_size -= 1
            stack_list.append(str(current.data))
            current = current.next_node

        return "\n".join(stack_list)