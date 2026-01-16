#read write create append
# f = open("FileHandlingDemo.txt", "r") # "r" -> Read mode
# print(f.read())


#to read specific part of the file
# print('To read specific number of characters')
# print(f.read(30))
#30 represent the number of character we want to read

# print("To read only one line")
# print(f.readline())

#read only one line
# print(f.readline())
# print(f.readline())

#loop through the entire file
# for x in f:
#     print(x)


#to close file
#f.close()


#Append mode
# f = open("FileHandlingDemo.txt","a") #"a" -> Appned
# f.write("A complete appended line")
# f.close()

# f=  open("FileHandlingDemo.txt", "r")
# print(f.read())


#Write Mode
#overwrite the file
# f = open("FileHandlingDemo.txt","w")
# f.write("A new Line from write mode")
# f.close()
#
# f=  open("FileHandlingDemo.txt", "r")
# print(f.read())


#Create Mode
# f = open("New.txt","x") #"x" -> to create new file
# f = open("NewFile.txt","w") #in Write mode if there is no file available, then it will automatically create one.

#to delete file
# import os
#os.remove("New.txt")
#
# if os.path.exists("NewFile.txt"):
#     os.remove("NewFile.txt")
# else:
#     print("File not present")


