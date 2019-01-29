"""
This program explains the program to delete alternate nodes in the linked list 
Linked list can be have odd number of elements or even number of elements. 
So, It has been run for both the scenarios.
"""

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
  
  # Module to count occurances of an element in the linked list
  def delete_alternate_nodes(self):
    current_node = self.head
    while current_node != None and current_node.next != None:
      next = current_node.next
      current_node.next = next.next
      current_node = current_node.next
      del next.data


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
  ll_obj.insert(7)
  ll_obj.insert(8)
  ll_obj.insert(9)
  ll_obj.insert(10)
  ll_obj.insert(11)
  ll_obj.insert(12)
  ll_obj.insert(13)
  ll_obj.insert(14)

  # Print the list
  print("3. Linked List (Having even number of elements)") 
  ll_obj.print_list()
  
  # Print the list
  print("4. Delete Alternative Nodes") 
  ll_obj.delete_alternate_nodes()

  # Print the list
  print("5. Linked List after Deletion of alternative elements") 
  ll_obj.print_list()

   # Print the list
  print("6. Now Linked List is having Odd number of elements") 
  ll_obj.print_list()
  
  # Print the list
  print("7. Again Delete Alternative Nodes") 
  ll_obj.delete_alternate_nodes()

  # Print the list
  print("8. Linked List after Deletion of alternative elements") 
  ll_obj.print_list()

