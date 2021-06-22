

### 1. 기본 연산 연습 1

- x라는 변수에 'abcdef'라는 string이 assign돼 있다고 했을 때, 'bcdefa' 라는 string을 얻어 보세요.
- 힌트: 다음 코드에서 ??? 안의 값을 채워 됩니다.

```python
x = 'abcdef'
y = ???
print(y)
```



### 2. while 문 연습 1

- 숫자로 구성된 리스트가 주어져 있을 때, 리스트 내 값들의 평균을 구해보기.
  예를 들어, lst = [1, -2, 5, 4, -3] 일 때 1을 프린트 해 보세요.
- 아래와 같은 skeleton code를 사용해도 됩니다.
	```python
	lst = [1, -2, 5, 4, -3]
	
	sum_of_elements = 0 # lst 의 원소의 합이라는 뜻
	num_of_elements = 0 # lst 의 원소의 개수라는 뜻
	
	idx = 0 # index 라는 뜻
	while idx < ???:
	    ???
	    idx = idx + 1
	
	avg_of_elements = sum_of_elements / num_of_elements
	
	print(avg_of_elements)



### 3. While 문 연습 2

- 스트링으로 된 문장 내부에 특정 word가 몇 번 포함되는지 찾기.
- 예를 들어, sss 와 같은 문장이 주어져 있고, 'an' 이라는 단어가 sss 내부에 몇 번 나타나는지 찾기.
    - sss = 'Love is `an` open door! Love is `an` open door! Life can be so much more!' 일 때, an 이 두 개 있으니 2를 프린트하게 해 보세요.
- str을 ' ' (띄어쓰기) 기준으로 잘라 list에 보관할 수 있습니다.
    + 예) `lst = sss.split(' ')` 을 하게 되면 `lst` 는 `['Love', 'is', 'an', ...]` 이 됩니다.
- 아래의 skeleton code를 사용해도 됩니다.
    ```python
    sss = 'Love is an open door! Love is an open door! Life can be so much more!'
    lst = sss.split(' ')
    
    idx = 0 # lst의 index 라는 뜻
    num = 0 # 'an'의 개수라는 뜻
    while ???:
        if ???:
            num = num + 1
        idx = idx + 1
    print(num)
    ```

### 4. While 문 연습 3

- 스트링으로 된 문장 내부에 특정 문구가 몇 번 포함되는지 찾기.
- 예를 들어, sss 와 같은 문장이 주어져 있고, 'an' 이라는 문자열이 sss 내부에 몇 번 나타나는지 찾기.
    - sss = 'Love is `an` open door! Love is `an` open door! Life c`an` be so much more!'일 때, an 이 세 번 나타나고 있으니 3을 프린트하게 해 보세요.
  
  