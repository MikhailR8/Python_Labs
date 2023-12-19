from scipy.integrate import solve_ivp
import numpy

# A, B, C = map(int, input().split())
A, B, C = 9, 6, 3

def euler_dynamics(t, y):
    return [(B - C)/A * y[1] * y[2],
            (C - A)/B * y[0] * y[2],
            (A - B)/C * y[0] * y[1]]

def find_omega(p0, q0, r0, t):
    sol = solve_ivp(euler_dynamics, [0, t], [p0, q0, r0])
    return sol.y[:, -1]

# print(find_omega(2, 1, 1, 10))