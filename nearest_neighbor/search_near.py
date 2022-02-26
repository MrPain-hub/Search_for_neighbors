import pandas as pd
import numpy as np
from annoy import AnnoyIndex
from icecream import ic
"""
Импорт входных данных
"""
from nearest_neighbor.read_dataset import sett_np, stress_np, u_np, sig_np
"""
Создание пространства
"""
dimension = len(sett_np[0])  # Размерность данных
forest = 20  # Сколько деревьев использовать

Space = AnnoyIndex(dimension, metric='angular')
for i, j in enumerate(sett_np):  # Добавление векторов в пространство
    Space.add_item(i, j)
Space.build(n_trees=forest, n_jobs=-1)  # После build нельзя добавлять вектора
"""
Поиск в пространстве
"""
Ax, Ay, Az = {}, {}, {}
Au, Asig = {}, {}
find_near = 1000  # Сколько найти соседий
for num_point, point in enumerate(stress_np):
    neighbor = Space.get_nns_by_vector(point, find_near, search_k=-1)
    length_min = 0.0
    for near in neighbor:  # Выбор лучшего соседа
        """
        Евклидово расстояние
        """
        length = np.sum(
            np.square(
                point - sett_np[near]
            )
        )
        if length < length_min or length_min == 0:
            length_min = length

            Ax[num_point] = sett_np[near][0]
            Ay[num_point] = sett_np[near][1]
            Az[num_point] = sett_np[near][2]
            Au[num_point] = u_np[near]
            Asig[num_point] = sig_np[num_point]
"""
Запись результата
"""
output = pd.DataFrame({})

output["координата x"] = Ax.values()
output["координата y"] = Ay.values()
output["координата z"] = Az.values()
output["|u|"] = Au.values()
output["sig zz"] = Asig.values()

output[["координата x",
        "координата y",
        "координата z",
        "|u|",
        "sig zz"]].to_excel(r'out_dataset.xlsx', index=False)
