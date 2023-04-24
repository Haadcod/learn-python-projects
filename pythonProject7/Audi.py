class Audi:
    def __init__(self):
        self.mode=['q7','a8','a5','a3']
    def outmodel(self):
        print('Thes are the Audi car series')
        for models in self.mode:
            print('\t %s'%models)
