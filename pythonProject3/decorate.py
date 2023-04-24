def make_pretty(func):
    def inner():
        print('I got decorated')
    return inner
def ordinary():
    print('I am ordinary')
ordinary()
pretty=make_pretty(ordinary)
pretty()