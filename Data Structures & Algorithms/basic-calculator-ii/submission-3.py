class Solution:
    def calculate(self, s: str) -> int:
        operator, index = None, 0
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                operator = s[i]
                index = i
            elif operator not in ['+', '-'] and (s[i] == '*' or s[i] == '/'):
                operator = s[i]
                index = i
        print(s)
        
        if operator == '+':
            return self.calculate(s[:index]) + self.calculate(s[index+1:])
        elif operator == '-':
            return self.calculate(s[:index]) - self.calculate(s[index+1:])
        elif operator == '*':
            return self.calculate(s[:index]) * self.calculate(s[index+1:])
        elif operator == '/':
            return self.calculate(s[:index]) // self.calculate(s[index+1:])
        else:
            return int(s)

