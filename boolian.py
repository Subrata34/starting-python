#bool = True
#print(bool)
cod=123.88
print(type(cod))
#complex number data
compound =45j
print(type(compound))
# string type data :
yourname="Amgonota"
myname="titu"
print(yourname + myname) #concate kora
print(yourname+ '  '+myname)
print('my name is '+ myname)
#Boolen data 
Bool=True
print(Bool)
print(type(Bool)) #check boolen
x = 5
print(type(x))
#string formating 
number_1=20;
number_2=80;
print(f"my age is {number_2}and my roll number is {number_1}")
#Binary type data 
somenumber=[3,5,7,9,67,79,89,49,49,240] #byte range 256
b=bytes(somenumber)
print(type(b))
#binary type data array 
somenumber=[3,5,7,9,67,79,89,49,49,240] #byte range 256
b1=bytearray(somenumber)
print(type(b1))
b1[0]=150
print(b1[0])
#None types of data 
q=None
print(type(q))
#List array
x=['nibi','khabi','chabi','habi','urbi']
x[0]='corbi'
print(x)
#tuple type of data 
tup=(12,30,31,80,60,70) #tuple emutable 

print(type(tup))
#range type data
ran=range(6)
for i in ran :
   print(i)