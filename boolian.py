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

#Arithmetic operator 
a=10
b=28
print('this is addition a and b :',a+b)
#Subtraction
print(' a and b subtraction ',a-b)
#Multiplication 
print('a and b multiplication :',a*b)
#Division 
print('a and b between number Division :',a/b)
#modulues %
print('a and b between number modulues :',a%b)
#Exponential **
x_1=5
b_2=2
print('a and b Exponential number :',x_1**b_2)
#Floor division //
sum_1=15
sum_2=7
print('sum_1 and sum_2 between floor division : ', sum_1//sum_2)

#Assignment Operator 
d=10
sum_1=d+5
print(sum_1) #same declaration 2nd process 

h=10
h+=10
print(h)

c=90
c-=10
print(c)

#comparison operator 
h_1=14
g=14
print(h_1==g) #equal operator 

print(h_1!=g) #gather than 
print(h_1>g)  #gather than
print(h_1<g)  # less  than 
print(h_1>=g) #gather than equal 
