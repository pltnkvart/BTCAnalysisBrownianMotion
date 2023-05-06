import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics

with open('lab.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    values = [int(row[1]) for row in reader]

diffs = []
avg_squares = []

for step in range(1, len(values) - 10):
    diff = []
    for i in range(len(values) - step):
        diff.append(round(values[i + step] - values[i], 1))
    diffs.append(diff)

# # вычисляем средние значения квадратов для каждого списка diffs
n = 0
time = 5
step = 1
avg_squares = []
razbros = []

for diff in diffs:
    diff_square = 0.0
    squares = [x ** 2 for x in diff]
    avg_square = statistics.mean(squares)
    avg_squares.append(round(avg_square, 1))
    print(f"Интервал {time} c, среднее значение квадрата : {avg_squares[n]}")
    for i in range(len(diff)):
        print(f"{i}-{i + step}: {diff[i]} : {diff[i] ** 2} : {round(diff[i] ** 2 - avg_square, 1)}")
        diff_square += (round(diff[i] ** 2 - avg_square, 1)) ** 2
    # print(diff_square)
    razbros.append(np.sqrt(abs(round(diff_square, 1)) / (len(diff) * (len(diff) - 1))))
    print("\n")
    n += 1
    time += 5
    step += 1

print(razbros)
# создаем график на основе массива avg_squares
plt.plot(avg_squares, 'o')
plt.plot(np.arange(len(avg_squares)),
         np.poly1d(np.polyfit(np.arange(len(avg_squares)), avg_squares, 1))(np.arange(len(avg_squares))))
plt.xticks(np.arange(len(avg_squares)), [5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
plt.errorbar(np.arange(len(avg_squares)), avg_squares, yerr=razbros, fmt='o')

# задаем название графика и осей
plt.title('График 2.26.2 Зависимость среднего значения квадрата проекции премещения от времени', fontsize=10)
plt.xlabel("Интервалы времени t, с")
plt.ylabel('Среднее значение квадратов <x²>, мм²', )
plt.grid(True)

# добавляем легенду и выводим график на экран
plt.show()
