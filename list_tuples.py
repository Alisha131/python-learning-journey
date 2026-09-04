#lists in python
marks = [92, 98, 99, 91]
print(marks)

print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])

print(len(marks))

#slicing of lists
print(marks[1:])

#list methods
marks.append(95)
print(marks)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks.reverse()
print(marks)

marks.insert(3, 100)
print(marks)

marks.pop(3)
print(marks)



list = ["banana", "litchi", "apple"]
list.sort()
print(list)



student = ["alisha", 99, 20,]
print(student)

student[0] = "ellieyy"
print(student)

#tuples in python

tup = (9, 6, 8, 2, 5, 2)
print(type(tup))
print(tup[0])
print(tup[1])

#methods of tuple

print(tup.index(2))
print(tup.count(5))
