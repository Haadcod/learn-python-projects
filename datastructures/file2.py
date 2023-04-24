#python module to import
print('file two name is set to:{}'.format(__name__))
def function_3():
    print('function three is executed')
if __name__=="__main__":
    print('file 2 executed wen run directly')
else:
    print('file2 executed when imported')
