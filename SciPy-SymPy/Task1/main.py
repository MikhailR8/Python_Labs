from sympy.matrices import Matrix, zeros
from sympy import Symbol

M = zeros(9)
M[0, 3] = Symbol(r'-\frac{1}{\rho}')
M[1, 4] = Symbol(r'-\frac{1}{\rho}')
M[2, 5] = Symbol(r'-\frac{1}{\rho}')
M[3, 0] = Symbol(r'-(\lambda + 2\mu)')
M[4, 1] = Symbol(r'-\mu')
M[5, 2] = Symbol(r'-\mu')
M[6, 0] = Symbol(r'-\lambda')
M[8, 0] = Symbol(r'-\lambda')
eigen = M.eigenvals()
for key, value in eigen.items():
    print(f'Собственное значение {key} кратности {value}')
