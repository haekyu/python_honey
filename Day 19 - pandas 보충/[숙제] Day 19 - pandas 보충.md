## Pandas 연습 
- [./iris.csv](./iris.csv) 를 pandas로 읽어봅시다. 이 데이터는 iris 라는 식물들의 데이터입니다. iris 는 세 개의 class 를 갖습니다: Iris Setosa, Iris Versicolour, Iris Virginica.
- iris 의 class 별 sepal length, sepal width, petal length, petal width 의 minimum, maximum, mean, standard deviation 을 구해봅시다. 다음과 비슷한 값이 나오면 됩니다 (출력 형식은 달라도 됩니다)
    ```
    Summary Statistics:
                    Min  Max   Mean    SD
    sepal length: 4.3  7.9   5.84  0.83
    sepal width: 2.0  4.4   3.05  0.43 
    petal length: 1.0  6.9   3.76  1.76
    petal width: 0.1  2.5   1.20  0.76
    ```