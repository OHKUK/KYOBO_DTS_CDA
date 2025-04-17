#### 클래스 class
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

calc1 = Calculator()  # 계산기1  / 객체 
calc2 = Calculator()  # 계산기2

print(calc1.add(3))  # 3 (계산기1의 result)
print(calc2.add(4))  # 4 (계산기2의 result)

## 클래스 선언하기 1. 

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    
        
# 객체 생성
person1 = Person("오애순", 18)
person2 = Person("양관식", 19)

# 속성 접근
print(person1.name)  
print(person1.age)   
print(person2.name)  
print(person2.age)   


## 클래스 선언하기 2.  학생 클래스를 정의 
class Student: 
    def __init__(self, name, age, major) : 
        self.name = name                
        self.age = age 
        self.major = major 
    def introduce(self) : 
        print(f"안녕하세요! 저는 {self.name}이고, 나이는 {self.age}살이며 {self.major}를 전공하고 있습니다.")


## Student 클래스의 객체 생성 
student1 = Student("홍길동", 20, "컴퓨터공학") 
student2 = Student("김영희", 22, "경영학") 


## 메서드 호출 
student1.introduce()
student2.introduce()

#### 클래스 선언하기 3. 은행 계좌 시스템 

#### account_holder : 계좌주 
#### balance : 잔고 
#### deposit : 입금 
#### withdraw : 출금 

class BankAccount: 
    def __init__(self, account_holder, balance = 0 ) : 
        self.account_holder = account_holder
        self.balance = balance 
    
    def deposit(self, amount) : 
        self.balance += amount 
        print(f"{amount}원이 입금되었습니다. 현재 잔액은 {self.balance}원 입니다.")

    def withdraw(self, amount) : 
        if amount  > self.balance : 
            print("잔액이 부족합니다.") 
        else: 
            self.balance -= amount 
            print(f"{amount}원이 출금되었습니다. 현재 잔액은 {self.balance}원 입니다.")



account = BankAccount("홍길동", 10000) 
account.deposit(5000)
account.withdraw(2000)
account.withdraw(20000)


#### 클래스 선언하기 4. 전달 값이 없을 경우 __init__ 생략 할 수 있다. 
#### 속성 전달이 안된다.
class Student: 
    def introduce(self) : 
        self.name = "test"         
        print(f"안녕하세요! {self.name}")


#### Student 클래스의 객체 생성 
student1 = Student()   
student2 = Student() 


#### 메서드 호출 
student1.introduce()
student2.introduce()


#### 클래스 예제 
#### 자동차 클래스 1. 

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("현대", "그랜저", 2023)
print(f"{car1.year}년식 {car1.brand} {car1.model}")  


car2 = Car("기아","카니발", 2021)
print(f"{car2.year}년식 {car2.brand} {car2.model}")  

#### 클래스 생성 

class Car:
    count = 0                      # 클래스 변수, 이 클래스로 만들어진 모든 객체가 공유한다. 

    def __init__(self, name):
        self.name = name
        Car.count += 1              

    @classmethod
    def total_cars(cls):          # 클래스 메서드 : 첫번째 인자로 클래스 자신을 자동으로 받는다. 
        return f"총 {cls.count}대의 자동차가 생성되었습니다."

#### 객체 생성 및 클래스 메서드 호출
car1 = Car("소나타")
car2 = Car("아반떼")
print(Car.total_cars())  
    #### 호출시  ClassName.Method 형태로 호출 


#### 부모 클래스 정의
class Animal:
    def __init__(self, name):
        self.name = name                   ## name 속성을 정의한다.
    
    def speak(self):                     
        return f"{self.name}은 소리를 냅니다."

#### 자식 클래스 정의 (Animal 상속)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)             # super().__init__name(name) 부모 클래스의 초기화 메서드 호출
        self.breed = breed
    
    def speak(self):                        # 부모 클래스의 메서드 오버라이딩
        return f"{self.name}는 멍멍 짖습니다."

#### 객체 생성 및 사용
animal = Animal("동물")
dog = Dog("바둑이", "진돗개")

