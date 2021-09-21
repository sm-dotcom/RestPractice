import numpy as np

nums = [1,2,3,4,5,6]
even = []
odd = []


 # def even_odd(nums):
for x in nums:
     # print(x)
       if (x % 2 == 0):
        # print("this is even",x,even.append(x))
        even.append(x)
       elif (x % 2 != 0):
         # print("this is odd",x, odd.append(x))
         odd.append(x)


# for i in even:
print("this is even array :", even)

# for j in odd:
print("this is odd :", odd)

