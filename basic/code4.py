# code4.py
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, value):
        self.result += value

cal = Calculator()
cal.add(5)
print("Result:", cal.result)
