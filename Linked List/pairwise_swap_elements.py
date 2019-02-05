"""
This program explains the program to pairwise swap elements 
e.g. If Linked List = [1,2,3,4,5,6]
     Output = [2,1,4,3,6,5]
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
  
  # Module to pairwise swap elements
  def pairwise_swap_elements(self):
    current = self.head.next
    next = current.next
    prev = self.head

    # Handling the case when the number of elements are <=2
    if current == None or next == None: 
      return 

    # update head
    self.head = current

    while (True):
      #print("[%s,%s,%s]"%(prev.data,current.data,next.data))
      # Update pointer of current node to previous Node
      next = current.next
      current.next = prev

      # Check if coming nodes are None
      if next == None or next.next == None:
        prev.next = next
        break

      # skip one node 
      prev.next = next.next # Important Step as next of previous element[1] after this will be forth element[4]
      prev = next
      current = prev.next
    
if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list")
  """For Demo Inserting Elements in order"""
  for i in range(1,15):
    ll_obj.insert(i)

  # Print the list
  print("3. Linked List ") 
  ll_obj.print_list()
  
  # Print the list
  print("4. Pairwise Swap Elements") 
  ll_obj.pairwise_swap_elements()

  # Print the list
  print("5. Linked List after Pairwise Swapping Element") 
  ll_obj.print_list()
