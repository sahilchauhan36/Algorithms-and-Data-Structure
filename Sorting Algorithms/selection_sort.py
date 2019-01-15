# This Program explains Selection Sort Algorithm which actually takes first element and find if any element is smaller than it, swap and so on.

def selection_sort(a):
  num = len(a)
  
  for i in range(0,num-1):
    min_index = i
    
    for j in range(i+1, num):
      if a[min_index] > a[j]:
        min_index = j
    
    if min_index != i:
      a[i], a[min_index] = a[min_index], a[i]

  return a

a = [2,5,1,3,9,7,4,6,8,10]

print("Array before Sorting :")
print(a)

selection_sort(a)

print("Array after Sorting :")
print(a)
