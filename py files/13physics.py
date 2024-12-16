import numpy as np
import matplotlib.pyplot as plt

charges = [
    {"pos": np.array([2, -1]), "q": 1},  # Заряд +1 в точке (2, -1)
    {"pos": np.array([-2, -1]), "q": -1},  # Заряд -1 в точке (-2, -1)
    {"pos": np.array([2, 1]), "q": 1},
    {"pos": np.array([-2, 1]), "q": -1}
]

define_dipole = lambda position, magnitude, angle_deg: {
    "position": np.array(position),
    "p_vector": magnitude * np.array([
        np.cos(np.radians(angle_deg)),
        np.sin(np.radians(angle_deg))
    ])
}

dipole = define_dipole([0, 0], 2.0, 70)

x = np.linspace(-5, 5, 200)
y = np.linspace(-5, 5, 200)
X, Y = np.meshgrid(x, y)

V = np.zeros_like(X)
Ex = np.zeros_like(X)
Ey = np.zeros_like(Y)

for charge in charges:
    cx, cy = charge["pos"]
    q = charge["q"]

    dx = X - cx
    dy = Y - cy
    r_squared = dx**2 + dy**2
    r = np.sqrt(r_squared)

    r[r == 0] = 1e-9
    Ex += q * dx / r_squared
    Ey += q * dy / r_squared

    V += q / r

px, py = dipole["p_vector"]
cx, cy = dipole["position"]
r_squared_dipole = (X - cx)**2 + (Y - cy)**2
r_dipole = np.sqrt(r_squared_dipole)

r_dipole[r_dipole == 0] = 1e-9

Ex_dipole = (1 / r_squared_dipole**1.5) * (
    3 * (px * (X - cx) + py * (Y - cy)) * (X - cx) - px * r_squared_dipole
)
Ey_dipole = (1 / r_squared_dipole**1.5) * (
    3 * (px * (X - cx) + py * (Y - cy)) * (Y - cy) - py * r_squared_dipole
)

V_dipole = (px * (X - cx) + py * (Y - cy)) / r_squared_dipole**1.5

Ex += Ex_dipole
Ey += Ey_dipole
V += V_dipole

E_magnitude = np.sqrt(Ex**2 + Ey**2)
E_magnitude_normalized = E_magnitude**0.3

Ex_normalized = Ex / E_magnitude
Ey_normalized = Ey / E_magnitude

r_dipole_at_pos = dipole["position"] - dipole["position"]
r_squared_dipole_at_pos = np.sum(r_dipole_at_pos**2)
r_squared_dipole_at_pos = max(r_squared_dipole_at_pos, 1e-9)

Ex_at_dipole = (1 / r_squared_dipole_at_pos**1.5) * (
    3 * (px * r_dipole_at_pos[0] + py * r_dipole_at_pos[1]) * r_dipole_at_pos[0] - px * r_squared_dipole_at_pos
)
Ey_at_dipole = (1 / r_squared_dipole_at_pos**1.5) * (
    3 * (px * r_dipole_at_pos[0] + py * r_dipole_at_pos[1]) * r_dipole_at_pos[1] - py * r_squared_dipole_at_pos
)

E_at_dipole = np.array([Ex_at_dipole, Ey_at_dipole])

Force_on_dipole = dipole["p_vector"] * E_at_dipole
Force_magnitude = np.linalg.norm(Force_on_dipole)
Force_direction = Force_on_dipole / Force_magnitude if Force_magnitude != 0 else np.array([0, 0])
Moment_dipole = px * Ey_at_dipole - py * Ex_at_dipole

plt.figure(figsize=(10, 8))
plt.streamplot(
    X, Y, Ex_normalized, Ey_normalized, color=E_magnitude_normalized, cmap="plasma", linewidth=1.5, density=2
)
contour = plt.contour(X, Y, V, levels=200, colors="red", linewidths=0.8)
plt.clabel(contour, inline=True, fontsize=8, fmt="%.1f")

for charge in charges:
    plt.scatter(*charge["pos"], color="red" if charge["q"] > 0 else "blue", s=100)

plt.quiver(
    *dipole["position"], *dipole["p_vector"], angles="xy", scale_units="xy", scale=1, color="green", label="Диполь"
)

plt.title("Электростатическое поле и эквипотенциальные линии с учетом диполя")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.colorbar(label="Напряженность поля")
plt.grid(True)
plt.legend()
plt.show()

print(f"Модуль поля в месте диполя: {np.sqrt(E_at_dipole[0]**2 + E_at_dipole[1]**2)}")
print(f"Сила, действующая на диполь: {Force_on_dipole}")
print(f"Модуль силы, действующей на диполь: {Force_magnitude}")
print(f"Направление силы, действующей на диполь: {Force_direction}")
print(f"Момент силы, действующий на диполь: {Moment_dipole}")

