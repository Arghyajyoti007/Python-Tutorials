# JSON : JavaScript Object Notation
# Used to storing and exchange data between Server and web application

import json
#parse : is a kind of method, where one string of data, gets converted into a different kind of data.

person = '{"name":"Bob", "language":["English","French"]}'
person_dict = json.loads(person)

# print(person_dict)
# print(person_dict['language'])

with open("data.json") as f:
    data = json.load(f)

print(data)
#to see json file properly
print(json.dumps(data, indent=4, sort_keys=True))


person = {"name":"Bob",
          "age" : "12",
          "language":["English","French"]
          }
person_json = json.dumps((person))
# print(person_json)

#In python
# dict
# list
# tuple
# str
# int
# float
# Bool
# None
# only these objects are equally can be converted into json

#writing to a json file
with open('person.txt','w') as json_file:
    json.dump(person,json_file)

