# Required Parameter & Default Parameter
# def print_name(name,greeting = "chao cac con vo"):
#     print(f'{name},{greeting}')
# Variable-length parameters (*args and **kwargs)
# If you mark a parameter with one asterisk (**),
# you can pass any number of positional arguments to your function (Typically called *prgs)


# def codexplore(a,b,c):
#     print(a,b,c)
def variblelengthArgExampler(a,b,*args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key,value)
def main():
    # Positional Arguments
    # codexplore(3,4,5)
    # print_name("thang quang loiii","tam biet cac con vo")

    # Keyword arguments
    # codexplore(a = "xin chao",c = "con vo",b = "cac")

    #*args:
    # variblelengthArgExampler('a','b', 1,2,4,5,3)
    # **kwargs:
    variblelengthArgExampler('a',2,'hello word',1,size= "upsize",age= "NG")
    pass
if __name__ == "__main__":
    main()