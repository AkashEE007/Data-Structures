class Node:
    """Each node in the linked list is an object, that are instantiated with every node
    created in the linked list.
    Models two attributes - data and the link to next node in the list."""

    data = None #Contains Node data
    next_node = None    #Contains reference to next node

    def __init__(self,data):
        self.data = data    

    def __repr__(self):
        return "<Node data: {0}>".format(str(self.data))
    

class LinkedList:
    """Singly Linked List"""

    def __init__(self):
        self.head = None    #head attribute models only node that list has reference to

    def is_empty(self):
        """Checks whether the linked list is empty or not. Returns a boolean
        value."""

        return self.head == None
    
    def size(self):
        """Returns the number of nodes in the list.
        Takes linear runtime O(n)."""

        current = self.head #"current" acts as a pointer to the node and keeps on storing next node reference
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def prepend(self,data):
        """Adds a new node containing data at the head of the list.
        Takes constant time O(1)."""

        new_node = Node(data) #Creating a new node
        new_node.next_node = self.head  #Creating the reference for previous head using next_node attribute
        self.head = new_node    #Declaring the newly added node as head of list

    def append(self,data):
        """Adds a new node containing data at the tail of the list.
        List traversal takes linear runtime.
        Overall runtime is O(n)"""

        new_node = Node(data)
        list_size = self.size()
        position = list_size
        current = self.head

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        next_node = None

        prev_node.next_node = new_node

    def search(self,key):
        """Search for first node that contains data that matches the key.
        Returns node or None if not found.
        Takes Linear runtime O(n)"""

        current = self.head     #Again current acts as a pointer

        while current:
            if current.data == key:
                return current
            
            else:
                current = current.next_node #"current" pointer storing reference for next node

        return None
    
    def insert(self,data,index):
        """Inserts a new node containing data at index position.
        Insertion taks constant time O(1), but finding node of
        insertion takes linear time O(n).
        Overall takes linear run time O(n)."""

        if index == 0:  #If index is 0, no need to traverse the list
            self.prepend(data)  #Just use add() method. A new node will be created inside add()
        
        if index > 0:
            new_node = Node(data)    #If index > 0, we need to traverse the list and create a new node object
            position = index

            current = self.head #Every time current.next_node is called, index is reduced by 1

            while position > 1:
                current = current.next_node
                position -= 1
            
            prev_node = current     #Including this one, next three lines of codes are for swapping the references
            next_node = current.next_node

            prev_node.next_node = new_node
            new_node.next_node = next_node

    def remove(self,key):
        """Removes node containing the data that matches the key.
        Returns node or None if next key doesn't exist
        Takes Linear runtime O(n)"""

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:    #When the node is not at the head of list
                found = True
                self.head = current.next_node

            if current.data == key: #When node is the head of the list
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node
        return current 
    
    def remove_by_index(self,index):
        """The method removes the node at particular index.
        Indexing starts from 0.
        Traversing requires linear runtime O(n)."""

        current = self.head
        previous_node = None

        if index == 0:
            prev_head = self.head
            self.head = current.next_node
            return prev_head.data

        elif index == self.size():
            return self.pop().data
        
        if index < self.size():
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            delete = current.next_node
            next_node = delete.next_node
            prev_node.next_node = next_node
            return delete.data
    
    def pop(self):
        """Removes the last node of the list.
        List traversal has runtime of O(n).
        Hence overall runtime is Linear O(n)."""

        current = self.head
        list_size = self.size()
        position = list_size

        while position > 2:
            position -= 1
            current = current.next_node

        last_node = current.next_node
        current.next_node = None

        return last_node
    
    def index(self,key):
        """The method returns the index of the node required.
        List traversal has linear runtime O(n).
        Indexing starts from 0.#"""

        position = -1
        current = self.head
        found = False

        while current and not found:
            if current.data == key:
                found = True
                position += 1

            else:
                current = current.next_node
                position += 1

        return position
              
    def __repr__(self):
        """Returns a string representation of the list.
        Takes linear runtime O(n)."""

        nodes = []
        current = self.head #"current" acts as pointer to first node

        while current:
            if current is self.head:    
                nodes.append("[Head: {}]".format(current.data))

            elif current.next_node is None:
                nodes.append("[Tail: {}]".format(current.data))

            else:
                nodes.append("[{}]".format(current.data))

            current = current.next_node
        return "-> ".join(nodes)

