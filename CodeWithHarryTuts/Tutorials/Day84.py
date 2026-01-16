import time

def usingFor():
    for i in range(100):
        print(i)

def usingWhile():
    i=0
    while(i<100):
        print(i)
        i+=1


t1 = time.time()
usingFor()
print(time.time()-t1)

t2 = time.time()
usingWhile()
print(time.time()-t2)

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)

print(5)
time.sleep(5)
print("Printed after 5secs")