class NumberAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers
    def analyze(self):
        for num in self.numbers:
            if num % 2 == 0:
                yield num, "Even"
            else:
                yield num, "Odd"
obj = NumberAnalyzer([10, 15, 20, 25])
for result in obj.analyze():
    print(result)