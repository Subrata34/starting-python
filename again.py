#List comprehension 
num=[1,2,3,4,5]
# for i in num :
#     print(i*2)
double=[i*2 for i in num]
print(double)

#sort list 
variable=[1,2,4,5,9,6,8]
variable.sort()
print(variable)

latter=["h",'i','j','p','k','m','n']
latter.sort()
print(latter)

#reverse list 
Num=[1,2,3,4,5,6,7,8,9]
Num.sort(reverse=True)
print(Num)

#copy a list 
number=[1,2,3,4,5,6]
copylist=number.copy()
print(number)
print(copylist)

#join the two list 
list_1=[1,2,3,4,5,8]
list_2=[6,4,3,2,6,9]
list_3=list_1+list_2
print(list_3)

list_1.extend(list_2)   #python programming method joining 
print(list_1)