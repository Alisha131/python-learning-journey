str1 = "this is a string.\n we are creating it in python"
str2 = 'alisha'
str3 = """ellieyyyy"""
final_str = str2 + " " + str3
print(str1)
print(str2 + str3)

print(str2[0])
print(str2[2])

print(len(str1))
print(len(str2))
print(len(final_str))

print(str2[1:4])

str = 'i am a coder'
print(str.endswith("er"))

print(str.capitalize())
print(str)

print(str.replace("a", "o")) #we can also replace words

print(str.find("r")) #we can also find words

print(str.count("a")) #we can also counts word

#conditional statements
age = int(input("enter your age :"))
if(age >= 18):
    print("adult")  #indentation- proper spacing
    print("can vote")
elif(age<18):
    print("child")

