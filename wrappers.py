def logger(func):
    def wrapper():  
        print("function started")
        func()
        print("function ended")
    return wrapper

@logger
def say_hi():
    print("hi")

@logger
def say_bye():
    print("bye")

say_hi()
say_bye()