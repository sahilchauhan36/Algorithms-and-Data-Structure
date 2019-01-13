# This is a basic program for Bubble Sort by Sahil Chauhan
# Bubble Sort is one of the easiest Sorting algo with N^2 Complexity.
def bubble_sort(a):
  num = len(a)

  for i in range(num-2):
    for j in range(num-i-1):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
  
  return a 

a = [10,3,4,5,2,1,7,8,9,6]

print("Array before Bubble Sort :")
print(a)

bubble_sort(a)

print("Array after Bubble Sort :")
print(a)
