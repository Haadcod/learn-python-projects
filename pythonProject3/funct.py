def  is_called():
    def is_returned():
        print('hello')
    return is_returned()
new=is_called()
new()