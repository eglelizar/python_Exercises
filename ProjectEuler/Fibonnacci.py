def fibonnacciDelimited (delimited):
    a = 1
    b = 1
    c = 0
    evenSum = 0
    while (c< delimited):
        c = a + b
        if (c % 2==0):
            evenSum += c
        a = b
        b = c
    return evenSum

def fibonnacci (num):
    if (num ==0 or num==1):
        return 1
    return fibonnacci (num -1 ) + fibonnacci *(num-2)

print(fibonnacciDelimited(4000000))