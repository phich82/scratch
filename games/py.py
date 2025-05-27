from sympy import factor, symbols, solve, sympify
def find_zeroes(polynomial_string):
    J = symbols('J')
    f = sympify(polynomial_string)
    roots = solve(f, J)
    print(roots)

find_zeroes("(J**4) + (7*J**3) + (-765*J**2) + (3609*J**1) + (17820*J**0)")