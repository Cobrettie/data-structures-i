"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)

        # if list currently has a head
        if self.head:
            new_node.next = self.head # point new_node .next to old head
            self.head.prev = new_node # point current head .prev to new_node
            self.head = new_node # point new_node to be the new current head
            self.length += 1

        # if list has no head (basically an empty list)
        else:
            self.head = new_node
            self.tail = new_node
            # we don't need to set .prev or .next because those are already defined as None in ListNode class if no value is provided

        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        # if list has a tail (if list has a tail,I assume list also has a head)
        if self.tail:
            self.tail.next = new_node # point tail .next to new_node
            new_node.prev = self.tail # point new_node .prev to old tail
            self.tail = new_node # point tail to be new_node
            self.length += 1
        
        # if list has no tail (assuming if no tail, then no head either)
        else:
            self.head = new_node # point head to be new_node
            self.tail = new_node # point tail to be new_node

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return self.head.value
        
        current_max = self.head.value

        # just a starting point for us to begin looping through and checking values
        current_node = self.head

        #iterate through list, stopping when current_node == None
        while current_node is not None:
            # check if current_max is less than current_node.value, if so: set current_max = current_node.value
            if current_max < current_node.value:
                current_max = current_node.value
            # set current_node to next node in list to keep checking conditions
            current_node = current_node.next
            return current_max

