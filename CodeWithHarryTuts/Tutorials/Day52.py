# Lambda Function
# def double(x):
#     return x*2
double = lambda x:x*2
cube = lambda x:x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(3,5,10))

# Use of Lambda Function
def appl(fx,value):
    return 6+fx(value)

ans=appl(cube, 2)
print(ans)