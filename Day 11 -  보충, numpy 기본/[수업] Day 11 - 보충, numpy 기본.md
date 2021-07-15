# Day 11

- 보충
- numpy 기본



## 보충

### for 문 보충

- enumerate
       - iterator와 그 iterator의 순서까지 알고싶을 때
    - 예)
    
     ```python
     for th, word in enumerate(['I', 'am', 'a', 'boy', 'you', 'are', 'a', 'girl']):
         print('%d 번째 단어는 %s 다.' % (th, word))
         print('{} 번째 단어는 {} 다.'.format(th, word))
     ```

     출력 결과

     ```
     0 번째 단어는 I 다.
     0 번째 단어는 I 다.
     1 번째 단어는 am 다.
     1 번째 단어는 am 다.
     2 번째 단어는 a 다.
     2 번째 단어는 a 다.
     3 번째 단어는 boy 다.
     3 번째 단어는 boy 다.
     4 번째 단어는 you 다.
     4 번째 단어는 you 다.
     5 번째 단어는 are 다.
     5 번째 단어는 are 다.
     6 번째 단어는 a 다.
     6 번째 단어는 a 다.
     7 번째 단어는 girl 다.
     7 번째 단어는 girl 다.
     ```
    
- zip
    - 여러 iterator를 병렬적으로 한번에 알고싶을 때
    - 예)
        ```python
        name = ['철수', '영희', '영수']
        age = [1, 2, 3]
        addr = ['Seoul', 'Seoul', 'Seoul']
        
        for n, ag, ad in zip(name, age, addr):
            print('{}는 {}살이고 {}에 산다'.format(n, ag, ad))
        ```
        출력 결과
        ```
        철수는 1살이고 Seoul에 산다
        영희는 2살이고 Seoul에 산다
        영수는 3살이고 Seoul에 산다
        ```



### dict 보충

- key들 얻기
    - `딕셔너리.keys()`
    - 예1)
        ```python
        profiles = {'철수': 5, '영희': 2, '영수': 3, '가나다': 4}
        print(profiles.keys())
        ```
        출력 결과
        ```
        dict_keys(['가나다', '영수', '영희', '철수'])
        ```
    - 예2) 검색 전, key가 있는지 확인. 
        ```python
        my_keyword = '안녕'
        if my_keyword in profiles.keys():
        # if my_keyword in profiles: 도 사실은 가능하다
            v = profiles[my_keyword]
            print('%s: %s' % (my_keyword, v))
        else:
            print('ERR: no %s in the dictionary' % my_keyword)
        ```
        출력 결과
        ```
        ERR: no 안녕 in the dictionary
        ```
- value들 얻기
    - `딕셔너리.values()`
    - 예)
        ```python
        print(profiles.values())
        ```
        출력 결과
        ```
        dict_values([4, 3, 2, 5])
        ```



## numpy 기본

- Numpy는 Numeric object을 만들어 활용하는 패키지

- Numpy array 만들기
    - `np.array(어떤 list)`: list를 numpy array로 형변환
    - 예)
        ```python
        import numpy as np
        
        vec1 = np.array([1, 2, 3, 4])
        ```

- array 계산 (numeric 계산)
    - 사칙 연산 가능
        - 예)
            ```python
            # v1과 v2 정의
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([-3, -2, -1])
            
            # vector와 scalar의 계산
            >>> v1 + 1
            array([2, 3, 4])
            >>> v1 * 0.5
            array([ 0.5,  1. ,  1.5])
            
            # vector와 vector의 계산
            >>> v1 + v2
            array([-2,  0,  2])
            ```
    - dot product (내적)
        - `v1.dot(v2)`
        - 예)
            ```python
            # v1과 v2 정의
            >>> v1 = np.array([1, 2, 3])
            >>> v2 = np.array([-3, -2, -1])
            
            # v1과 v2의 내적
            >>> v1.dot(v2)
            -10
            ```
    
- `shape()`: numpy array 의 모양 (차원) 을 알 수 있다.
    
    - 예)
        
        ```python
        >>> v1 = np.array([1, 2, 3])
        >>> v1.shape
        (3,)
        
        >>> v2 = np.array([[1, 2], [3, 4], [5, 6]])
        >>> v2.shape
        (3, 2)
        ```
        
        
