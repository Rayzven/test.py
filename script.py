import pandas as pd
import matplotlib.pyplot as plt

#Чтение файла excel
excel_data = pd.read_excel('example.xlsx')
data = pd.DataFrame(excel_data, columns=['name', 'cost', 'year'])

#Значения затрат Группы "А" по годам
x1 = excel_data.values[(0,1,2,3,4,5), 2]
y1 = excel_data.values[(0,1,2,3,4,5), 1]

#Значения затрат Группы "B" по годам
x2 = excel_data.values[(6,7,8,9,10,11), 2]
y2 = excel_data.values[(6,7,8,9,10,11), 1]

#Значения затрат Группы "C" по годам
x3 = excel_data.values[(12,13,14,15,16,17), 2]
y3 = excel_data.values[(12,13,14,15,16,17), 1]

#Расчет суммарных затрат для каждой группы
Sum_Team_A = excel_data.values[(0,1,2,3,4,5), 1].sum()
Sum_Team_B = excel_data.values[(6,7,8,9,10,11), 1].sum()
Sum_Team_C = excel_data.values[(12,13,14,15,16,17), 1].sum()

#Расчет максимальных и минимальных затрат по годам (без учета группы)
Max_2019 = excel_data.values[(0,6,12), 1].max()
Min_2019 = excel_data.values[(0,6,12), 1].min()
Max_2020 = excel_data.values[(1,7,13), 1].max()
Min_2020 = excel_data.values[(1,7,13), 1].min()
Max_2021 = excel_data.values[(2,8,14), 1].max()
Min_2021 = excel_data.values[(2,8,14), 1].min()
Max_2022 = excel_data.values[(3,9,15), 1].max()
Min_2022 = excel_data.values[(3,9,15), 1].min()
Max_2023 = excel_data.values[(4,10,16), 1].max()
Min_2023 = excel_data.values[(4,10,16), 1].min()
Max_2024 = excel_data.values[(5,11,17), 1].max()
Min_2024 = excel_data.values[(5,11,17), 1].min()

#Размер окна с графиками и диаграммами
plt.figure(figsize=(16, 9))

#Создание графика затрат
plt.subplot(3,1,1)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3 ,y3)
plt.grid(1)
plt.title('График затрат')
plt.xlabel('Год')
plt.ylabel('Затраты')
plt.legend(['Группа А', 'Группа B', 'Группа C'])

#Создание диаграммы с суммарными значениями
plt.subplot(2,3,4)
plt.bar(['Группа А','Группа B','Группа C'] , [Sum_Team_A, Sum_Team_B, Sum_Team_C])
plt.title('Суммарные затраты за всё время')
plt.ylabel('Затраты')

#Создание диаграммы МАКСИМАЛЬНЫХ значений
plt.subplot(2,3,5)
plt.bar(['2019', '2020', '2021', '2022', '2023', '2024'] , [Max_2019,  Max_2020, Max_2021, Max_2022, Max_2023, Max_2024], color='red')
plt.title('Максимальные затраты')
plt.ylabel('Затраты')

#Создание диаграммы !минимальных! значений
plt.subplot(2,3,6)
plt.bar(['2019', '2020', '2021', '2022', '2023', '2024'] , [Min_2019,  Min_2020, Min_2021, Min_2022, Min_2023, Min_2024], color='green')
plt.title('Минимальные затраты')
plt.ylabel('Затраты')

#Вывод всех графиков и диаграмм
plt.show()
