import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics

with open('btc.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    values = [float(row[1].replace(',', '.')) for row in reader]

diffs = []
avg_squares = []

for step in range(1, len(values) - 1):
    diff = []
    for i in range(len(values) - step):
        diff.append(round(values[i + step] - values[i], 1))
    diffs.append(diff)

# # вычисляем средние значения квадратов для каждого списка diffs
n = 0
time = 1
step = 1
avg_squares = []
razbros = []

for diff in diffs:
    diff_square = 0.0
    squares = [x ** 2 for x in diff]
    avg_square = statistics.mean(squares)
    avg_squares.append(round(avg_square, 1))
    print(f"Интервал {time} месяцев, среднее значение квадрата : {avg_squares[n]}")
    for i in range(len(diff)):
        print(f"{i}-{i + step}: {round(diff[i], 1)} : {round((diff[i] ** 2), 1)} : {round(diff[i] ** 2 - avg_square, 1)}")
        diff_square += (round(diff[i] ** 2 - avg_square, 1)) ** 2
    razbros.append(np.sqrt(abs(round(diff_square, 1)) / (len(diff) * (len(diff) - 1))))
    print("\n")
    n += 1
    time += 1
    step += 1

print("Массив погрешностей для каждой точки:")
print(razbros)

# создаем график на основе массива avg_squares
plt.plot(avg_squares, 'o',)
plt.plot(np.arange(len(avg_squares)),
         np.poly1d(np.polyfit(np.arange(len(avg_squares)), avg_squares, 1))(np.arange(len(avg_squares))))
plt.errorbar(np.arange(len(avg_squares)), avg_squares, yerr=razbros, fmt='o')
plt.xticks(np.arange(len(avg_squares)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# задаем название графика и осей
plt.title('График 2.26.3 Зависимость среднего значения квадрата проекции премещения от времени (Курс BTC)', fontsize=10)
plt.xlabel('Интервалы времени t, месяцев')
plt.ylabel('Среднее значение квадратов <x²>, мм²')
plt.grid(True)

# добавляем легенду и выводим график на экран
plt.show()
