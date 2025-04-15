#연산자
100 - (5 + 7) * 4 + 81 / 9 ** 2

## 변수계산 
# 100 - (5 + 7) * 4 + 81 / 9 ** 2
a = 100 
b = 5 
c = 7 
d = 4 
x = 81 
y  = 9 
z = 2 
print( a - (b + c) * d + x / y ** z)

## cascading assignment
# "=" 연산자를 사용하여 여러 변수를 연결하고, 가장 오른쪽에 있는 값을 모든 변수에 할당한다. 
x = y = z = 1 + 2 + 3
print(x, y, z)

x = 20
print(x, y, z)


# 가변 객체(예: 리스트, 딕셔너리)는 동일한 객체를 여러 변수에서 참조할수 있기 때문에, 
# 주의해서 사용 
# 불변 객체는 안전
a = b = []
a.append(2)
print(a)
print(b)

## value swapping (값 교환)
# 두 변수의 값을 서로 바꾸는 작업 
a = 100 
b = 150
print("a=",a,"b=",b)
t = a
a = b
b = t
print("a=",a,"b=",b)

a = 100 
b = 150
print("a=",a,"b=",b)
a, b = b, a
print("a=",a,"b=",b)

##  거듭제곱(exponential)
print(2 ** 8)

## 나누기 (division) 
money = 6000
print(money / 12)


## 몫 (floor division)
print(money // 13)

## 나머지 (modulo)
remainder = money % 13 
print(remainder)

#논리연산
print(5 > 3 and 5 < 10)
print( not (10 == 11))
print(10 == 11 or 12 > 10)

#복합대입연산
number = 10
# number = number + 1 
number += 1
print(number)

# number = number - 1
number -= 1
print(number)

# number = number * 2 
number *= 2
print(number)

# number = number / 2 
number /= 2
print(number)

# 절대값
print(abs(-5))
print(abs(5))

# 최대값 vs. 최소값 5, 10 15, 20 

print(max(5, 10, 15, 20))
print(min(5, 10 ,15, 20))

# 올림
print(round(3.14))
print(round(3.12345678,6))

#math 모듈 사용
from math import *
# 올림 
result = ceil(3.14)
print(result)

# 내림
result = floor(3.14)
print(result)

# 제곱근
result = sqrt(256)
print(result)

# random 모듈
from random import *
 # 0.0 이상 10.0 미만의 난수 생성 
print(random()* 10)


# 0 이상 10 미만의 난수 생성 
print(int(random()* 10))


# 1 이상 11미만의 난수 생성 
print(int(random()* 10)+1)

## 예를 들어 1 ~ 45 사이의 정수 범위안에서 로또 번호를 뽑으려면

print(int(random()* 45+1))
print(int(random()* 45+1))
print(int(random()* 45+1))
print(int(random()* 45+1))
print(int(random()* 45+1))
print(int(random()* 45+1))

print(randrange(1,10))
print(randint(1, 10))