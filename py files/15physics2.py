def calculate_capacitor_parameters(voltage, distance, dielectric, area=1, connected=True):

    epsilon_0 = 8.854e-12
    capacitance = epsilon_0 * dielectric * area / distance

    charge = capacitance * voltage

    field_strength = voltage / distance

    results = {
        "Емкость (Ф)": capacitance,
        "Заряд (Кл)": charge,
        "Напряжённость поля (В/м)": field_strength,
    }

    if not connected:
        new_voltage = charge / capacitance
        results["Новое напряжение (В)"] = new_voltage

    return results


if __name__ == "__main__":
    print("Введите параметры плоского конденсатора:")
    voltage = float(input("Напряжение между пластинами (В): "))
    distance = float(input("Расстояние между пластинами (м): "))
    dielectric = float(input("Относительная диэлектрическая проницаемость: "))
    area = float(input("Площадь пластин (м², по умолчанию 1): ") or 1)
    connected_input = input("Конденсатор подключен к источнику питания? (да/нет): ").strip().lower()
    connected = connected_input == "да"

    parameters = calculate_capacitor_parameters(voltage, distance, dielectric, area, connected)

    print("\nРезультаты расчёта:")
    for param, value in parameters.items():
        print(f"{param}: {value:.3e}")

## pyinstaller --onefile 15lec2.py