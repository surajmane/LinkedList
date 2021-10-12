class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def get_data(self):
        """return the data stored in the node"""
        return self.data
    

    def __repr__(self):
        return "This is the pointere: data={}".format(self.data)

    def set_data(self, new_data):
        """replaces old value with the new value"""
        self.data = new_data

    def get_next(self):
    	"""Get the position of the next data value"""
    	return self.next

    def set_next(self, new_next):
    	"""Sets the next pointers position"""
    	self.next = new_next
        
    def set_previous(self, new_previous):
        self.previous = new_previous
    	
    def get_previous(self):
        return self.previous
        
class DLL:
    def __init__(self):
	    self.head = None
		
    def is_empty(self):
        return self.head is None	
	
    def __repr__(self):
	    return "The value of head is pointing to = {}".format(self.head)

    def size(self):
    	"""Traverses through the linked list and returns the number of nodes."""
    	if self.head is None:
    		return "The linked list is empty"
    	size = 0
    	current = self.head
    	while current is not None:
    	    current = current.next
    	    size+=1
    	return size
    
    def search(self, data):
    	if self.head is None:
    		return "The linked list is empty, nothing to search."
    	current = self.head
    	while current is not None:
    		if current.get_data() == data:
    			return True
    		else:
    			current = current.next
    	return False
    		
    	
    def add_front(self, data):
        temp = DLLNode(data)
        temp.set_next(self.head)
    	
        if self.head is not None:
    	    self.head.set_previous(temp)
    		
        self.head = temp
        
    def remove(self, data):
    	"""Traverses the list, if the element is found it removes the first occurance from the list.
    	Time complexity is O(n) because in the worse case we'll need to traverse the whole list."""
    	if self.head is None:
    		return "The list is empty, nothing to remove."
    	current = self.head
    	found = False
    	
    	while not found:
    		if current.get_data() == data:
    			found = True
    		else:
    			if current.get_next() is None:
    				return "The data you want to remove doesn't exist, nothing to remove."
    			else:
    				current = current.get_next()
    	if current.previous is None:
    		self.head = current.get_next()
    		current.next.set_previous(self.head)
    	elif current.get_next() is None:
    		current.previous.set_next(None)
    	else:
    		current.previous.set_next(current.get_next())
    		current.next.set_previous(current.get_previous())