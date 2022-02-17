#Basics Tata Types:
'''
các kiểu dữ liệu cơ bản trong python: bool,none,int,float, str
'''

'''
topic #0: bool & none
'''


# [] bool True & false
var_bool = True
[] type(): Dynamically typed
print(type(var_bool))


#Numerically, they're evaluated as integers with value 1 (True), 0 (False)
a = 4 + True
print(a)
b = False
if b == 0:
    print("B is 0")
[] None: Phần tử không
var_none = None
print(type(var_none))
None is often used as a placeholder for optional or missing value.
It evaluates as False in conditionals.
email_address = None
email_address = "thangquangloi21@gmail.com"
if email_address:
   print(f"Email address is {email_address}")
else:
   print(f"Email address is empty or {email_address}")
'''
Topic #1: Number (int & float)
'''


# [] Numbers: int (Integer = Số Nguyên) & float (Floating point numbers = Số Thực)
print("1 =",type(1)) #int
print("0 = ",type(0))
print("-10 = ",type(-10))

print("0,0 = ",type(0.0)) #float
print("3,4 = ",type(3.4))
print("4E2 = ",4E2,type(4E2)) #4*10^2



#[] Arithmetic: Các Phép Toán: + - * / ** / // %
print(10+3) # 13
print(10-3) # 7
print(10*3) # 30
print(10**3) # 10*10*10 = 1000
print(10/3) # 3.333333
print(10//3) # 3
print(10%3) # 10 chia 3 = 3 du 1



# [] Basic Function (Hàm Cơ Bản)
print(pow(10,3))#10**3 = 1000
print(abs(-6.9)) #6.9
print(round(6.69)) #7
print(round(4.468, 2)) #4.47 -> làm tròn đến số thứ hai
print(bin(512)) # 'Ob1000000000 ' --> binary format(nhi phan)
print(hex(512)) # '0x200' --> hexadecimal format(thap luc phan)
