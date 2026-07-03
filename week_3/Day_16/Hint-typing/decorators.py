def fence(func):

    def wrapper():
        print("Fence initialized.")
        func()
        print("Fence completed.")
    return wrapper

@fence
def my_function():
    print("decorated!!!")

my_function()