def greeting(name):
    return f"Hello, {name}!"

person = {
    "name": "Alice",
    "age": 25,
    "country": "Korea"
}

import mypackage.mymodule

print(mypackage.mymodule.greeting("John"))  # 출력: Hello, John!
print(mypackage.mymodule.person["age"])     # 출력: 25


## 3. 모듈의 일부만 가져오기 
# from 키워드를 사용하여 특정 함수나 변수를 가져온다. 
# 사용하는 함수앞에 모듈명을 기록하지 않아도 된다. 

from mypackage.mymodule import  greeting

print(greeting("Jane"))  # 출력: Hello, Jane!

#### 4. 모듈에 별칭 주기
#### as 키워드를 사용하여 모듈에 별칭을 부여한다. 

import mypackage.mymodule as mx

print(mx.greeting("Tom"))  # 출력: Hello, Tom!


## 모듈 실습 1. 영화표 금액 계산 모듈 만들기 

## [theater_module.py]   : 파일 변도로 생성해서 저장한다. 

# 일반 가격 
def price(people) : 
    print("{0}명, 영화표 가격은 {1}원입니다. ".format(people, people * 10000))

# 조조 할인 가격 
def price_morning(people) : 
    print("{0}명, 영화표 가격은 {1}원입니다. ".format(people, people * 6000))

# 학생 할인 가격 

def price_student(people) : 
    print("{0}명, 영화표 가격은 {1}원입니다. ".format(people, people * 4000))

## 모듈 실습 2. 모듈 사용하기 
# main.py
import mypackage.theater_module

mypackage.theater_module.price(3)
mypackage.theater_module.price_morning(5)
mypackage.theater_module.price_student(2)

## 모듈 실습  3. 모듈의 일부만 가져오기 

from mypackage.theater_module import price, price_morning

price(3)
price_morning(5)
# price_student(2)    ## 오류 

# 1. 패키지 생성하기 

# - mypackage/ 
#     - __init__.py 
#     - math_operations.py 
#     - string_operations.py 


# math_operations.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b


# string_operations.py
def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

#### 2. 패키지 사용하기 

#### main.py
import mypackage.math_operations as math_ops
import mypackage.string_operations as str_ops

print(math_ops.add(10, 5))                 
print(math_ops.multiply(10, 5))            

print(str_ops.to_uppercase("hello"))       
print(str_ops.to_lowercase("WORLD"))       

#### 3. 서브 패키지 활용하기 
#### 서브 패키지를 사용하면 더 복잡한 구조를 관리할 수 있다. 
#### - mypackage/ 
####     - __init__.py 
####     - math_operations.py 
####     - string_operations.py 
####     - subpackage/
####         - __init__.py 
####         - advanced_math.py 

#### advanced_math.py
def power(base, exponent):
    return base ** exponent

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

#### main.py
from mypackage.subpackage import advanced_math

print(advanced_math.power(2, 3))  
print(advanced_math.factorial(5))  

import sys

sys.path.append("C:/Users/3-15/Desktop/python_lab")

import mypackage

print(mypackage.add(10, 20))        
print(mypackage.to_uppercase("hi")) 