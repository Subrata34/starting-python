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