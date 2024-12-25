import numpy as np


def solve_circuit(resistances, emfs, connections):
    num_nodes = max(max(conn) for conn in connections) + 1
    num_resistors = len(resistances)

    A = np.zeros((num_nodes, num_nodes))
    b = np.zeros(num_nodes)

    print("Шаг 1: Формирование матрицы системы...")
    for idx, (node1, node2) in enumerate(connections):
        conductance = 1 / resistances[idx]
        A[node1, node1] += conductance
        A[node2, node2] += conductance
        A[node1, node2] -= conductance
        A[node2, node1] -= conductance

    for idx, emf in enumerate(emfs):
        node1, node2 = connections[idx]
        b[node1] += emf
        b[node2] -= emf

    A = A[:-1, :-1]
    b = b[:-1]

    print("Матрица коэффициентов A:")
    print(A)
    print("Вектор правых частей b:")
    print(b)

    # Решение системы уравнений
    print("\nШаг 2: Решение системы уравнений...")
    voltages = np.linalg.solve(A, b)
    voltages = np.append(voltages, 0)

    print("Напряжения на узлах:")
    print(voltages)

    # Рассчитываем токи через резисторы
    print("\nШаг 3: Расчет токов через резисторы...")
    currents = []
    for idx, (node1, node2) in enumerate(connections):
        current = (voltages[node1] - voltages[node2]) / resistances[idx]
        currents.append(current)

    # Вывод результатов
    print("\nРезультаты:")
    for idx, current in enumerate(currents):
        print(f"Ток через резистор R{idx + 1}: {current:.2f} А")

    return currents

resistances = [10, 20, 30]
emfs = [5, 10]
connections = [
    (0, 1),
    (1, 2),
    (2, 0)
]

currents = solve_circuit(resistances, emfs, connections)


## pyinstaller --onefile 15lec.py
