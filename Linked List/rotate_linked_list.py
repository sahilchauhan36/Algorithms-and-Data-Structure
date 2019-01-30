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

  # Module to rotate a linked list 
  def rotate_list(self, n):
    current_pointer = self.head
    fast_pointer = self.head
    
    count=0
    # Move fast pointer nth steps so that when fast_pointer is at last element, current_pointer will be at nth element from end.
    while count < n:
      fast_pointer = fast_pointer.next
      count += 1

    while fast_pointer.next != None:
      fast_pointer = fast_pointer.next
      current_pointer = current_pointer.next

    # update pointers
    fast_pointer.next = self.head
    self.head = current_pointer.next
    current_pointer.next = None


if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  """For Demo Inserting Elements in order"""
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List before Rotation") 
  ll_obj.print_list()
  
  rotations = 3
  print("4. Calling Linked List Rotation by %s " % rotations)
  ll_obj.rotate_list(rotations)

  print("5. Linked List after Rotation")
  ll_obj.print_list()
