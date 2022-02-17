'''
Project: Random Password
'''
import string
import  random

LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTUATION = string.punctuation

#print(PUNCTUATION)
def password_generator(length=8):
    printable = f'{LETTER} {NUMBER}{PUNCTUATION}'
    printable = list(printable)
    random.shuffle(printable)
    randon_password = random.choices(printable, k=length)
    randon_password = ''.join(randon_password)
    return randon_password
def get_password_length():
    password_length = input("How long do you want your password: ")
    return int(password_length)
def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)

if __name__ == '__main__':
    main()