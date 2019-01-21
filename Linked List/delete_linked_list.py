# This program explains the Deletion Functionality of the Linked List

class node:
  def __init__(self, data):
    self.data = data
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data):
    print("Insert Element: %s" % data)
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
    temp_node = self.head
    while temp_node.next != None:
      print("Element in the list : %s" % temp_node.data)
      temp_node = temp_node.next

  def delete_list(self):
    current_node = self.head
    while current_node != None:
      next_node = current_node.next
      del current_node
      current_node = next_node
    

if __name__=='__main__':
  print("Create a Linked List Object")
  ll_obj = linked_list()
  
  # Update head of the linked list 
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("Linked List before Deletion") 
  ll_obj.print_list()
  
  print("Call Linked List Deletion")
  ll_obj.delete_list()

  print("Linked List after Deletion")
  ll_obj.print_list()
