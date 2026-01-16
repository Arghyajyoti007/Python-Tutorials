import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fxx(n):
    time.sleep(5)
    return n*5

print(fxx(5))
print("done for 5")
print(fxx(4))
print("done for 4")
print(fxx(5))
print("done for 5")
print(fxx(4))
print("done for 4")