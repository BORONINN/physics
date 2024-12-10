import numpy as np
import matplotlib.pyplot as plt

# Определение параметров зарядов
charges = [
    {"pos": np.array([2, -1]), "q": 1},  # Заряд +1 в точке (2, -1)
    {"pos": np.array([-2, -1]), "q": -1}, # Заряд -1 в точке (-2, -1)
    {"pos": np.array([2, 1]), "q": 1},
    {"pos": np.array([-2, 1]), "q": -1}
]

# Определение сетки для вычисления поля
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)  # Создание сетки

# Инициализация потенциала и векторов электрического поля
V = np.zeros_like(X)
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)

# Построение электростатического поля и потенциала
for charge in charges:
    # Координаты заряда
    cx, cy = charge["pos"]
    q = charge["q"]

    # Расчет векторов расстояний
    dx = X - cx
    dy = Y - cy
    r_squared = dx ** 2 + dy ** 2  # Квадрат расстояния
    r = np.sqrt(r_squared)  # Расстояние

    # Избегаем деления на ноль
    r[r == 0] = 1e-9

    # Вклад в электрическое поле от этого заряда
    Ex += q * dx / r_squared
    Ey += q * dy / r_squared

    # Вклад в потенциал от этого заряда
    V += q / r

# Модуль поля и его нелинейное преобразование для цветовой карты
E_magnitude = np.sqrt(Ex ** 2 + Ey ** 2)
E_magnitude_normalized = E_magnitude ** 0.3  # Усиление изменений вблизи зарядов

# Нормализация векторов электрического поля
Ex /= E_magnitude
Ey /= E_magnitude

# Построение графика
plt.figure(figsize=(10, 8))

# Линии напряженности
plt.streamplot(
    X, Y, Ex, Ey, color=E_magnitude_normalized,
    cmap='plasma', linewidth=1.5, density=2
)

# Эквипотенциальные линии
contour = plt.contour(X, Y, V, levels=200, colors='red', linewidths=0.8)
plt.clabel(contour, inline=True, fontsize=8, fmt="%.1f")

# Заряды
for charge in charges:
    plt.scatter(*charge["pos"], color="red" if charge["q"] > 0 else "blue", s=100)

plt.title("Электростатическое поле и эквипотенциальные линии")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.colorbar(label="Напряженность поля")
plt.grid(True)
plt.show()
