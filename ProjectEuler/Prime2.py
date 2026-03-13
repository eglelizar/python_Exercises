def isPrime(c):
    return (c == '2' or c == '3' or
            c == '5' or c == '7')
  
# replace with previous prime character
def decrease(s, i):
      
    # if 2 eras[i] and replace next with 7
    if (s[i] <= '2'):
          
        # s.erase(i, 1);
        s[i] = '7'
    elif (s[i] == '3'):
        s[i] = '2'
    elif (s[i] <= '5'):
        s[i] = '3'
    elif (s[i] <= '7'):
        s[i] = '5'
    else:
        s[i] = '7'
  
def primeDigits(s):
    s = [i for i in s]
    i = 0
  
    while i < len(s):
  
        # find first non prime char
        if (isPrime(s[i]) == False):
  
            # find first char greater than 2
            while (s[i] <= '2' and i >= 0):
                i -= 1
  
            # like 20
            if (i < 0):
                i = 0
                decrease(s, i)
          
            # like 7721
            else:
                decrease(s, i)
  
            # replace remaining with 7
            for j in range(i + 1,len(s)):
                s[j] = '7'
  
            break
        i += 1
  
    return "".join(s)

print(primeDigits("13195"))