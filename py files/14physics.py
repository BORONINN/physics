import numpy as np
import matplotlib.pyplot as plt


def calculate_refraction(E1, epsilon1, epsilon2, angle1):
    theta1 = np.radians(angle1)
    E2 = E1 * np.sqrt(epsilon1 / epsilon2)
    theta2 = np.arcsin(np.sqrt(epsilon1 / epsilon2) * np.sin(theta1))
    D1 = epsilon1 * E1
    D2 = epsilon2 * E2
    return E2, np.degrees(theta2), D1, D2


def plot_refraction():
    print('Введите')
    epsilon1 = float(input("диэлектрическую проницаемость первой среды -> epsilon1: "))
    epsilon2 = float(input("диэлектрическую проницаемость второй среды -> epsilon2: "))
    E1 = float(input("модуль напряженности в первой среде (E1): "))
    angle1 = float(input("угол падения в градусах: "))
    E2, angle2, D1, D2 = calculate_refraction(E1, epsilon1, epsilon2, angle1)

    fig, ax = plt.subplots(figsize=(8, 6))
    boundary_x = [-2, 2]
    boundary_y = [0, 0]

    x1 = -np.cos(np.radians(angle1))
    y1 = np.sin(np.radians(angle1))
    x2 = np.cos(np.radians(angle2))
    y2 = -np.sin(np.radians(angle2))

    scale_factor = 1.5

    for i in np.linspace(-2, 2, 10):
        ax.plot([i, i + x1 * E1 * scale_factor], [0, y1 * E1 * scale_factor], color='blue')
        ax.plot([i, i + x2 * E2 * scale_factor], [0, y2 * E2 * scale_factor], color='red')

    ax.plot(boundary_x, boundary_y, 'k--')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Преломление линий напряженности и смещения на границе диэлектриков')
    plt.grid()
    plt.show()

plot_refraction()


## pyinstaller --onefile lec14.py