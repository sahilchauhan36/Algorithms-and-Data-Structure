# This program explains the program to count the number of occurances of a given element in the linked list.

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
  def count_element(self, element):
    current_node = self.head
    count = 0 # variable to keep record of number of occurances
    while current_node != None:
      if current_node.data == element:
        count += 1
      current_node = current_node.next
    return count


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
  ll_obj.insert(2)
  ll_obj.insert(2)

  # Print the list
  print("3. Linked List before Deletion") 
  ll_obj.print_list()
  
  # Element to count
  element = 2
  print("4. Count the element %s in the Linked List" % element)
  occurances = ll_obj.count_element(element)

  print("5. Number of Occurances of the given element in linked list are: %s" % occurances)
