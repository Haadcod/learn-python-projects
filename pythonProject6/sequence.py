def check_index(key):
    """Is the given key an acceptable index?
    Tobe acceptable, the key has tobe a non negative integer. if it is
    not an integer, a TypeError is raised: If it is a  negative, an indexError is raised (since the sequence is of infinite length) """
    if not isinstance(key,int):
        raise TypeError
    if key<0:
        raise TypeError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        """initialise the arithmetic sequence
        start _ The first value in a sequence
        step _ The difference between two adjacent values
        changed _ The dictionary value that has been modified by the user"""
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self, key):
        """Get item from the arithmetic sequence"""
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key *self.step
    def __setitem__(self, key, value):
        """change item in th arithmetic sequence"""
        check_index(key)
        self.changed[key]=value
s=ArithmeticSequence(1,2)
print(s.__getitem__(4))