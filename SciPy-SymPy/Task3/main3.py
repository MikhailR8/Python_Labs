import sympy
from scipy.integrate import solve_ivp
import numpy
import matplotlib.pyplot as pyplot

# SymPy
x = sympy.Symbol('x')  # Объявляем символы и переменные
y = sympy.Function('y')
C1 = sympy.Symbol('C1')
equation = sympy.Eq(y(x).diff(x), -2 * y(x))  # Задаём уравнение и решаем его
solution = sympy.dsolve(equation)

eq1 = solution.rhs.subs(x, 0)  # задаём систему уравнений для констант из начальных условий и решаем её
equation_for_start_conditions = sympy.Eq(eq1, sympy.sqrt(2))
sol_for_const = sympy.solve(equation_for_start_conditions)[0]
rez = solution.rhs.subs(C1, sol_for_const)  # Подставляем в решение константу
f = sympy.lambdify(x, rez, 'numpy')  # Превращаем решение в функцию

# SciPy
def returns_dydx(x, y):
    dydx = -2 * y
    return dydx

sol = solve_ivp(returns_dydx, [0, 100], [numpy.sqrt(2)])  # Численно решаем диффур
xs = sol.t
ys = sol.y[0]

fig, axes = pyplot.subplots(1, 2, figsize=(10, 5), layout='constrained')
axes[0].plot(xs, f(xs), zorder=10, label='Аналитическое решение SymPy')
axes[0].plot(xs, ys, label='Численное решение SciPy')
axes[1].plot(xs, f(xs) - ys, label='Разность двух решений')
axes[0].legend()
axes[1].legend()
axes[0].grid()
axes[1].grid()

pyplot.savefig('Task3.jpg')
pyplot.show()
