import sympy as sp

def solve_differentiation():
    x = sp.symbols('x')
    
    # مثال لدالة: x^2 + 5x + 6
    function = x**2 + 5*x + 6
    
    # حساب المشتقة
    derivative = sp.diff(function, x)
    
    print(f"The function is: {function}")
    print(f"The derivative is: {derivative}")

if __name__ == "__main__":
    solve_differentiation()
