import matplotlib.pyplot as plt
import numpy
import numpy as np
from quaternion import *
from matplotlib import cm
import matplotlib.animation as animation

fig = plt.figure(figsize=plt.figaspect(1))  # Square figure
ax = fig.add_subplot(111, projection='3d')

coefs = (9, 6, 3)  # Coefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1
# Radii corresponding to the coefficients:
rx, ry, rz = 1/np.sqrt(coefs)

# Set of all spherical angles:
n = 50
u = np.linspace(0, 2 * np.pi, n)
v = np.linspace(-np.pi / 2, np.pi / 2, n)

# Cartesian coordinates that correspond to the spherical angles:
# (this is the equation of an ellipsoid):
x = rx * np.outer(np.cos(u), np.cos(v))
y = ry * np.outer(np.sin(u), np.cos(v))
z = rz * np.outer(np.ones_like(u), np.sin(v))

x_copy = np.copy(x)
y_copy = np.copy(y)
z_copy = np.copy(z)

quat_0 = Quaternion(0.5, numpy.array([1, 1, 1]))
quat_0.normalize()
quat_0_con = quat_0.conjugate()
A, B, C = coefs
p0 = 0.05
q0 = 0.03
r0 = 0.01
K_abs = np.array([A * p0, B * q0, C * r0])

# quat_1 = Quaternion(0, np.array([1, 0, 0]))
# quat_out = quat_0 >> quat_1 >> quat_0_con
# S_1 = quat_out.get_axis()
# quat_2 = Quaternion(0, np.array([0, 1, 0]))
# quat_out = quat_0 >> quat_2 >> quat_0_con
# S_2 = quat_out.get_axis()
# quat_3 = Quaternion(0, np.array([0, 0, 1]))
# quat_out = quat_0 >> quat_3 >> quat_0_con
# S_3 = quat_out.get_axis()
# S = numpy.concatenate(([S_1], [S_2], [S_3]), axis=0)

# K_abs = np.matmul(S.T, K_relative)
# d = np.sqrt(A * (p0 ** 2) + B * (q0 ** 2) + C * (r0 ** 2)) / np.sqrt(np.dot(K_abs, K_abs))
# print(K_abs)
# x_to_plate = np.linspace(-0.4, 0.4, 20)
# y_to_plate = np.linspace(-0.4, 0.4, 20)
# X, Y = np.meshgrid(x_to_plate, y_to_plate)
# a = K_abs[0]
# b = K_abs[1]
# c = K_abs[2]
# print(a, b, c, d)
# Z = (d - a * X - b * Y)/c

frames = 150

# Generate each frame
for k in range(0, frames):
    quat_p = integrate_quaternion_t(quat_0, k)
    # print(quat_p)
    quat_p_con = quat_p.conjugate()
    for i in range(n):
        for j in range(n):
            quat_l = Quaternion(0, np.array([x[i][j], y[i][j], z[i][j]]))
            quat_out = quat_p >> quat_l >> quat_p_con
            x_copy[i][j], y_copy[i][j], z_copy[i][j] = quat_out.get_axis()

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x_copy, y_copy, z_copy, cmap=cm.coolwarm)
    # ax.plot_surface(X, Y, Z)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    plt.savefig(f"{k}.png")
    plt.close()


# Use pillow to save all frames as an animation in a gif file
from PIL import Image

images = [Image.open(f"{n}.png") for n in range(frames)]

images[0].save('ball.gif', save_all=True, append_images=images[1:], duration=100, loop=0)
