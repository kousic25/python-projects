class Numbers:
    def add(self, *args):
        print("Sum =", sum(args))
n1 = Numbers()
n1.add(10, 20, 30, 40)