# Day 08 - Class

## Class

- 나만의 data type 을 만들어주는 문법

- 용어
    - Class vs. Object
        - class: 내가 실존하는 어떤 특정 데이터를 만들기 위해 만든 `레시피`
        - object: (class로 만든) 실존하는 데이터
    - Class 내부 구성요소
        - attribute
            - class 내부의 data
            - class 내부 어떤 곳이든 access 가능한 global variable
        - function: attribute 를 처리하는 특정 class 만의 operation
    
- Class 만드는 방법

    ```python
    class 클래스이름:
        
        # Attributes
        def __init__(self):
            self.attribute1 = init 값1
            self.attribute2 = init 값2
            self....
    
        # Functions
        def 함수이름(self, 인풋1, ...):
            ...  
    ```

- Object 만드는 방법 (Construct 한다고 하기도 한다.)

    - `클래스이름()`

    - 예)

        ```python
        # Cat class 만들기
        class Cat:
            def __init__(self):
                self.age = 0
                self.brain = {}
            def eat(self, food, flavor):
                self.brain[food] = flavor
                self.age += 1
        
        # kitty 라는 object 만들기. kitty 의 데이터 타입은 Cat 이다.
        kitty = Cat()
        ```

- Object 사용 방법
    - attribute 에 접근하고 싶을 때
        - `object.attribute이름`
        
    - 함수를 사용하고 싶을 때
    
        - `object.함수이름(인풋...)`
    
    - 예)
    
        ```python
        # Cat class 만들기
        class Cat:
            def __init__(self):
                self.age = 0
                self.brain = {}
            def eat(self, food, flavor):
                self.brain[food] = flavor
                self.age += 1
        
        # kitty 라는 object 만들기. kitty 의 데이터 타입은 Cat 이다.
        kitty = Cat()
        
        # kitty 의 attribute 중 하나인 brain에 접근
        print(kitty.brain)
        
        # kitty 의 함수 중 하나인 eat() 사용
        kitty.eat('apple', 'good')
        
        # kitty 의 attribute 중 하나인 brain에 접근
        print(kitty.brain)
        ```
    
        실행 결과
    
        ```
        {}
        {'apple': 'good'}
        ```
    
        

## Object Oriented Programming (OOP)
- 한국말로 `객체 지향 프로그래밍`이라고 한다. 클래스를 만들어서 코드를 짜는 것을 우리는 OOP 스타일이라고 한다.
- OOP 장점
  - 코드가 아름다워진다! 기능별로 코드를 깔끔하게 모듈화할 수 있기 때문!
  - 유지 보수가 쉬워짐 - 원래 아름다운 코드는 유지 보수가 용이해짐.
  - 보안성 증가 - 내부 정보 (ex: attribute의 이름) 를 감출 수 있음. 즉 코드를 까보지(?) 않는 한 클래스 내부에 어떠한 이름의 attribute가 있는지 알 수 없음.

