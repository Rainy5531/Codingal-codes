class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        result = eval(self.expression)
        print(f"Result: {result}")

if __name__ == "__main__":
    expression = input("Enter a mathematical expression: ")
    solver = ExpressionSolver(expression)
    solver.solve()