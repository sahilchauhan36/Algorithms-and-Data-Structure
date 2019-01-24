# This program explains the Linked list Length program

class node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data):
    Node = node(data)
    if self.head == None:
      self.head = Node
    else:
      temp_node = self.head
      while temp_node.next != None: 
        temp_node = temp_node.next
      temp_node.next = Node

  # Module to print the linked list
  def print_list(self):
    print('\t[', end=' ')
    temp_node = self.head
    while temp_node != None:
      print("%s" % temp_node.data, end=' ,')
      temp_node = temp_node.next
    print('\b]')

  # Module to delete a linked list 
  def delete_list(self):
    current_node = self.head
    while current_node != None:
      next_node = current_node.next
      del current_node.data
      current_node = next_node 
    self.head = None 

  def length(self):
    length = 0
    current_node = self.head
    while current_node != None:
      current_node = current_node.next
      length = length + 1
    return length
  
  def find_mid_element(self):
    """
    This Function will print mid element of the linked list
    Use 2 Pointer i.e. Fast Pointer and Slow Pointer 

    Move Fast Pointer by 2 steps each time and slow pointer by 1.

    When Fast Pointer will reach to end slow must be on mid.
    
    """
    fast_pointer = self.head
    slow_pointer = self.head

    while fast_pointer != None and slow_pointer != None:
      fast_pointer = fast_pointer.next.next
      slow_pointer = slow_pointer.next

    return slow_pointer.data  
    

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List") 
  ll_obj.print_list()

  mid = ll_obj.find_mid_element()
  print("4. Mid Element of Linked List is %s" % mid)
