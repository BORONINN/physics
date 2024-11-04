import numpy as np
import matplotlib.pyplot as plt

# Входные данные
m = 1 # Масса груза (кг)
k = 10 # Коэффициент жесткости пружины (Н/м)
b = 0.2 # Коэффициент сопротивления среды (Н/(м/с))

# Начальные условия
x0 = 0.1 # Начальное смещение (м)
v0 = 0 # Начальная скорость (м/с)

# Время моделирования
t_max = 15 # Максимальное время (с)
dt = 0.01 # Шаг по времени (с)
t = np.arange(0, t_max, dt)

# Решение дифференциального уравнения движения
def f(x, v):
  return v, -(k * x + b * v) / m

# Метод Рунге-Кутты четвертого порядка
def rk4(f, x0, v0, t):
  x = np.zeros_like(t)
  v = np.zeros_like(t)
  x[0] = x0
  v[0] = v0
  for i in range(len(t) - 1):
    k1x, k1v = f(x[i], v[i])
    k2x, k2v = f(x[i] + dt / 2 * k1x, v[i] + dt / 2 * k1v)
    k3x, k3v = f(x[i] + dt / 2 * k2x, v[i] + dt / 2 * k2v)
    k4x, k4v = f(x[i] + dt * k3x, v[i] + dt * k3v)
    x[i + 1] = x[i] + dt / 6 * (k1x + 2 * k2x + 2 * k3x + k4x)
    v[i + 1] = v[i] + dt / 6 * (k1v + 2 * k2v + 2 * k3v + k4v)
  return x, v

# Решение дифференциального уравнения
x, v = rk4(f, x0, v0, t)

# Расчет энергии
kinetic_energy = 0.5 * m * v**2
potential_energy = 0.5 * k * x**2
total_energy = kinetic_energy + potential_energy

# Построение графиков
plt.figure(figsize=(10, 6))
plt.plot(t, kinetic_energy, label='Кинетическая энергия', color='red')
plt.plot(t, potential_energy, label='Потенциальная энергия', color='blue')
plt.plot(t, total_energy, label='Полная механическая энергия', color='black')
plt.xlabel('Время (с)')
plt.ylabel('Энергия (Дж)')
plt.title('Энергетические превращения при колебании груза на пружине')
plt.legend()
plt.grid(True)
plt.show()


## pyinstaller --onefile physics8.py