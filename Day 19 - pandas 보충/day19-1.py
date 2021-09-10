'''
iris 는 세 개의 class 를 갖습니다: Iris Setosa, Iris Versicolour, Iris Virginica.
iris 의 class 별 sepal length, sepal width, petal length, petal width 의
minimum, maximum, mean, standard deviation 을 구해봅시다.
'''
import pandas as pd
df = pd.read_csv("./iris.csv")
group = df.groupby("class")
# for idx, item in group:
#     print(item)
class_min = group.min().T
print(class_min)
class_max = group.max().T
class_mean = group.mean().T
class_sd = group.std().T

Iris_seto = pd.DataFrame()
Iris_seto["Min"] =class_min["Iris-setosa"]
Iris_seto["Max"] = class_max["Iris-setosa"]
Iris_seto["Mean"] = class_mean["Iris-setosa"]
Iris_seto["SD"] = class_sd["Iris-setosa"]
print("Iris-sesosa -------------------------------")
print(Iris_seto)

Iris_vers = pd.DataFrame()
Iris_vers["Min"] =class_min["Iris-versicolor"]
Iris_vers["Max"] = class_max["Iris-versicolor"]
Iris_vers["Mean"] = class_mean["Iris-versicolor"]
Iris_vers["SD"] = class_sd["Iris-versicolor"]
print("Iris-versicolor -------------------------------")
print(Iris_vers)

Iris_vir = pd.DataFrame()
Iris_vir["Min"] =class_min["Iris-virginica"]
Iris_vir["Max"] = class_max["Iris-virginica"]
Iris_vir["Mean"] = class_mean["Iris-virginica"]
Iris_vir["SD"] = class_sd["Iris-virginica"]
print("Iris-virginica -------------------------------")
print(Iris_vir)