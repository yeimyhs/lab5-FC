import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def solve_continuity_equation(L, T, N, M):
    dx = L / N
    dt = T / M

    u = np.zeros((M+1, N+1))
    u[0, :] = 0.0

    for i in range(1, M+1):
        for j in range(1, N):
            u[i, j] = u[i-1, j] - dt * (u[i-1, j] - u[i-1, j-1]) / dx

    return u

def plot_solution(u, L, T):
    N, M = u.shape

    x = np.linspace(0, L, N)
    t = np.linspace(0, T, M)
    X, T = np.meshgrid(x, t)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='viridis')

    ax.set_xlabel('Posición')
    ax.set_ylabel('Tiempo')
    ax.set_zlabel('Velocidad')
    plt.show()

# Obtener datos del usuario
'''L = float(input("Ingrese la longitud del conducto: "))
T = float(input("Ingrese el tiempo total: "))
N = int(input("Ingrese el número de puntos espaciales: "))
M = int(input("Ingrese el número de puntos temporales: "))'''
L = 1.0
T = 0.1
N = 100
M = 500

# Resolver la ecuación de continuidad
solution = solve_continuity_equation(L, T, N, M)

# Graficar la solución
plot_solution(solution, L, T)
