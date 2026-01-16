# Map, Filter, Reduce
l = [1,2,4,6,4,3]
cube = lambda x:x*x*x

newL = list(map(cube,l))
print(newL)


# FILTER
def filter_function(a):
    return a>4
newnewL = list(filter(filter_function,l))
print(newnewL)

# REDUCE
from functools import reduce
sumNum = reduce(lambda x,y:x+y, l)
print(sumNum)