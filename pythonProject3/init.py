class ComplexNumber:
    def __init__(self, r=0,j=1):
        self.real=r
        self.image=j
    def get_data(self):
        print(f'{self.image}+{self.real}')
num1=ComplexNumber(2,4)
num1.get_data()
num2=ComplexNumber(5)
num2.get_data()
num2.attr(10)
print(num2.real,num2.image,num2.attr)
print(num1.attr)