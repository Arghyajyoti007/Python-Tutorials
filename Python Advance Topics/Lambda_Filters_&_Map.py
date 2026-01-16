# lambda
# lambda is a small and anonymous function
# *** it can take any number of arguments, but can have only one expression
# expression : a+2, a+3, a+4
x = lambda a: a + 20
# print(x(5))
x = lambda a, b: a + b
# print(x(5,30))

# def f1(x):
#     return x+10
#
# print0(f1(5))

f1 = lambda a: a + 10


# print(f1(50))

def f2(x):
    return lambda a: a * x


doub = f2(2)
# print(doub(11))


# filter
#  runs a function on all items in a collection, but only stores the true values

# def prime(x):
#     for n in range(2,x):
#         if x % n == 0:
#             return False
#         else : return True

age = [25,14,85,18,6,55,44,552,333,66]
def function(x):
    if x>=18:
        return True
    else:
        return False

adults = filter(function, age)
for c in adults:
    print(c)




# map()
# runs a function on all items in a collection
coll = [10,20,30,40,50]
coll2 = []
coll3 = list(map(float,coll))


for x in coll:
    coll2.append((float(x)))

print(coll2)
print(coll3)

double = list(map(lambda x : x*2, coll))
print(double)