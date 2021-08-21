# Day 18
- numpy 로 파일 읽고 쓰기
- Pandas

## numpy 로 파일 읽고 쓰기
- 숫자 자체를 읽어올 때
    - ex) matrix를 읽어올 때
- numpy library를 import 해와야 함
    ```python
    # numpy library를 가져와서 np 라고 부른다
    import numpy as np
    ```
- 파일 읽기: [numpy.loadtxt](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.loadtxt.html) 함수 사용
    - text 파일을 읽어와서 array로 리턴한다.
    - 대표적인 parameters
        - fname: name/path of a text file
        - dtype: data type
        - delimiter: a string used to separate values
    - return data read from the text file
    - 예)
        ```python
        import numpy as np
        mat = np.loadtxt('./sample-mat.txt', dtype=int, delimiter=' ')
        print(mat)
        ```
        출력 결과
        ```
        [[-1  2  1]
         [ 5  2 -1]
         [ 3  2  1]]
        ```
- 파일 쓰기: [numpy.savetxt](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.savetxt.html) 함수 사용
    - array_like (numpy array, list, tuple, ...) data를 text file로 저장한다.
    - 대표적인 parameters
        - fname: name/path of a text file
        - X: array_like data to be saved to the text file
        - fmt: format of values. ex) '%d', '%.2lf', ...
        - delimiter: a string used to separate values
    - does not return anything (return None)
    - 예)
        ```python
        # Import numpy and say it as np
        import numpy as np

        # Read sample-mat.txt
        mat = np.loadtxt('./sample-mat.txt', dtype=int, delimiter=' ')
        
        # Make transpose of mat
        trans_mat = mat.T

        # Save trans_mat
        np.savetxt('./sample-transpose-mat.txt', trans_mat, fmt='%d', delimiter=' ')
        ```
        ['./sample-transpose-mat.txt'](./sample-transpose-mat.txt) 를 열어보면 아래와 같다.
        ```
        -1 5 3
        2 2 2
        1 -1 1
        ```

## pandas
- spreadsheet 를 처리하는 데에 특화된 라이브러리
    - spreadsheet 파일의 예시
        - csv: comma separated values
        - tsv: tab separated values
        - xlsx: 엑셀파일
- pandas library를 import 해와야 함.
    ```python
    # pandas library를 가져와서 pd 라고 부른다
    import pandas as pd
    ```
- 파일 읽기: [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html) 함수 사용
    - 텍스트 파일을 읽어서 DataFrame 형식으로 저장한다.
        - DataFrame 이라는 data type이 따로 있음
        - DataFrame 은 데이터를 행/렬로 구분한 2D table이라고 생각하면 됨 ([참고](http://pinkwink.kr/735))
        - DataFrame 은 dictionray 비슷하게 구현되어있음.
            - key: column 의 이름
            - val: 해당 column의 data 들
    - 대표적인 parameters
        - filepath_or_buffer: path of file to read
        - sep: separator, a string used to separate values
        - names: list of column names to use
            - ex) ['State', 'No. of Presidents']
            - 만약 names가 주어지지 않으면, names는 자동으로 텍스트파일의 가장 첫 번째 row가 된다.
            - 아니면 `header=None` 을 주고, 첫 번째 row도 데이터로 읽히게끔 해도 됨.
        - dtype: Type name or dict of column -> type, default None
    - 예) [state-presidents.csv](./state-presidents.csv) 읽기
        ```python
        import pandas as pd
        state_president_dataframe = pd.read_csv('./state-presidents.csv', sep=',')
        print(state_president_dataframe)
        ```
        출력 결과
        ```
                     State  No. of Presidents
        0          Alabama                  0
        1           Alaska                  0
        2          Arizona                  0
        3         Arkansas                  1
        4       California                  2
        5         Colorado                  0
        6      Connecticut                  0
        7         Delaware                  0
        8          Florida                  0
        ...
        ```
    - column names 얻기
        - `dataframe.columns` 를 통해 column 이름들을 얻을 수 있음.
        - 예)
            ```python
            names = state_president_dataframe.columns
            print(names)

            name_lst = list(names)
            print(name_lst)
            ```
            출력 결과
            ```
            Index(['State', 'No. of Presidents'], dtype='object')
            ['State', 'No. of Presidents']
            ```
    - column names 변경하기 
        - 방법1) 직접 dataframe.columns 에 원하는 이름들 대입하기
            - 예)
                ```python
                state_president_dataframe.columns = ["state", "num"]
                ```
        - 방법2) [pandas.DataFrame.rename](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html) 이용
            - 예)
                ```python
                new_df = state_president_dataframe.rename(columns={names[0]: 'state', names[1]: 'num'})
                print(new_df)

                ```
                출력 결과
                ```
                             state  num
                0          Alabama    0
                1           Alaska    0
                2          Arizona    0
                3         Arkansas    1
                4       California    2
                5         Colorado    0
                6      Connecticut    0
                7         Delaware    0
                8          Florida    0
                ...
                ```
    - cf) [pandas.read_excel](https://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.read_excel.html) 함수: Excel 파일을 읽어 DataFrame으로 저장하기
- 파일 쓰기: [pandas.DataFrame.to_csv](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DataFrame.to_csv.html) 사용
    - DataFrame 을 파일로 저장
    - 대표적인 parameters
        - path_or_buf: 저장할 파일 경로
        - sep: separator
        - index: 인덱스를 저장할지 말지
    - 예)
        ```
        new_df = state_president_dataframe.rename(columns={names[0]: 'state', names[1]: 'num'})
        new_df.to_csv('./state-president.tsv', sep='\t')
        ```
        ['./state-president.tsv'](./state-president.tsv) 를 열어보면 아래와 같다.
        ```
            state   num
        0   Alabama 0
        1   Alaska  0
        2   Arizona 0
        3   Arkansas    1
        4   California  2
        5   Colorado    0
        6   Connecticut 0
        7   Delaware    0
        8   Florida 0
        ...
        ```
- Indexing 
    - 특정 column, 혹은 특정 row, 혹은 특정 (row, column) 의 데이터를 access 하고싶을 때
    - 특정 column 인덱싱
        - `df[컬럼이름]`
    - 특정 row 인덱싱
        - `df.loc[row_index, :]`
    - 특정 (row, column) 인덱싱
        - `df[컬럼이름][row_index]`
    - 인덱싱을 통해 데이터프레임을 수정할 수 있다.
        - 예)
            ```python
            df[컬럼이름] = 원하는 컬럼데이터 (리스트 등등)
            ```
- Slicing
    - Data frame 의 slicing 도 가능하다.
    - 예)
        ```python
        # Row slicing
        df.loc[0:2, :]

        # Column slicing
        df.loc[row_index, "name": "age"]  
        ```