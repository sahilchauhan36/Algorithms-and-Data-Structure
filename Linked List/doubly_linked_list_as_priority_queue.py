# This program explains the concept of Priority list using Doubly Linked List

class node():
  def __init__(self, data, priority):
    self.prev = None
    self.next = None
    self.data = data
    self.priority = priority
  
class linked_list:
  def __init__(self):
    self.head = None

  # Module to insert an element in the linked list 
  def insert(self, data, priority):
    print("[%s,%s]" % (data,priority), end = ' ')
    Node = node(data, priority)
    # Check if there are no elements in the list insert it and update head pointer
    if self.head == None:
      self.head = Node
    else:
      # If the New element is having max priority
      if self.head.priority >= priority:
        self.head.prev = Node
        Node.next = self.head
        self.head = Node
      else:
        current_node = self.head

        # Traverse till element is having low priority an it is not the end of list 
        while current_node != None and current_node.priority < data:
          parent_node = current_node
          current_node = current_node.next

        Node.prev = parent_node
        parent_node.next = Node
        Node.next = current_node
        
        # Condition to check if element is having last element with max priority
        if current_node != None:
          current_node.prev = Node

  # Module to print the linked list
  def print_list(self, print_data=True):
    print("( ", end =' ')
    current_node = self.head
    while current_node != None:
      if print_data is True:
        print("[%s , %s]" %(current_node.data, current_node.priority) , end =' ')
      else:
        print("%s," %current_node.priority, end =' ')
      current_node = current_node.next
    print(")")

if __name__=='__main__':
  print("1. Create a Linked List Object")
  ll_obj = linked_list()
  
  # Insert Elements in linked list 
  print("2. Insert elements in Linked List")
  ll_obj.insert(1,2)
  ll_obj.insert(2,1)
  ll_obj.insert(4,3)
  ll_obj.insert(5,1)
  ll_obj.insert(6,7)
  ll_obj.insert(7,9)
  ll_obj.insert(6,5)
  ll_obj.insert(5,4)
  ll_obj.insert(6,6)

  # Print the list with data
  print("\n3. Print the list with data")
  ll_obj.print_list()

  # Print the list 
  print("3. Print the list without data (Priority only)")
  ll_obj.print_list(print_data=False)

