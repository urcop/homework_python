def show(func):
    def new_func(*args, **kwargs):
        print('Name of function - ', func.__name__)
        print('args - ', args)
        print('kwargs - ', kwargs)
    return new_func
