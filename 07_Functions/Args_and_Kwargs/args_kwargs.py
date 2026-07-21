"""
*args
"""
def sum_num(*args):
    total = 0
    for i in args:
        total += i
    print(total)
sum_num(1,2,3)

