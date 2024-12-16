import numpy as np
import matplotlib.pyplot as plt

# Параметры для потенциального поля
k_field = 1.0  # коэффициент потенциального поля

# Создаем сетку значений для x и y
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Вычисляем потенциальную энергию в каждом узле сетки
U = 0.5 * k_field * (X**2 + Y**2)

# Визуализация потенциального поля
plt.figure(figsize=(8, 6))
contour = plt.contourf(X, Y, U, levels=50, cmap="viridis")
plt.colorbar(contour, label="Потенциальная энергия U(x, y)")
plt.title("Потенциальное поле")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

## pyinstaller --onefile 567physics2.py


