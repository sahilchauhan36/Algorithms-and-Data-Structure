# This program explains how to find intersection point of two linked list.

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

  def length(self):
    length = 0
    current_node = self.head
    while current_node != None:
      current_node = current_node.next
      length = length + 1
    return length
  
  def create_intersection(self, linked_list_2):
    # traverse given List 4 steps
    current_node = linked_list_2.head
    count = 0
    while count != 4:
       current_node = current_node.next
       count = count + 1
    
    # traverse current list till end
    current_node_2 = self.head
    count = 0
    while current_node_2.next != None:
      current_node_2 = current_node_2.next
    
    # update current list end with givem list 4th element
    current_node_2.next = current_node

  def find_intersection(self, linked_list_obj):
    length_1 = self.length()
    #print("[Length 1 : %s]" % length_1)
    length_2 = linked_list_obj.length()
    #print("[Length 2 : %s]" % length_2)
 
    count = abs(length_1 - length_2)
    # If first List is longer 
    if length_1 > length_2:
      current_node = self.head
      while count != 0:
        current_node = current_node.next
        count = count - 1
      current_node_2 = linked_list_obj.head
    else: # If Second List is longer
      current_node = linked_list_obj.head
      while count != 0:
        current_node = current_node.next
        count = count - 1
      current_node_2 = self.head

    # Comman for both scenarios
    # Traverse Both the list parallely and compare the nodes of both the lists
    while current_node_2 != None and current_node != None:
      if current_node.data == current_node_2.data:
        print("Intersection Point is  %s" % current_node.data)
        return
      current_node = current_node.next
      current_node_2 = current_node_2.next

    # If there is no intersection point 
    if current_node_2 == None and current_node == None:
      print("No element found !")
      return

if __name__=='__main__':
  # Create a linked list
  print("1. Create a Linked List Object 1")
  ll_obj = linked_list()
  

  # Update head of the linked list 
  print("2. Insert Elements in Linked list 1")
  ll_obj.insert(1)
  ll_obj.insert(2)
  ll_obj.insert(3)
  ll_obj.insert(4)
  ll_obj.insert(5)
  ll_obj.insert(6)

  # Print the list
  print("3. Linked List 1") 
  ll_obj.print_list()

  print("4. Create a Linked List Object 2")
  ll_obj_2 = linked_list()
  

  # Insert elements in list 2 and create one intersection
  print("5. Insert Elements in Linked list 2")
  ll_obj_2.insert(11)
  ll_obj_2.insert(22)
  ll_obj_2.insert(33)
  ll_obj_2.insert(44)
  ll_obj_2.insert(55)
  ll_obj_2.insert(66)

  # Print the list
  print("6. Linked List 2") 
  ll_obj_2.print_list()

  # Create Intersection  
  print("7. Create Intersection in Linked list 2")
  ll_obj_2.create_intersection(ll_obj)

  # Print the list
  print("8. Linked List 2 after intersection creation") 
  ll_obj_2.print_list()

  # Get Intersection
  print("9. Find Intersection") 
  ll_obj.find_intersection(ll_obj_2)
