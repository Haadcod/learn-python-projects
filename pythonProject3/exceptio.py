class MuffledCalculator:
    muffle=False
    def calc(self,expr):
        try:
           return eval(expr)
        except ZeroDivisionError:
            if self.muffle:
                print('the value cant be zero')
            else:
                raise
cal=MuffledCalculator()
cal.calc('2/7')