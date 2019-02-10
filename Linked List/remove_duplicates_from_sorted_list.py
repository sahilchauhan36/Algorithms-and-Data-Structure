# This program explains the program to remove duplicates from an sorted linked list 

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

  # Module to remove duplicates from a sorted linked list 
  def remove_duplicates(self):
    current_node = self.head
    parent_node = None
    while current_node.next != None:
      if current_node.data ==  current_node.next.data:
        if parent_node != None:
          parent_node.next = current_node.next
          del current_node.data
          current_node = parent_node.next
        else:
          self.head = current_node.next
          del current_node.data
          current_node = self.head
      else:
        current_node = current_node.next
        if parent_node != None:
          parent_node = parent_node.next
        else:
          parent_node = self.head
  
if __name__=='__main__':
  # Create Linked List 
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Insert Elements in the Linked List 
  print("2. Insert Elements in Linked list")
  ll_obj.insert(1)
  ll_obj.insert(1)
  ll_obj.insert(3)
  ll_obj.insert(5)
  ll_obj.insert(5)
  ll_obj.insert(6)
  ll_obj.insert(7)
  ll_obj.insert(7)

  # Print the linked list 
  print("3. Linked List ") 
  ll_obj.print_list()

  # Remove Duplicate elements in the linked list
  print("4. Call Duplicates removal")
  ll_obj.remove_duplicates()
  
  # Print the list after deletion of duplicate elements
  print("3. Linked List after removing duplicate elements")
  ll_obj.print_list()
