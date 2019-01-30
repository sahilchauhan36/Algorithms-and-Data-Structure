# This program explains the program to rotate a Linked List

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

  # Module to make the list in odd even order
  def odd_even_list(self):
    prev_pointer = None
    current_pointer = self.head
    next_pointer = current_pointer.next
    fast_pointer = self.head
    print("current_pointer before start : %s" % current_pointer.data)
    
    while fast_pointer.next != None:
        fast_pointer = fast_pointer.next
    last_element = fast_pointer
    
    while current_pointer != last_element:
      print("current_pointer %s" % current_pointer.data)
      if current_pointer.data%2 == 0:
        prev_pointer.next = next_pointer
        current_pointer.next = None
        fast_pointer.next = current_pointer
        fast_pointer = fast_pointer.next

      if prev_pointer is None:
        prev_pointer = None
      else:
        prev_pointer = next_pointer
      current_pointer = next_pointer
      next_pointer = current_pointer.next

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  """For Demo Inserting Elements in order"""
  ll_obj.insert(1)
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List before arrangement") 
  ll_obj.print_list()
  
  print("4. Calling Linked List ZigZag Arrangement")
  ll_obj.odd_even_list()

  print("5. Linked List after arrangement")
  ll_obj.print_list()
