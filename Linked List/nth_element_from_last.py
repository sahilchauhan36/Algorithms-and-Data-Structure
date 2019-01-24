# This program explains the Linked list Nth element from the last program

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
  
  def find_nth_element_from_end(self, n):
    """
    This Function will return nth element from the last.
     - Use 2 pointer 
     - Move fast pointer n steps from head
     - Now move both main pointer and fast pointer simultaneously
     - Now when fast will reach to end, main would be n steps behind it.
    """
    fast_pointer = self.head
    main_pointer = self.head

    count = n
    while n:
      fast_pointer = fast_pointer.next
      n = n - 1     
    while fast_pointer != None and main_pointer != None:
      fast_pointer = fast_pointer.next
      main_pointer = main_pointer.next

    return main_pointer.data  
    

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

  nth_element = ll_obj.find_nth_element_from_end(2)
  print("4. Nth Element from last of Linked List is %s" % nth_element)
