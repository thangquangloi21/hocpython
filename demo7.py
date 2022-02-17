'''
1. Creating a list
'''

# list_1 = ["banana", "apple", "orange", "cherry"]
# list_2 = [5, "quang loi", False,None]
# list_3 = list()
#
# print(list_3)


'''
2. Access elements: Truy cập đến các giá trị trong list
'''
my_list = [1,2,3,3,3,'3','3','3',True]
# print(len(my_list)) #dem so gia tri trong list
# print(my_list[2]) #in ra gia tri cua vi tri thu 2
# print(my_list.index('3')) #tim vi tri cua gia tri '3' (dem tu 0)
# print(my_list.count('3')) #ham dem so gia tri trong list
# for item in my_list: #in ra toan bo gia tri trong my list
#     print(item)


# Python's built-in enumerate function

# presidents = ["Washington", "Adams", "Jefferson","Madison", "Monroe", "Adams", "Jackson"]
# print(presidents)
# for index, president in enumerate(presidents,start=1): #ham enumerate reurn phan tu va vi tri trong list
#     print(f"Persident # {index}: {president}")

# Sicing
# : is called slicing and
# has the format [ start : end : step ]

# my_list = [1, 12,True,'3'] #cat list
# print(my_list[::-1])

'''
3. List Operations & Useful Methods
3.1. Add to List
'''
my_list = [5,6,23,62,161,5,67,1,6]
# print(my_list + [100,"TQL"])
# print(my_list)
# my_list.append(100) #them vao list gia tri
# print(my_list)
# print(my_list.insert(3,5)) #them gia tri 5 vao vi tri 3
# print(my_list)

'''
3.2. Remove from List
'''
# print(my_list.pop(1))
# my_list.remove(4) #xoa gia tri dau tien
# del my_list[2] xoa gia tri
# print(my_list)

'''
3.3. Sorting sap xep phan tu
'''

# my_list.sort() #xep tang dan trong list
# my_list.sort(reverse=True) #giam dan
# my_list.reverse() #dao nguoc lai vi tri cua list
# print(sorted(my_list))# tao list moi va sap xep tu nho den lon
# print(list(reversed(my_list))) # tao ra list moi dao vi tri nguoc lai
# print(my_list)


'''
3.4. Useful operations
'''
print(max(my_list)) #tim so lon nhat
print(min(my_list)) # tim so nho nhat
print(sum(my_list)) #tong mylist