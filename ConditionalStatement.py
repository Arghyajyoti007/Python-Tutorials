#a==b
#a!=b
#a<b
#a<=b
#a>b
#a>=b

a=33
b=33

if a>b:
    print("a>b")
elif a==b:
    print("a==b")
else:
    print("a<b")

#alternative
print("a>b") if a>b else print("a<b")

a=200
c=32
if a>b and c>a:
    print("a")
else:
    print("b")