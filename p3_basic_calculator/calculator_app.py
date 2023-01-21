# define the function needed: add, sub, mul, and div
# print option to the user
# ask for values
# call the function
# while loop to continue the program until the user want to exit


class Calculation:
    def __init__(self):
        pass

    def add(self, a, b):
        answer = a + b
        print(f"{str(a)} + {str(b)} = {answer}")

    def sub(self, a, b):
        answer = a - b
        print(f"{a} - {b} = {answer}")

    def mul(self, a, b):
        answer = a*b
        print(f"{a} x {b} = {answer}")

    def div(self, a, b):
        answer = a/b
        print(f"{a} / {b} = {answer}")


class Calculator:
    def __init__(self):
        self.cal = Calculation()
        pass

    def loop(self):
        want = input("Wanna do it again? (y/n) ")
        while want == "y" or want == "Y":
            self.main()

    def main(self):
        print("Calculator Program")
        print("--------------------")
        print("look: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multipication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            a = int(input("val1: "))
            b = int(input("val2: "))
            self.cal.add(a, b)
            self.loop()
        if choice == "2":
            a = int(input("val1: "))
            b = int(input("val2: "))
            self.cal.sub(a, b)
        if choice == "3":
            a = int(input("val1: "))
            b = int(input("val2: "))
            self.cal.mul(a, b)
        if choice == "3":
            a = int(input("val1: "))
            b = int(input("val2: "))
            self.cal.mul(a, b)
        if choice == "4":
            a = int(input("val1: "))
            b = int(input("val2: "))
            self.cal.div(a, b)
        if choice == "5":
            print("Bye")
            exit()


cal = Calculator()
cal.main()
