def IsThisPrime (num):
    if num %2 ==0:
        return False
    for i in range(2, num//2+1):
        if (num% i == 0):
            return False
    return True

def getLargest(num):
    if (num == 0):
        return 0
    if (IsThisPrime(num)):
        return num
    return getLargest(num -1)

print(getLargest(13195))