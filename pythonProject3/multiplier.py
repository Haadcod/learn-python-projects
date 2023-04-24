def multiplier_of_number(n):
    def multiplier(x):
        return x*n
    return multiplier
times=multiplier_of_number(3)
times=multiplier_of_number(5)
print(times(9))
print(times(10))
