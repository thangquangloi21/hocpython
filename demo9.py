'''
Topic 8 - Dictionary: một tập hợp các cặp key-value không có thứ tự, có thể thay đổi và lập chỉ mục
Dictionary được khởi tạo với các dấu ngoặc nhọn {} và chúng có các khóa và giá trị (key-value).
Mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất,
trong khi đó value có thể là bất kỳ kiểu giá trị nào.
Key phải là một kiểu dữ liệu không thay đổi (immutable) như chuỗi, số hoặc tuple.
'''

# Create a new Dictionary: A dictionary is a collection which is unordered, changeable and indexed.
# A dictionary consists of a collection of key-value pairs.

my_dict = {"name": "TQL","content":
    "Programming Youtobe Channel","city":"Hanoi"}
# print((my_dict))
# my_list2 = dict(name = "loi",city="yen bai")
# print(my_list2)

# Access items
# conten_in_dict = my_dict["content"]
# print(conten_in_dict)
# print(my_dict["age"])

# Check for keys
# use if .. in .

# if "name" in my_dict:
#     print(my_dict["name"])
# else:
#     print("deo co gi")

# use try except I

# try:
#     print(my_dict["content"])
# except KeyError:
#     print("deo co key") #lay gia tri trong key

# Add and change items (key-value) pairs
# add a new key

# my_dict["email"] = "thangquangloi21@gmail.com"
# them vao key

# or overwrite the value on existing key
# my_dict["email"] = "thangquangloi23@gmail.com" #thay doi gia tri trong key
# print(my_dict)

# Delete items
# delete a key-value pair

# del my_dict["city"] #xoa key trong mang

#pop()
# print("pop value: " + my_dict.pop("city")) #xoa va lay ra gia tri


#.popitem()
# my_dict["age"] = 25
# print(my_dict)
# my_dict.popitem() # xoa phan tu cuoi cung duoc them vao
# print(my_dict)

# Looping through Dictionary
# loop over keys
# for key in my_dict.keys():
#    print(key, my_dict [key])

# loop over keys and values
# for key, value in my_dict.items():
#    print(key,value)

