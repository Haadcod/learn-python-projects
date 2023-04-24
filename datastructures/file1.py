#python module to execute
import file2
print('file_one name is set to:{}'.format(__name__))
def function():
    print('function one i executed')
def function2():
    print('function two is executed')
if __name___=='__main__':
    print('file1 executed when run directly')
else:
    print('file one executed when imported')
