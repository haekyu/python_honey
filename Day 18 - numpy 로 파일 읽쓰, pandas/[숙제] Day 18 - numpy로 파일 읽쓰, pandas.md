## 1. Pandas 연습 1 (데이터 읽기)
- [./data/presidents.csv](./data/presidents.csv) 를 pandas로 읽어봅시다. presidents.csv는 미국 대통령들의 정보를 정리한 표입니다.
- 대충 다음과 비슷한 출력을 보이면 됩니다.
    ```python
    president_info = ???

    print(president_info.columns)
    print()
    print(president_info['President'])
    ```
    출력 결과
    ```
    Index(['President', 'Years in office', 'Year first inaugurated',
       'Age at inauguration', 'State elected from', '# of electoral votes',
       ' # of popular votes ', ' National total votes ',
       'Total electoral votes', 'Rating points', 'Political Party',
       'Occupation', 'College', '% electoral', '% popular'],
      dtype='object')

    0          George Washington
    1                 John Adams
    2           Thomas Jefferson
    3              James Madison
    4               James Monroe
    5          John Quincy Adams
    6             Andrew Jackson
    7          Martin Van Buren
    8     William Henry Harrison
    ...
    ```

## 2. Pandas 연습 2 (데이터 추출하기)
- presidents.csv의 ' # of popular votes ' 에 해당하는 컬럼 데이터를 list로 읽어봅시다.
- 대충 다음과 같은 출력을 보이면 됩니다.
    ```python
    pop_votes = ???
    print(pop_votes)
    ```
    출력 결과
    ```
    ['NA()', 'NA()', 'NA()', 'NA()', 'NA()', 'NA()', ' 642,553 ', ' 764,176 ', ' 1,275,390 ', 'NA()', ' 1,339,494 ', ' 1,361,393 ', 'NA()', ' 1,607,510 ', ' 1,836,072 ', ' 1,865,908 ', 'NA()', ' 3,013,650 ', ' 4,034,311 ', ' 4,446,158 ', 'NA()', ' 4,874,621 ', '5443892.0', ' 5,551,883 ', ' 7,108,480 ', 'NA()', ' 7,676,258 ', ' 6,293,152 ', ' 16,133,314 ', 'NA()', ' 21,411,991 ', ' 22,825,016 ', 'NA()', ' 33,936,137 ', ' 34,221,344 ', 'NA()', ' 31,785,148 ', 'NA()', ' 40,830,763 ', ' 43,904,153 ', ' 48,886,097 ', ' 44,909,326 ', ' 50,460,110 ', ' 69,492,376 ']
    ```
- 힌트: 형 변환을 해야할 수도 있습니다. 
    - ex) 무언가를 list로 바꾸고 싶다면, `list(그 무언가)` 를 통해 list로의 형 변환이 가능합니다.

## 3. Pandas 연습 3 (데이터 파싱하기)
- 2번에서 얻은 리스트 pop_votes의 원소를 원하는 형태로 변경해봅시다.
- 우선 각 원소들은 string이 아닌 int를 갖게끔 만드려고 합니다.
    - 'NA()' 의 경우, -1로 변경해 줍시다.
    - 나머지는 그대로 숫자로 변경하면 됩니다.
        - 예) ' 1,275,390 ' -> 125390
- 대충 다음과 같은 출력을 보이면 됩니다.
    ```python
    ???
    print(pop_votes)
    ```
    출력 결과
    ```
    [-1, -1, -1, -1, -1, -1, 642553, 764176, 1275390, -1, 1339494, 1361393, -1, 1607510, 1836072, 1865908, -1, 3013650, 4034311, 4446158, -1, 4874621, 5443892, 5551883, 7108480, -1, 7676258, 6293152, 16133314, -1, 21411991, 22825016, -1, 33936137, 34221344, -1, 31785148, -1, 40830763, 43904153, 48886097, 44909326, 50460110, 69492376]
    ```