class Addition:
    first=0
    second=0
    answer=0
    def __init__(self,f,s):
        self.first=f
        self.second=s
    def dispaly(self):
        print('first number is =',self.first)
        print('second number is =',self.second)
        print('Addition of two numbers =',self.answer)
    def claculate(self):
        self.answer=self.first + self.second
obj=Addition(1000,3000)
obj.claculate()
obj.dispaly()