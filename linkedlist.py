class SLLnode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        """return the data stored in the node"""
        return self.data

    def __repr__(self):
        return "This is the pointer: data={}".format(self.data)

    def set_data(self, new_data):
        """replaces old value with the new value"""
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
        
class SLL:
	def __init__(self):
		self.head = None
		
	def __repr__(self):
		return "The value of head is pointing to = {}".format(self.head)
	
	def add_front(self, new_data):
		"""Adds a node at the start of the linked list"""
		temp = SLLnode(new_data)
		temp.set_next(self.head)
		self.head = temp
		
	def is_empty(self):
		"""Returns true if the linked list is empty"""
		return self.head is None
	
	def search(self, data):
		"""Traverses the linked list and returns where the data is present in the liked list or not. Returns True or False.
		Time complexity is O(n) because in the worse case it will need to go through the whole list. 
		"""
		if self.head is None:
			return "The linked list is empty. Cannot search the data."
		
		current = self.head
		while current is not None:
			if current.get_data() == data:
				return True
			else:
				current = current.get_next()
		return False
			    	
	def size(self):
		"""Traverses the linked list and Returns the number of nodes in the linked list. Returns the size.
		
		Time complexity is O(n) because it has to traverse the whole linked list.
		"""
		size = 0
		if self.is_empty():
			return 0
	
		current = self.head
		while current is not None: #while there are no nodes in the list
		    size+=1
		    current = current.get_next()
		    
		return size
	
	def remove(self, removeData):
		"""Searches for the given data and if found, removes it from the linked List. Returns nothing.
		Time complexity is O(n) because in worst case we'll need to visit every node in the list.'
		"""
		if self.head is None:
			return "The linked list is empty, nothing to remove."
		
		current = self.head
		previous = None
		found = False
		
		while not found: #while the element is not found keep iterating
			if current.get_data() == removeData:
				found = True
			else:
				if current.get_next() == None:
					return "A node with that value is not present"
				else:
					previous = current
					current = current.get_next()
		if previous is None:
			self.head = current.get_next()
			
		else:
			previous.set_next(current.get_next())
			
				