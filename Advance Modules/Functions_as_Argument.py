def disp(sh):
    return "Display Funtion "+sh()

def show():
    return "Show Function"

print(disp(show))

def trial(x,y):
    print(x+y)

trial(5,6)
trial("Hello","World")

list = ['car','bus','bike','scooter']
def loop(x):
    print(x*3)

def map_simple(crazy,list):
    for items in list:
        crazy(items)

loop(list)
map_simple(loop,list)