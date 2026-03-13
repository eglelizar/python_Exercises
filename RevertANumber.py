
#123
# module 3
# result 3 * 10 + reverse(12)
#  result 2 * 10 +  reverse(1)
# 1
def reverse (num):
    revertedNum = 0
    signed = 1
    if (num < 0):
        signed = -1
    num = abs(num)
    while (num > 0):
        mod = num % 10
        revertedNum= revertedNum *10 + mod
        num = num //10
    
    limit = pow (2, 31)
    if revertedNum > limit -1 or revertedNum < -limit:
        return 0
    return revertedNum * signed

print(reverse(1534236469))