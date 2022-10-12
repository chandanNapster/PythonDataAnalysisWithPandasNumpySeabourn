num = 10

# print("The number is {0} and the data type is {1}".format(num, type(num)))


# print(num == 10)
# print(num != 10)
# # print(num <> 10)
# print(num >= 5)
# print(num <= 15)
# print(num < 10)
print(num in [10,15,16] and num not in [23,10,32,56])

print(num in [10,15,16] and not(num not in [23,10,32,56]))

print(num in [10,15,16] and not(not(num not in [23,10,32,56])))

print(num in [10,15,16] and not(not(not(num not in [23,10,32,56]))))



a = True
b = False 

c = a | b 

print(c)