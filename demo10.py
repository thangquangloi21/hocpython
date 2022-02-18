#for

# my_list = [1,2,3]
# my_list = {'a': 1,'b': 2,'c': 3}
# for num,value in my_list.items():
#     print(num,value)

'''
pop.py
while <condition that evaluates to boolean>:
     # action
   if <condition ,that evaluates to boolean>:
        break # break out of while loop
    if <condition that evaluates to boolean>:
        continue #continue to the next line in the block
'''

msg = ''
while msg != 'quit':
    msg = input("Please give me an input:")
    print(msg)