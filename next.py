#type casting : converting work type casting 
name=40
print(int(name))   #this convert iniger from string 

#python list :
li=[1,90,200]
print(li)
li[1]=20
print(li) 

# Access list item :
list =['google','gmail','instagram','microsoft']
print(list)
list[2]='facebook'
print(list)

# append {this function is add data in this list  }
list.append('google chorme')
print(list )

#insert {this function is add data by index number }

list.insert(3,'Youtube ')
print(list )

#remove {this function is remove the data from list }
newlist =['habib ','mamun','jamil','khairul','kumkum',800,900,500,400]
print(newlist)
newlist.remove('jamil')
print(newlist)

#pop {this function is remove index number }
newlist.pop(1)
print(newlist)

#del {this function is remove one index from this list }
del newlist[1]
print(newlist)

#clear {this function is remove in the world }
print(newlist)
newlist.clear()
print(newlist)

#you can loop though the list item

Looplist =['rahul pit singh','konona ranuath','janovi kapur','Kira adbani','Kirti sonam']

for team in Looplist :
    print(team)

# Use the range() and len() functions to create a suitable iterable.
for i in range(len(Looplist)) :
    print(i)

#Print all items, using a while loop to go through all the index numbers

Looplist =['rahul pit singh','konona ranuath','janovi kapur','Kira adbani','Kirti sonam']

y=0
while y<len(Looplist):
    print(Looplist[y])
    y=y+1
