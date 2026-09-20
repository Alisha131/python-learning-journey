#loops in python

# 1. while loops
count = 1
while count < 5 :
 print("alisha") 
 count += 1

 #print number 1 to 5
 #i = 1
 #while i <= 5:
 #print(i)
 #i += 1

 #continue statement
i = 0
while i <= 5:
 if(i == 3):
  i+=1
  continue
 print(i)
 i+=1


#for loops
list = ["patato", "brinjal", "cucumber", "ladyfinger"]
for i in list:
 print(i)

 #range()
 print(range(5))

 seq = range(9)
 for i in seq:  #for i in range(9)
  print(i)