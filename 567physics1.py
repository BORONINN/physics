import numpy as np
import matplotlib.pyplot as plt

# Параметры задачи
g = 9.81  # ускорение свободного падения, м/с^2
m = 1.0  # масса тела, кг (можно условно принять за 1 кг)
k = 0.1  # коэффициент сопротивления
v0 = 50  # начальная скорость, м/с
angle = 45  # угол броска в градусах
h0 = 0  # начальная высота, м

# Преобразуем угол в радианы
theta = np.radians(angle)

# Начальные условия
vx0 = v0 * np.cos(theta)
vy0 = v0 * np.sin(theta)
x0, y0 = 0, h0  # начальные координаты

# Время моделирования
dt = 0.01  # шаг по времени
t_max = 10  # максимальное время моделирования

# Списки для хранения значений
x, y = [x0], [y0]
vx, vy = [vx0], [vy0]
time = [0]

# Численное решение с использованием метода Эйлера
while y[-1] >= 0:
    # Текущее время
    t = time[-1] + dt

    # Текущие значения скоростей и координат
    vx_current = vx[-1]
    vy_current = vy[-1]
    x_current = x[-1]
    y_current = y[-1]

    # Вычисляем силы сопротивления
    Fx = -k * vx_current
    Fy = -m * g - k * vy_current

    # Обновляем ускорения
    ax = Fx / m
    ay = Fy / m

    # Обновляем скорости
    vx_new = vx_current + ax * dt
    vy_new = vy_current + ay * dt

    # Обновляем координаты
    x_new = x_current + vx_current * dt
    y_new = y_current + vy_current * dt

    # Записываем новые значения в списки
    vx.append(vx_new)
    vy.append(vy_new)
    x.append(x_new)
    y.append(y_new)
    time.append(t)

# Построение графиков
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

# Траектория движения
axs[0].plot(x, y)
axs[0].set_title("Траектория движения тела")
axs[0].set_xlabel("x (м)")
axs[0].set_ylabel("y (м)")

# Скорость от времени
axs[1].plot(time, [np.sqrt(vx[i] ** 2 + vy[i] ** 2) for i in range(len(time))])
axs[1].set_title("Скорость тела от времени")
axs[1].set_xlabel("Время (с)")
axs[1].set_ylabel("Скорость (м/с)")

# Координаты от времени
axs[2].plot(time, x, label="x (м)")
axs[2].plot(time, y, label="y (м)")
axs[2].set_title("Координаты тела от времени")
axs[2].set_xlabel("Время (с)")
axs[2].set_ylabel("Координаты (м)")
axs[2].legend()

plt.tight_layout()
plt.show()


## pyinstaller --onefile 567physics1.py