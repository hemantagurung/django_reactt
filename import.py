def my_deco(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper      
