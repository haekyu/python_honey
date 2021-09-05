# Day 19: 
- Pandas dataframe row 별 iteration
- Pandas groupby
- Pandas apply

## Pandas.DataFrame row 별 iteration
- 전체 column 을 iteration
    ```python
    df = pd.read_csv(...)
    for idx, row in df.iterrows():
        print(row)
        # col = row[컬럼이름]
    ```
- 특정 (몇개의) column 을 iteration
    ```python
    df = pd.read_csv(...)
    for val1, val2, val3 in zip(df[col1 이름], df[col2 이름], df[col3 이름]):
        ...
    ```

## groupby
- [groupby()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)
- DataFrame을 grouping 하는 함수
- `df.groupby(column)`
    - df의 데이터를 그룹핑 할건데, 인풋으로 주어진 column 기준으로 grouping 한다
    - 예)
        ```python
        import pandas as pd
        
        df = pd.read_csv("presidents.csv")
        group = df.groupby("Political Party")
        for idx, item in group:
            print(item)
        ```
        출력 결과
        ```
                    President  Years in office  ...  % electoral  % popular
        6       Andrew Jackson              8.0  ...         68.2       56.0
        7    Martin Van Buren               4.0  ...         57.8       50.8
        10       James K. Polk              4.0  ...         61.8       49.5
        13     Franklin Pierce              4.0  ...         85.8       50.8
        14      James Buchanan              4.0  ...         58.8       45.3
        21    Grover Cleveland              4.0  ...         54.6       48.5
        23    Grover Cleveland              4.0  ...         62.4       46.1
        27      Woodrow Wilson              8.0  ...         81.9       41.8
        31  Franklin Roosevelt             12.0  ...         88.9       57.4
        32     Harry S. Truman              8.0  ...         NA()       NA()
        34     John F. Kennedy              3.0  ...         56.4       49.7
        35   Lyndon B. Johnson              5.0  ...         NA()       NA()
        38        Jimmy Carter              4.0  ...         55.2       50.1
        41        Bill Clinton              8.0  ...         68.8       43.0
        43        Barack Obama              NaN  ...         67.8       53.7

        [15 rows x 15 columns]
                   President  Years in office  ...  % electoral  % popular
        2   Thomas Jefferson              8.0  ...         53.3       NA()
        3      James Madison              8.0  ...         69.3       NA()
        4       James Monroe              8.0  ...         82.8       NA()
        5  John Quincy Adams              4.0  ...         32.2       NA()

        [4 rows x 15 columns]
            President  Years in office  ...  % electoral  % popular
        1  John Adams              4.0  ...         95.0       NA()

        [1 rows x 15 columns]
                 President  Years in office  ...  % electoral  % popular
        16  Andrew Johnson              4.0  ...         NA()       NA()

        [1 rows x 15 columns]
                   President  Years in office  ...  % electoral  % popular
        0  George Washington              8.0  ...        100.0       NA()

        [1 rows x 15 columns]
                       President  Years in office  ...  % electoral  % popular
        15       Abraham Lincoln              4.0  ...         59.4       39.8
        17      Ulysses S. Grant              8.0  ...         72.8       52.7
        18   Rutherford B. Hayes              4.0  ...         50.1       48.0
        19     James A. Garfield              0.5  ...         58.0       48.3
        20     Chester A. Arthur              3.0  ...         NA()       NA()
        22     Benjamin Harrison              4.0  ...         58.1       47.8
        24      William McKinley              4.0  ...         60.6       51.0
        25    Theodore Roosevelt              8.0  ...         NA()       NA()
        26   William Howard Taft              4.0  ...         66.5       51.6
        28     Warren G. Harding              2.0  ...         76.1       60.3
        29       Calvin Coolidge              6.0  ...         NA()       NA()
        30        Herbert Hoover              4.0  ...         83.6       58.2
        33  Dwight D. Eisenhower              8.0  ...         83.2       55.1
        36      Richard M. Nixon              5.0  ...         55.9       43.4
        37           Gerald Ford              3.0  ...         NA()       NA()
        39         Ronald Reagan              8.0  ...         90.9       50.7
        40           George Bush              4.0  ...         79.2       53.4
        42        George W. Bush              8.0  ...         50.4       47.9

        [18 rows x 15 columns]
                         President  Years in office  ...  % electoral  % popular
        8   William Henry Harrison              0.8  ...         79.6       52.9
        9               John Tyler              4.0  ...         NA()       NA()
        11          Zachary Taylor              1.0  ...         56.2       47.3
        12        Millard Fillmore              3.0  ...         NA()       NA()

        [4 rows x 15 columns]
        ```
