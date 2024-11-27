# # print("hello world")
# # #hhhah
# # print(
# #     '''this is line 1
# #     this is line 2'''
# # )

# # # a=5
# # # b=5.0
# # # c="ram"

# # # print(type(a))
# # # print(type(b))
# # # print(type(c))

# # a= range(10)
# # b= range(5,10)
# # c= range(5,10,2)

# # print(type(a),type(b),type(c))


# # for i in a:
# #     print(i)

# # for i in b:
# #     print(i)

# # for i in c:
# #     print(i)      


# # str1 ="Hello"
# # str2 = "world"
# # str3 = str1 + str2
# # print(str1)
# # print(str3*5)
# # print(str3[0:-1])
# # print(str3[0:5])

# # a=['apple', 'banana', 'peach']
# # print(a)
# # a.append('kiwi')
# # a.remove('banana')

# # print(str[0:5])


# # a=('apple', 'banana', 'peach')
# # print(a)

# my_dict= {
#     'name': 'hari',
#     'age': 22
# }
# print(my_dict)
# print(my_dict['name'])
# my_dict['gender'] = 'm'

# my_dict.pop('name')

# #hhhhhhhhh
# my_dict = {
#     "name": "Hemanta",
#     "age": 24,
#     "address": "Gharipatan"
# }

# # for key, value in my_dict.items():
# #     print(f"Key: {key}, Value: {value}")


# for key in my_dict:
#     print(f"key:{key} value:{my_dict[key]}")

# # for value in my_dict.items():
# #     print[f"key:"]    
  

# a= int(5.6)
# print(a)


# a= True
# print(type(a))



# fruits = ['apple','banana', 'watermelon']
 
# for elements in fruits:
#    print(elements )


# for element in "hello":
#     print(element, end='/')   


# colors =['red', 'green', 'blue']
# # print(enumerate(colors))
# for element,value in enumerate(colors):
#     print(element, value)



# a = ["bob", "ova", "rin"]
# b = [20, 21, 22]

# for name, age in zip(a, b):
#     print(name,age)

# #fizzbuzz 
# for x in range(1, 31):
#     if x % 3 == 0 and x % 5 == 0:
#         print("FizzBuzz")
#     elif x % 3 == 0:
#         print("Fizz")
#     elif x % 5 == 0:
#         print("Buzz")
#     else:
#         print(x)


# from mypackage.module1 import greet
# greet()

import mypackage
mypackage.greet()
