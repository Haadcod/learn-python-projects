class Bmw:
    def __init__(self):
        self.mode=['i8','x7','x5','x3']
    def outmodel(self):
        print('The output for bmw series')
        for models in self.mode:
            print('\t %s'%models)
