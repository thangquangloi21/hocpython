'''
Ham An Danh - Lamdba trong Python
lambda arguments: expression
'''
# A lambda function is a small (one line) anonymous function
# that is defined without a name.
# a lambda function that adds 69 to the input argument

# codexplore = lambda x,y,z : x + y - z
# print(codexplore(4,6,7))

'''
Custom sorting using a lambda function as key parameter
'''
# coordinate2d = [(6,9),(9,6),(-1,3),(2,10)]
# print("1 :",sorted(coordinate2d)) #sap xep tu be toi lon theo bien x
# print("2 :",sorted(coordinate2d,key=lambda point: point[1])) #sap xep tu be toi lon theo bien y

# number_list = [5,3,-2,5,7,53,32,-5,-7]
# print(sorted(number_list)) #sap xep tu be den lon
# print(sorted(number_list,key = lambda x:abs(x))) #sap xep tu be den lon theo tri tuyet doi

'''
Use lambda for map function
'''
# map(func, seq), transforms each element with the function.
# list_keyword = ["thangquangloi","toi nguoi","yen bai"]
# print(list(map(lambda x: x.title(),list_keyword)))
#
# new_list = [keyword.title() for keyword in list_keyword]
# print(new_list)
# viet chu dau tien in hoa

'''
filter(func, seg), returns all elements for which func evaluates to True
'''
# list_number = [1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x%2 != 0,list_number)))
#
# new_list = [x for x in list_number if x%2!=0]
# print(new_list)  #in so chan ra trong list

'''
reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
func takes 2 arguments.
'''
from  functools import  reduce
sequence = [1,2,3,4,5,6,7,8,9]
# print(reduce(lambda a,b: a+b,sequence))
# print(reduce(lambda a,b: a if a > b else b,sequence))
