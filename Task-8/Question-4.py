import pandas as pd
my_series = []
a = int(input("Enter the number of words in your sentence:"))
for i in range(int(a)):
    print("The",int((i)+1),"word of the sentence")
    my_series.append((input()))
my_series = pd.Series(my_series)
upp_series = my_series.map(lambda x: x[0].upper() + x[1::])
upp_series=pd.Series(upp_series)
print("The sentence is")
for i in range(a):
    print(my_series[i],end=" ")
print("\nThe changed sentence is")
for i in range(a):
    print(upp_series[i],end=" ")    