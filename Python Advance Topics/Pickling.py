# Pickling : A module in python
# Serialization and Deserialization
# Convert any type of object into bytes (0s and 1s)
# In Machine Learning the data we pass, we need to flatten it first
# 1D data : Point; 2D data : Line
# Pickle is used to convert data from 2d format to 1d format and vice versa
#mainly used in machine learning

import pickle
mydict = {
    '1':'a',
    '2':'b'
}

pickle_file = open("picklefile.txt", "wb") #wb : write byte
pickle.dump(mydict,pickle_file) #used to dump the mydict into pickle_file

pickle_file = open("picklefile.txt", "rb") #rb : read byte
new_dict = pickle.load(pickle_file)
print(new_dict)