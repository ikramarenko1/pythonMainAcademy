from local_module import local_function as say_local


def global_function():
    print('Це функція з global_function.')


say_local()
global_function()

