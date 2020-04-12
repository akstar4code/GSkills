import bisect
arr = [0,1,2,3,3,4,4,5,8,10]
# O(log(n)) uses binary search technique
print(bisect.bisect(arr,3)) #rightmost elements place selected
print(bisect.bisect_left(arr,3)) # Leftmost elements postion is selected
print(bisect.bisect_right(arr,3)) #rightmost elements postion is selected
# O(log(n)) uses binary search technique
bisect.insort(arr,3) #insert element at rightmost elements in list
print(*arr)
bisect.insort_left(arr,4) ##insert element at leftmost elements in listr
print(*arr)
bisect.insort_right(arr,4) #insert element at rightmost elements in list
print(*arr)