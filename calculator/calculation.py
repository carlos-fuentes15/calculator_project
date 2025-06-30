class Calculation:
    def __init__(self, a: float, b: float, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        return self.operation(self.a, self.b)

    def __str__(self):
        op_symbol = {
            'add': '+',
            'subtract': '-',
            'multiply': '*',
            'divide': '/'
        }.get(self.operation.__name__, '?')
        return f"{self.a} {op_symbol} {self.b} = {self.perform()}"

    @staticmethod
    def create(a, b, operation):
        return Calculation(a, b, operation)
