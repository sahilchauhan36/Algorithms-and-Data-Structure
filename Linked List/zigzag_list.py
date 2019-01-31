# This program explains the program to arrange a Linked List in Zig-Zag Fashion
 
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
    print("last element of the list is %s" % last_element.data)
    
    while current_pointer != last_element:
      if current_pointer.data%2 == 0:
        if self.head is current_pointer:
          self.head = next_pointer
        else:
          prev_pointer.next = next_pointer
          current_pointer.next = None
          fast_pointer.next = current_pointer
          fast_pointer = fast_pointer.next
    
      if current_pointer.data%2 != 0:
        prev_pointer = current_pointer
      current_pointer = next_pointer
      next_pointer = current_pointer.next
      print("[previous:%s, current:%s, next:%s]" %(prev_pointer.data, current_pointer.data,next_pointer.data))
      self.print_list()
  
  # Module to arrange the list in Zig-Zag Fashion i.e. Every alternate element will be either reverse of the previous element 
  def zig_zag_list(self):
    # For Performing ZigZag the list should be first odd even segregated.
    print("Performing Odd Even Segregation.")
    self.odd_even_list()

    # find last odd element
    last_odd_element = self.head
    while last_odd_element.next.data%2 != 0:
      last_odd_element = last_odd_element.next
    print("Last odd element: %s" %last_odd_element.data )
    
    even_pointer = last_odd_element.next
    print("First even element: %s" % even_pointer.data)

    # rearrange
    prev_pointer = None
    current_pointer = self.head
    next_pointer = current_pointer.next
    while even_pointer != None and next_pointer != last_odd_element:
      
      if next_pointer.data %2 !=0:
        last_odd_element.next = even_pointer.next
        current_pointer.next = even_pointer 
        even_pointer.next = next_pointer
        even_pointer = last_odd_element.next
        next_pointer = current_pointer.next
      else:    
        current_pointer = current_pointer.next.next
        next_pointer = current_pointer.next 

      self.print_list()
      print("[current:%s, next:%s]" %(current_pointer.data,next_pointer.data))

    
if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  """For Demo Inserting Elements in order"""
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(8)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(9)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List before arrangement") 
  ll_obj.print_list()
  
  print("4. Calling Linked List Arrangement")
  ll_obj.zig_zag_list()

  print("5. Linked List after arrangement")
  ll_obj.print_list()
