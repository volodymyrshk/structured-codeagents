from tools.math_tools import calculate_derivative, calculate_integral, solve_equation

def test_calculate_derivative():
    assert calculate_derivative("x**2", "x") == "2*x"

def test_calculate_integral():
    assert calculate_integral("sin(x)", "x") == "-cos(x)"

def test_solve_equation():
    assert solve_equation("x**2 - 4", "x") == "[-2, 2]"
