
#SyntaxError
#IndexError: list index out of range
#ModuleNotFoundError: No module named 'notamodule'
#KeyError: 3
#ImportError: cannot import name 'cube' from 'math' (unknown location)
#StopIteration
#TypeError
#NameError: name 'b' is not defined
#ZeroDivisionError
#KeyboardInterrupt


"""
>>> print "Hello"
  File "<stdin>", line 1
    print "Hello"
    ^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> ^X
KeyboardInterrupt
>>> cls
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'cls' is not defined
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>> l=[1,2,3]
>>> l[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> import notamodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'notamodule'
>>> d={'1':"qwe",'2':"wer"}
>>> d[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
>>> from math import cube
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'cube' from 'math' (unknown location)
>>> it=iter([1,2,3])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
KeyboardInterrupt
>>> "12"+12
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>>
KeyboardInterrupt
>>> int('xyz')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'xyz'
>>> age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> it
<list_iterator object at 0x000001939F81BBB0>
>>> l
[1, 2, 3]
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> x=100/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
KeyboardInterrupt
>>> name=input("Enter name")
Enter nameTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyboardInterrupt
>>>

"""
