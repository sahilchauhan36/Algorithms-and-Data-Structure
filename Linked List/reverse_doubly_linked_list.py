# This program explains the concept reversal of Doubly Linked List

class node():
  def __init__(self, data):
    self.data = data
    self.prev = None
    self.next = None
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data):
    
    Node = node(data)
    if self.head == None:
      self.head = Node
      print("\t", end='')
    else:
      temp_node = self.head
      while temp_node.next != None: 
        temp_node = temp_node.next
      temp_node.next = Node
      Node.prev = temp_node
    print("%s" % data, end = ' ')

  # Module to print the linked list
  def print_list(self):
    print("\t[", end =' ')
    temp_node = self.head
    while temp_node != None:
      print("%s" %temp_node.data , end =' ')
      temp_node = temp_node.next
    print("]")
  
  # Module to reverse doubly linked list
  def reverse(self):
    current_node = self.head
    while current_node != None:
      temp = current_node.prev
      current_node.prev = current_node.next
      current_node.next = temp
      current_node = current_node.prev 

    self.head = temp.prev

if __name__=='__main__':
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  
  # Insert Elements in linked list 
  print("2. Insert elements in Linked List")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list 
  print("\n3. Print Linked List")
  ll_obj.print_list()

  # Perform Reverse
  print("4. Perform Reverse")
  ll_obj.reverse()

  # Print the list 
  print("5. Print Linked List")
  ll_obj.print_list()
