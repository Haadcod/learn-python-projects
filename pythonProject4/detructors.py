class Employee:
    def __init__(self):
        print('Employee is created')
    def __del__(self):
        print('The employee object is deleted')
def create_obj():
    print('we are creating the obj')
    obj=Employee()
    print('we are ending the obj')
    return obj
print('calling the obj function.....')
obj=create_obj()
print('program end....')
