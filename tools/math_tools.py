from sympy import symbols, diff, integrate, solve, sympify

def calculate_derivative(expression_str: str, variable_str: str):
    x = symbols(variable_str)
    expr = sympify(expression_str)
    derivative = diff(expr, x)
    return str(derivative)

def calculate_integral(expression_str: str, variable_str: str):
    x = symbols(variable_str)
    expr = sympify(expression_str)
    integral = integrate(expr, x)
    return str(integral)

def solve_equation(equation_str: str, variable_str: str):
    x = symbols(variable_str)
    equation = sympify(equation_str)
    solution = solve(equation, x)
    return str(solution)
