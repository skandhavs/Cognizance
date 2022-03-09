import numpy as np
my_array1= []
a = int(input("Enter size of first array :"))
for i in range(a):
    print("Element",int(i)) 
    my_array1.append(int(input()))
my_array1 = np.array(my_array1)
print("The first array is ",my_array1)
my_array2= []
b = int(input("Enter size of second array :"))
for i in range(b):
    print("Element",int(i)) 
    my_array2.append(int(input()))
my_array2 = np.array(my_array2)
print("The second array is ",my_array2)
print("Are the two arrays equal? ",np.array_equal(my_array1,my_array2))