'''
Topic #2: Strings (Chuỗi Ký Tự) a sequence of characters
'''
String: ordered, immytable, text presentation
use singe or double quotes
my_string = 'Hello World'
my_string = "hello Word 2"
use singe or double quotes
print(my_string,type(my_string))

use singe or double quotes
my_string = 'I\'m a "Cuu duong than cong"'
my_string = "I\'m living in \"Dong lao\""
print(my_string)

backslash if you want to continue in the next line
my_string = "voi mong muon cac ban luyen thanh \
cao thu vo lam"
print(my_string)


Access characters and substrings
my_string = "Hello World"
get character by referring to index
char = my_string[-2]
print(char)
# String is immutable -> Cannot be changed
my_string[0] = "m"

Substrings with slicing
stringName [startIndex:endindex]
start at index 1 and go until index 5 (not include #5)

sub_string = my_string[1:5] #lay tu 1 den 5
sub_string = my_string[:5] #lay tu dau den thu 5
sub_string = my_string[6:] #lay tu thu 6 den het

sub_string = my_string[::-1] # dao nguoc ki tu
sub_string = my_string[::2] #cat doan trong chuoi
print(sub_string)


'''
Concatenate two or more strings
'''

greeting = "Helo, xin chao cac ban "
channel = "TQL"
sentence = greeting + "chao mung cac ban den moi Channel cua " + channel
print(sentence)

join elements of a list into a string: .join()

my_list = ['how', 'are', 'you','doing']
sentence = ' '.join(my_list)
print(sentence)


'''
Iterating
'''

my_string = "Hello xin chao cac ban"
for char in my_string:
    print(char)
if "x" in my_string:
    print("yes")
else:
    print("no")

'''
Basic & Useful Function (Hàm Cơ Bản và Hữu Ích)
'''

# strip()
'I am alone' --> Strips all whitespace characters from both ends.
print("    I am alone   ".strip())
print("On an is land".strip('O')) #xoa O


#split()
print('but life is good'.split())
print('but, very boring'.split(','))

replace()(thay the)

print('Help me'.replace("me","you"))

ham kiem tra
my_string = 'hello, word'
print(my_string.startswith('need')) #kiem tra vi tri dau tien
print(my_string.endswith('fire')) #kiem tra vi tri cuoi cung

print(my_string.find(' ')) #tim vi tri  co the dung index va find

print(my_string.lower()) #chuyen doi hoa thanh thuong
print(my_string.upper()) # chuyen doi thuong thanh hoa

print(my_string.capitalize()) #chuyen doi chu cai dau thanh in hoa

print(my_string.count('o')) #dem so phan tu trong mang

'''
String Formatting
'''
# %, .format (), f-Strings

# %

name = "code nua code mai"
my_string = "cac ban  phai %s" % name
pi = 3.14159
s = "pi number"
my_string = "Variable is %.2f from %s " % (pi,s)
print(my_string)


#.format()
age = 24
height = 170.5
my_string = "I am {} years old;height {:.3f} cm".format(age, height)
print(my_string)


# f-Strings
name = "loi"
pi = 3.14159
age = 20
my_string = f"Pi is {pi:.2f} and my name is {name}; {age} year old"
print (my_string)