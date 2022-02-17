'''
4. List Comprehensions

List Comprehension giúp bạn viết code ngắn gọn (đặc biệt khi đang ở trong một vòng lặp đã có)
và dễ đọc, nhìn code hơn.
'''

# new_list[<action> for <item> in <iterator> if <some condition>]
# word = "Hello word"
# print([char for char in word])
# for char in word:
#      print(char)

# even_number = [i for i in range(0,10)if i % 2 == 0]
# print(even_number)

transactions = [100,100,300,400,150,80]
TAX_RATE = 0.08
SERVICE_CHARGE = 0.07

# def get_price_tax_service(bill):
#
#     return  bill*(1+ TAX_RATE + SERVICE_CHARGE)
#
# final_prices = [get_price_tax_service(bill) for bill in transactions]
# print(final_prices)

# Advanced Functions
#list() --> convert strings => List

# my_string = "welcome to codeXplore Chanel"
# list_of_chars = list(my_string)
# print((list_of_chars))              #ep kieu sang list r in ra

#sum()
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(sum(list_1))  #sum de tinh tong

#zip(): looping through two list simultaneously  (lap 2 list cung 1 luc)

# wizards = ['Harry Potter', 'Ron', 'Hermione']
# pets = ['Hedwig', 'Scabber', 'Crookshank']
# for index,(wiz,pet) in enumerate(zip(wizards,pets)):
#     print(f"{index + 1}.{wiz} has {pet}")

# sorted ()
# sorted_by_secon = sorted (['hi', 'hello', 'you', 'CodeXplore'],key = lambda el: el[1])
# print(sorted_by_secon)

# sorted_by_key = sorted([{'name': 'codeXplore','age': 15},
#         {'name': 'andy','age': 18},
#         {'name': 'zoey','age': 55}],key = lambda el: el['name'])
# print(sorted_by_key)


'''
5. 20 Array/List Matrix: Mång 2 Chiều
'''
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
# print(matrix[2][1])  #nhap toa do tim ra gia tri

# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col])
#Transform Matrix in List:
# list_converted = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
# print(list_converted) #converted thanh 1 list

# Combine columns with zip and *:
print([x for x in zip(*matrix)])