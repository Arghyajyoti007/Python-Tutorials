numbers = [1,2,3,4,5,6,7,8,9,100]
for x in numbers:
    print(x)

x = "Fruits"
for a in x:
    print(a)

#break
for x in numbers:
    print(x)
    if x==5:
        break

#continue
for x in numbers:
    if x==4:
        continue
    print(x)

for x in range(100):
    print(x)

for x in range(40, 100):
    print(x)

#while loop
i=1
while i<6:
    print(i)
    i+=1

j=1
while j<6:
    j += 1
    if j==3:
        continue
    print(j)

