class Infiter:
    """infinte iterator to return all odd numbers"""
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        num=self.num
        self.num+=2
        return num
a=iter(Infiter())
next(a)
next(a)
next(a)
next(a)