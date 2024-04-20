newtuple=[1,2,3,'vaggo',True,False]

print(newtuple[-2])     #index start from -1 and lifte site
#Rang of  tuble 
print(newtuple[1:6])

#update tuple 
thistuple=['hamdu','habib','khokon','sakib']
a=list(thistuple) #convert to the list tuple and then append 
a.append("sakil") #append this tuple 
thistuple=tuple(a) #store the tuple 
print(thistuple)
