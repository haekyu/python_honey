

### 1. 기본 연산 연습 

- 어떤 자연수가 주어져있을 때 그것이 몇 자리 수인지 알아내기. 예를 들어, x = 3 이면 1을, x = 2323 이면 4를 얻어 보세요.
  
- 힌트 1: 어떤 자연수를 string으로 변환하고 싶으면 `str(<어떤 자연수>)` 함수를 사용하면 됩니다.
  + `str(333)` 이나 `str(333) + '000'` 을 한 번 해보세요!
- 힌트 2: 아래 코드에서 ??? 안의 값을 채워도 됩니다.

```python
>>> x = 1234
>>> y = ???
>>> y
```



### 2. Boolean 연습

- XOR 연산을 만들어 봅시다.
- XOR (exclusive or) 은 두 개의 명제 가운데 한개만 참일 경우를 판단하는 논리 연산이다. 
- XOR 연산의 진리표는 다음과 같다.
  - `True xor True` == False
  - `True xor False` == True
  - `False xor True` == True
  - `False xor True` == False
- 다음 코드에서 ??? 안의 값을 채워도 됩니다.
  ```python
  x = ??? # True 아니면 False 대입
  y = ??? # True 아니면 False 대입
  z = ??? # x xor y 값이 들어가도록 만듦
  print(z)
  ```
- 힌트: [위키](https://ko.wikipedia.org/wiki/배타적_논리합) 에서 "특징" 부분을 잘 보면 됨. `^`, `ㄱ`, `V` 가 and, or, not 중 하나인데 그걸 캐치하면 됨.