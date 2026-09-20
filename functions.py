#functions definitions
def sum(a, b):
     s = a+b
     print("sum is", s)
     return s
sum(2, 3)
sum(4, 5)

#functions without parameters
def print_hello():
    print("hello")

    print_hello()
    print_hello()
    print_hello()
#average of three numbers
    def calc_avg(a, b, c):
        sum = a+b+c
        avg = sum/3
        return avg

    calc_avg(3, 6, 7) 

#print lenght of string

cities = ["delhi", "mumbai", "noida", "moradabad"]
heroes = ["thor", "ironmen","caption america", "shaktiman"]

def print_len(list):
    print_len(cities)
    print_len(heroes)

#print element in a list in a single line
heroes = ["thor", "ironmen","caption america", "shaktiman"]

def print_list(list):
    for item in list:
        print(item, end=" ")

    print_list(heroes)


#print factorial of n

def fact(n):
    
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print(fact)

        fact(5)
#convert USD into INR

def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD =", inr_val, "INR")

    converter(1)   # 1 USD = 83 INR

    #recursion

    def show(n):
        if(n==0):
            return
        print(n)
        show(n-1)

        show(5)

    #returns n! in recursive function


    def fact(n):
        if(n==0 or n==1):
            return 1
        else:
            return  n*fact(n-1)