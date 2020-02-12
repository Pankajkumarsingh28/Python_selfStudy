a='This is Testing World'
a1=''
b='My Testing World'
b1=''
l1=(len(a))
l2=(len(b))
print(l1)
print(l2)
for i in range (l1-1,10,-1):
    a1=a1+a[i]
print(a1)
print(len(a1))
for j in range (l2-1,5,-1):
    b1=b1+b[j]

print(b1)
print(len(b1))
if (a1==b1):
    print("Both string are equal")
else:
    print("They are not equal")
