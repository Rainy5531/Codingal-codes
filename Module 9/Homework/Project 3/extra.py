class operation:
    def __init__(self, num):
        self.num = num

    def add(self):
        total = 0
        for digit in str(self.num):
            total += int(digit)
        return "The sum of the digits of {} is {}".format(self.num, total)

num = int(input("Enter number: "))
op = operation(num)

print(op.add())