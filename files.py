openfiles= open("text.text", "r")

print(openfiles.read())

wr=open("hablu.pdf","a")
wr.write("this is pdf files in this folder\n ")
print(wr.read())
