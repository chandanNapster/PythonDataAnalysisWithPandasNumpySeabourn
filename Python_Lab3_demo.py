x = 2 + 3
print("The {0} output is {1}".format(x, "ron"))


print(type(3))

def add(x,y):
    if str(type(x)) == "<class 'int'>" and str(type(y)) == "<class 'int'>":
        return x + y 
    elif  str(type(x)) == "<class 'int'>" and str(type(y)) == "<class 'str'>":
        print("NOT POSSIBLE")   

print("The output of add method is {0}".format(add(2,"RON")))    

# i = 10
# j = 20
# k = 30

# if i==j and i == k and j==k:
#     print("Hello")
# else:
#     print("Yellow")    