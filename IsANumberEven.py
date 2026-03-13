class NumberAnalysis:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        self.num = data

    # a method
    def read_number(self):
        print(self.num)

    def isEven(self):
        print(self.num % 2 == 0)


# creating object of the class
# this will invoke parameterized constructor
obj = NumberAnalysis(55)

# calling the instance method using the object obj
obj.read_number()
obj.isEven()

# creating another object of the class
obj2 = NumberAnalysis(66)
obj2.read_number()
obj2.isEven()

# calling the instance