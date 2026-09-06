#dictionary
info = {
    "key" : "value",
    "name": "alisha",
    "subjects" : ["python", "c", "java"],
    "topics" : ("dict", "set"),
    "age" : 20,
    "is_adult" : True,
    "marks" : 99,
    "score": {   #nested dictionary
        "phy": 98,
        "chem": 99,
        "maths":100
    }
}
print(info)
print(type(info))  #type
print(info["name"])
print(info["age"])
print(info["subjects"])
print(info["topics"])

info["name"] = "ellieyy"  #update the dictionary value
print(info["name"])
\
print(info["score"]["chem"])

 #dictionary methods
print(info.keys())
print(list(info.keys())) #type caste in list
print(len(info.keys()))
print(info.items())
print(info.get("subjects"))
info.update({"city" : "delhi"})
print(info)

#set in python

myset = {1, 2, 2, 2, 3, 3,  4, "alisha", "zakir"}
print(myset)
print(type(myset))
print(len(myset))

collection = set()  #empty set; syntax
print(type(collection))

#methods of set

collection.add(9)
collection.add(8)
collection.add(9)
collection.add(10)
collection.add("ellieyy")
collection.add((6, 88, 97))
collection.add(2)

collection.remove(9)

print(collection.add(55))  #none
print(collection.pop()) #randomly pop out the element

print(collection)

#collection.clear-it clears all elements
print(len(collection))

print(myset.union(collection))  #union in set

print(myset.intersection(collection)) #intersection in set