print(animal.speak())  
print(dog.speak())    
print(f"{dog.name}의 품종은 {dog.breed}입니다.") 

#### 부모 클래스 1
class Animal:
    def eat(self):
        print("동물이 먹이를 먹습니다.")

#### 부모 클래스 2
class Walker:
    def walk(self):
        print("걷는 생물입니다.")

#### 자식 클래스 (Animal과 Walker를 상속)
class Dog(Animal, Walker):
    def bark(self):
        print("개가 멍멍 짖습니다.")

#### 객체 생성 및 메서드 호출
dog = Dog()
dog.eat()   
dog.walk()  
dog.bark()  

#### 다중 상속에서 메서드 충돌 처리 

class A:
    def action(self):
        print("A의 action 호출")

class B:
    def action(self):
        print("B의 action 호출")

#### 다중 상속
class C(A, B):  # A와 B를 상속받음
    def action(self): 
        print("C의 action 호출")

#### 객체 생성 및 메서드 호출
c = C()
c.action()  

####다중 상속에서 메서드 충돌 처리  ( 메서드 이름이 같을 경우 )

class A:
    def action(self):
        print("A의 action 호출")

class B:
    def action(self):
        print("B의 action 호출")

#### 다중 상속
class C(A, B):  # A와 B를 상속받음
    pass

#### 객체 생성 및 메서드 호출
c = C()
c.action()  

#### MRO (Method Resolution Order)
print(C.__mro__)
       
class A:
    def __init__(self):
        print("A 초기화")

class B:
    def __init__(self):
        print("B 초기화")

class C(A, B):  # 다중 상속
    def __init__(self):
        super().__init__()               # MRO에 따라 A의 __init__이 먼저 호출됨
        print("C 초기화")

c = C()
#### 다중 상속과 super()
#### 다중 상속과 super()
#### super()를 사용하면 MRO에 따라 부모 클래스의 메서드를 적절히 호출할 수 있다 
class A:
    def __init__(self):
        print("A 초기화")

class B:
    def __init__(self):
        print("B 초기화")

class C(A, B):  # 다중 상속
    def __init__(self):
        super().__init__()               # MRO에 따라 A의 __init__이 먼저 호출됨
        print("C 초기화")

c = C()


class Animal:
    def eat(self):
        print("동물이 먹이를 먹습니다.")

class Machine:
    def operate(self):
        print("기계가 작동합니다.")

# 다중 상속
class RobotDog(Animal, Machine):
    def bark(self):
        print("로봇 개가 멍멍 짖습니다.")

robot_dog = RobotDog()
robot_dog.eat()      # 출력: 동물이 먹이를 먹습니다.
robot_dog.operate()  # 출력: 기계가 작동합니다.
robot_dog.bark()     # 출력: 로봇 개가 멍멍 짖습니다.


# pass
#### 1. 빈 함수 정의 

def my_function():
    pass              # 나중에 구현할 예정

print("함수 호출 가능")
my_function()          # 아무 동작도 하지 않음

#### 2. 빈 클래스 정의 
class MyClass:
    pass              # 나중에 속성과 메서드를 추가할 예정

#### 객체 생성 가능
obj = MyClass()
print(type(obj))  
#### 3. 조건문에서 pass 사용 
x = 10

if x > 5:
    pass               # 조건이 참일 때 아무 동작도 하지 않음
else:
    print("x는 5 이하입니다.")
#### 4. 루프에서 pass 사용 
#### 루프 내 특정 조건에서 동작을 생략하고 싶을 때 사용 
for i in range(5):
    if i % 2 == 0:
        pass             # 짝수일 경우 아무 동작도 하지 않음
    else:
        print(f"{i}는 홀수입니다.")
#### 5. 예외처리에서 pass 사용 
#### 예외를 처리하지만, 아무 동작도 하지 않고 프로그램 실행을 계속 진행하라 때 

try:
    x = int("invalid")  # 문자열을 정수로 변환 시도 (실패)
except ValueError:
    pass                 # 에러를 무시하고 지나감

print("프로그램 계속 실행")
