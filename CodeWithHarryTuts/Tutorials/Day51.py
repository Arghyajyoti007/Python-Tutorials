# seek() in file handling
# Move to the 10th byte in the file

with open('file.txt','w') as f:
    print(type(f))
f.seek(10)
f.write("Hello World!")

print(f.tell())
f.truncate(5)

