import numpy
from scipy.integrate import solve_ivp
import omega_integrator

class Quaternion:  # a + ib + jc + kd
    def __init__(self, scalar, vector):
        self.scalar = float(scalar)
        self.vector = vector.astype(float)

    def __rshift__(self, other):
        new_scalar = self.scalar * other.scalar - numpy.dot(self.vector, other.vector)
        new_vector = self.scalar * other.vector + \
                 other.scalar * self.vector + numpy.cross(self.vector, other.vector)
        return Quaternion(new_scalar, new_vector)

    def __str__(self):
        return numpy.array2string(self.to_numpy(), precision=2, separator=' ')

    def get_axis(self):
        return self.vector

    def get_angle(self):
        return 2 * numpy.arccos(self.scalar)

    def get_norm(self):
        return numpy.sqrt(self.scalar ** 2 + numpy.dot(self.vector, self.vector))

    def normalize(self):
        norm = numpy.sqrt(self.scalar ** 2 + numpy.dot(self.vector, self.vector))
        self.scalar /= norm
        self.vector /= norm

    def to_numpy(self):
        return numpy.concatenate((self.scalar, self.vector), axis=None)

    def conjugate(self):
        new_scalar = self.scalar
        new_vector = -self.vector
        return Quaternion(new_scalar, new_vector)

quat_0 = Quaternion(0.5, numpy.sqrt(3) / 2 * numpy.array([0, 1, 0]))
quat_0.normalize()
print(quat_0)
p0 = 0.05
q0 = 0.03
r0 = 0.01

def poisson_equation(t, y):
    quat_omega_t = Quaternion(0, omega_integrator.find_omega(p0, q0, r0, t))
    return 0.5 * (Quaternion(y[0], y[1:]) >> quat_omega_t).to_numpy()

def integrate_quaternion_t(quat0, t):
    sol = solve_ivp(poisson_equation, [0, t], quat0.to_numpy())
    return Quaternion(sol.y[:, -1][0], sol.y[:, -1][1:])


print(integrate_quaternion_t(quat_0, 2))
