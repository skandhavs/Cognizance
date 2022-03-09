import numpy as np
np.set_printoptions(linewidth=np.inf)
my_array = []
a = int(input("Enter the size of array:"))
for i in range(a):
    print("Element",int(i))
    my_array.append(int(input()))
my_array = np.array(my_array)
print("The vector you have entered is ",(my_array))
mod_arr=np.zeros(len(my_array)+((len(my_array)-1)*5))
mod_arr[::6]=my_array
print("The modified array is")
print(mod_arr)