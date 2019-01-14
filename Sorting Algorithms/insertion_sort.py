# This Program explains the Insertion Sort which works similiar to the Sorting of a Peck of Cards.
def insertion_sort(a):
  n = len(a)
  for i in range(1,n):
    temp = a[i]
    j = i-1
    while(temp<a[j] and j>=0):
      a[j+1] = a[j]
      j = j-1
    a[j+1] = temp
    print(a)
  return j

a = [10,5,2,4,1,6,9,3,7,8]
# Array before Insertion Sort
print("Array before Insertion Sort")
print(a)

# Call Insertion Sort
insertion_sort(a)

# Array after Insertion Sort 
print("Array after Insertion Sort")
print(a)
