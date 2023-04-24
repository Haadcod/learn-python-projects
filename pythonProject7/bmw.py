class Bmw:
    def __init__(self):
        self.mode=['i8','x1','x5','x6']
    def outmodel(self):
        print('These are the Bmw series')
        for models in self.mode:
            print('\t %s'%models)
