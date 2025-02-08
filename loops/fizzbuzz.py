for number in range(1,101):
    flag =0
    if (number % 3 == 0):
        flag +=1
    if(number %5 ==0):
        flag +=2
    if(flag ==3):
        print ("FizzBuzz")
    elif(flag ==1):
        print("Fizz")
    elif(flag ==2):
        print("Buzz")
    elif(flag ==0):
        print(number)