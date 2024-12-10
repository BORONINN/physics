import numpy as np
import matplotlib.pyplot as plt

# Определение параметров зарядов
charges = [
    {"pos": np.array([1, 0]), "q": 1},  # Заряд +1 в точке (2, 2)
    {"pos": np.array([-1, 0]), "q": -1}  # Заряд -1 в точке (-2, -2)
]

# Определение сетки для вычисления поля
x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)  # Создание сетки

# Инициализация векторов электрического поля
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)

# Построение электростатического поля
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
    r_squared[r_squared == 0] = 1e-9

    # Вклад в электрическое поле от этого заряда
    Ex += q * dx / r_squared
    Ey += q * dy / r_squared

# Модуль поля и его нелинейное преобразование для цветовой карты
E_magnitude = np.sqrt(Ex ** 2 + Ey ** 2)
E_magnitude_normalized = E_magnitude ** 0.3  # Усиление изменений вблизи зарядов

# Нормализация векторов электрического поля
Ex /= E_magnitude
Ey /= E_magnitude

# Построение графика
plt.figure(figsize=(8, 6))
plt.streamplot(
    X, Y, Ex, Ey, color=E_magnitude_normalized,
    cmap='plasma', linewidth=1.5, density=2
)
plt.colorbar(label="напряженность поля")
for charge in charges:
    plt.scatter(*charge["pos"], color="red" if charge["q"] > 0 else "blue", s=100)
plt.title("Электростатическое поле системы зарядов")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.show()


## pyinstaller --onefile hw10.py