- `df.groupby([column1, column2, ...])`
    - 여러 column 을 기준으로 그룹핑.
    - column1 별로 그룹화하고, 다시 column2 별로 그룹화 하고, ... 여러 컬럼을 기준으로 그룹핑
    - 예)
        ```python
        import pandas as pd
        
        df = pd.read_csv("presidents.csv")
        group = df.groupby(["Political Party", "Occupation"])
        for idx, item in group:
            df2 = pd.DataFrame()
            df2["President"] = item["President"]
            df2["Political Party"] = item["Political Party"]
            df2["Occupation"] = item["Occupation"]
            print(df2)
            print("-" * 30)
        ```
        출력 결과
        ```
                President Political Party Occupation
        34  John F. Kennedy        Democrat     Author
        ------------------------------
                  President Political Party   Occupation
        32  Harry S. Truman        Democrat  Businessman
        38     Jimmy Carter        Democrat  Businessman
        ------------------------------
                 President Political Party Occupation
        27  Woodrow Wilson        Democrat   Educator
        ------------------------------
                     President Political Party Occupation
        6       Andrew Jackson        Democrat     Lawyer
        7    Martin Van Buren         Democrat     Lawyer
        10       James K. Polk        Democrat     Lawyer
        13     Franklin Pierce        Democrat     Lawyer
        14      James Buchanan        Democrat     Lawyer
        21    Grover Cleveland        Democrat     Lawyer
        23    Grover Cleveland        Democrat     Lawyer
        31  Franklin Roosevelt        Democrat     Lawyer
        41        Bill Clinton        Democrat     Lawyer
        43        Barack Obama        Democrat     Lawyer
        ------------------------------
                    President Political Party Occupation
        35  Lyndon B. Johnson        Democrat    Teacher
        ------------------------------
                   President        Political Party Occupation
        3      James Madison  Democratic-Republican     Lawyer
        4       James Monroe  Democratic-Republican     Lawyer
        5  John Quincy Adams  Democratic-Republican     Lawyer
        ------------------------------
                  President        Political Party       Occupation
        2  Thomas Jefferson  Democratic-Republican  Planter, Lawyer
        ------------------------------
            President Political Party Occupation
        1  John Adams      Federalist     Lawyer
        ------------------------------
                 President Political Party Occupation
        16  Andrew Johnson  National Union     Tailor
        ------------------------------
                   President Political Party Occupation
        0  George Washington            None    Planter
        ------------------------------
                President Political Party Occupation
        39  Ronald Reagan      Republican      Actor
        ------------------------------
                     President Political Party Occupation
        25  Theodore Roosevelt      Republican     Author
        ------------------------------
                 President Political Party   Occupation
        40     George Bush      Republican  Businessman
        42  George W. Bush      Republican  Businessman
        ------------------------------
                    President Political Party Occupation
        28  Warren G. Harding      Republican     Editor
        ------------------------------
                 President Political Party Occupation
        30  Herbert Hoover      Republican   Engineer
        ------------------------------
                      President Political Party Occupation
        15      Abraham Lincoln      Republican     Lawyer
        18  Rutherford B. Hayes      Republican     Lawyer
        19    James A. Garfield      Republican     Lawyer
        20    Chester A. Arthur      Republican     Lawyer
        22    Benjamin Harrison      Republican     Lawyer
        24     William McKinley      Republican     Lawyer
        26  William Howard Taft      Republican     Lawyer
        29      Calvin Coolidge      Republican     Lawyer
        36     Richard M. Nixon      Republican     Lawyer
        37          Gerald Ford      Republican     Lawyer
        ------------------------------
                       President Political Party Occupation
        17      Ulysses S. Grant      Republican    Soldier
        33  Dwight D. Eisenhower      Republican    Soldier
        ------------------------------
                   President Political Party Occupation
        9         John Tyler            Whig     Lawyer
        12  Millard Fillmore            Whig     Lawyer
        ------------------------------
                         President Political Party Occupation
        8   William Henry Harrison            Whig    Soldier
        11          Zachary Taylor            Whig    Soldier
        ------------------------------
        ```
- group 별 특정 함수 먹이기
    - 
    - 예)
        ```python
        import pandas as pd
        df = pd.read_csv("presidents.csv")
        group = df.groupby("Political Party")
        group.mean()
        ```
        출력 결과
        ```
                               Years in office  ...  Rating points
        Political Party                         ...
        Democrat                      5.714286  ...     582.714286
        Democratic-Republican         7.000000  ...     611.000000
        Federalist                    4.000000  ...     598.000000
        National Union                4.000000  ...     280.000000
        None                          8.000000  ...     842.000000
        Republican                    4.861111  ...     529.705882
        Whig                          2.200000  ...     385.000000

        [7 rows x 4 columns]
        ```

## apply
- DataFrame에 나만의 함수를 먹이고싶을 때
- 예)
    ```python
    import pandas as pd

    def is_number(s):
        return str(s).replace(".", "", 1).isnumeric()

    def my_sum(col):
        s = 0
        for val in col:
            if is_number(val):
                s += float(val)
        return s

    df = pd.read_csv("presidents.csv")
    app = df.apply(my_sum)
    print(app)
    ```
    출력 결과
    ```
    President                       0.0
    Years in office               220.3
    Year first inaugurated      83382.0
    Age at inauguration          2404.0
    State elected from              0.0
    # of electoral votes         9139.0
     # of popular votes       5443892.0
     National total votes           0.0
    Total electoral votes       13478.0
    Rating points               22867.0
    Political Party                 0.0
    Occupation                      0.0
    College                         0.0
    % electoral                  2381.6
    % popular                    1451.1
    dtype: float64
    ```