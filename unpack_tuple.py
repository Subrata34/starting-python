
#unpack tuple
fruits=( 'chari','mango','bananna ','apple ','watermalon')
(a,b,c,d,h)=fruits
print(a)

#again method (unpack tuple one variable )

(*e,)=fruits
print(e)
(*p,s)=fruits
print(s)
#different method 
(f,*g)=fruits
print(g)
#different method 
(o,*k,l,n)=fruits
print(k)
