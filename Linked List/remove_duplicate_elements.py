# This program explains the program to remove duplicates from an unsorted linked list 

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

  # Module to remove duplicates from a list linked list 
  def remove_duplicates(self):
    current_node = self.head
    set_list = set()
    self.print_list()
    print("[current_node : %s]" % current_node.data)
    while current_node != None:
      #print("[current_node : %s]" % current_node.data)
      if current_node.data in set_list:
        parent.next = current_node.next
        del current_node.data
        current_node = parent.next
      else:
        set_list.add(current_node.data)
        parent = current_node
        current_node = current_node.next
    set_list.clear()
  
if __name__=='__main__':
  # Create linked list 1
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Insert Elements into Linked List 
  print("2. Insert Elements in Linked list")
  ll_obj.insert(5)
  ll_obj.insert(1)
  ll_obj.insert(3)
  ll_obj.insert(5)
  ll_obj.insert(5)
  ll_obj.insert(1)
  ll_obj.insert(7)

  # Print the linked list 
  print("3. Linked List") 
  ll_obj.print_list()

  # Remove Duplicate elements in the linked list
  print("4. Call Duplicates removal")
  ll_obj.remove_duplicates()
  
  # Print the list after deletion of duplicate elements
  print("3. Linked List after removing duplicate elements")
  ll_obj.print_list()
