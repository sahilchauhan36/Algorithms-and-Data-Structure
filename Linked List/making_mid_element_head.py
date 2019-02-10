# This program explains the program to make mid_element HEAD of the linked list.

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
  
  def make_mid_head(self):
    fast_pointer = self.head
    slow_pointer = self.head

    while fast_pointer.next != None and fast_pointer != None:
      fast_pointer = fast_pointer.next.next
      parent_slow_pointer = slow_pointer
      slow_pointer = slow_pointer.next

    parent_slow_pointer.next = slow_pointer.next
    slow_pointer.next = self.head
    self.head = slow_pointer
    

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
  ll_obj.insert(7)

  # Print the list
  print("3. Linked List") 
  ll_obj.print_list()

  # Making Mid Element HEAD
  ll_obj.make_mid_head()
  print("4. Making Mid Element Head")

  # Print the list after changes
  print("3. Linked List") 
  ll_obj.print_list()

