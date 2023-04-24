class Audi:
    def __init__(self):
        self.mode=['b3','b5','r5','y6']
    def outmodel(self):
        print('The out pot for audi series is:')
        for models in self.mode:
            print('\t %s'%models)