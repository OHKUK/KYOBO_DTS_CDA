## 1. 기본적인 함수 선언 

# 함수 선언
def greet() :
    print("안녕하세요")


# 함수 호출
print("시작")
greet()

## 2. 매개변수가 있는 함수 
# 함수에 입력값(매개 변수, parameter, argument)을 전달하여 동적인 작업을 수행할 수 있다.

# 함수 선언 
def greet(name) :
    print(f"안녕하세요. {name}님!")

# 함수 호출
greet("파이썬")

## 3. 값을 반환하는 함수 

# 함수 선언 
def add(a, b) :
    return a + b

# 함수 호출 및 결과 저장
result = add(9, 5)
print(result)

## 4. 기본값이 있는 매개변수 
## 함수에서 매개변수에 미리 지정해 둔 값 
def greet(name="힘들어요") :
    print(f"안녕하세요 {name}님")


# 기본값 사용
greet()

# 매개변수 전달
greet("졸려요")

## 5. 여러 개의 값을 반환하는 함수 / return 에서 반환값 계산 
def calculate(a, b):
    return a + b, a - b, a * b, a / b

# 여러 값을 반환받아 저장
add_result, sub_result, mul_result, div_result = calculate(10,20)
print(f"+ : {add_result} - : {sub_result} * : {mul_result} / : {div_result}")

## 6. 여러 함수를 한 줄  호출 
def add(a, b) : 
    return a + b 

def multiple(a, b) : 
    return a * b 
    
f1, f2 = add(2, 5)*10 , multiple(3,7)-5

print("add : ",f1, "multiple : " ,f2)

## 7. 키워드 인자 사용 
## 키워드 인자는 보통 어떤 함수에 전달값이 많고 기본값이 잘 정의 되어 있을 때, 대부분 기본값을 그대로 사용하면서
## 필요한 부분만 값을 전달하려는 경우에 유용하다.


def profile(name, age, home="Seoul") : 
    print(name, age, home) 


## 함수를 호출 할 때 함수에서 정의된 순서대로 입력하는 전달값을 위치 인자(positional argument)

profile("제니","25","Seoul")
profile(home="방콩",name="로제",age="25")
profile(name="로제",age="25")

## 8. 가변 인자 / 가변 매개 변수 (*args)

def profile(name, age, home, email, phone): 
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
    print(home, email, phone) 

profile("양관식", 19, "제주", "sweetboy@jeju.com", "1234-5678")
profile("부상길", 27, "제주", "harkboy@jeju.com", "5678-1234")

## 가변 매개 변수 
def profile(name, age, *info) :#info=튜플로나오네
    print("이름: {0}\t나이: {1}\t".format(name, age), end=" ") 
    print(info,type(info))

profile("양관식", 19, "제주", "sweetboy@jeju.com", "1234-5678")
profile("부상길", 27, "제주", "harkboy@jeju.com", "5678-1234")

## 가변 매개 변수 추가 예제 
### 함수를 선언하고 매개변수를 sum_all
def add(*info) :
    sum_all= sum(info)
    print(f"다합치면 {sum_all}")
add(1,2,897,123,4345)

## 키워드 가변 매개 변수 예제 1. 
def print_info(**kwargs) :
    for key, value in kwargs.items() :
        print(f"key : {key} \t value : {value}")



# itesm() : 딕셔너리의 모든 키-값 쌍을 튜플 형태로 반환 
# 반환되는 객체는 dict_item 라는 이터러블 타입        

print_info(name="오애순", age=25, city="제주")
print_info(name="아이유", age=30, city="서울")

## 키워드 가변 매개 변수 예제 2. : 기본값과 함께 사용 

def greet_user(greeting="안녕하세요", **kwargs):
    print(greeting)
    for key, value in kwargs.items() :
        print(f"key : {key} \t value : {value}")

# 함수 호출
greet_user(name="박보검", age=30)
greet_user("환영합니다!", name="박영범", hobby="영화보기")

## 키워드 가변 매개 변수 예제 3. :  함수 내부에서 딕셔너리로 활용 
def calculate_total_price(**kwargs) :
    total = 0
    for item, price in kwargs.items() :
        total += price
        print(f"{item} : {price}원")
    print(f"총합 : {total}원")

# 함수 호출
calculate_total_price(apple=1000, banana=2000, orange=1500)

## ## 키워드 가변 매개 변수 예제 4. :  다른 매개 변수와 조합 
## 필수 매개 변수(usrname)와 키워드 가변 매개 변수를 함께 사용 

def user_profile(username, **kwargs) :
    print(f"사용자 이름 : {username}")
    for key, var in kwargs.items():
        print(f"{key}:{var}")

# 함수 호출
user_profile("홍길동", age=25, city="서울", hobby="축구")

## 키워드 가변 매개 변수 예제 5. : *args와 함께 사용 
## 위치 가변 매개 변수(*args)와 키워드 가변 매개변수(**kwargs)를 조합하여 다양한 형태의 입력을 처리 가능 
## *args는 항상 **kwargs보다 앞에 와야한다. 
def mixed_arguments(*args, **kwargs) :
    print("위치 인자:", args, type(args))
    print("키워드 인자", kwargs, type(kwargs))

# 함수 호출
mixed_arguments(1, 2, 3, name="박보검", age=30)

## 키워드 가변 매개 변수 예제 6. 다른 함수로 키워드 인자 전달(unpacking)


## display_info는 3 개의 고정된 키워드 인자를 받는다. 
## 딕셔너리(data)를 **를 사용해서 언패킹하여 전달할 수 있다. 
def display_info(name, age, city):
    print(f"이름: {name}, 나이: {age}, 도시: {city}")


 # 딕셔너리를 언패킹(Unpacking)하여 전달
 # 딕셔너리의 키-값 쌍이 각 함수의 매개 변수 이름과 값에 매핑된다. 

# 람다함수
# 일반 함수 정의 방식
def add(a, b):
    return a + b

# 람다 함수 정의 방식
print((lambda a , b : a + b)(3,4))

add_lambda = lambda a, b : a + b 


## 사전 정의 없이 즉석에서 사용이 가능하다. 
print(add_lambda(10,20))

# map()
##  map() 예제 1. 사용자 정의 함수를 활용한 예제 

# 숫자를 두 배로 만드는 함수 선언 
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

double_numbers = list(map(double, numbers))
print(double_numbers)

## 람다 함수 예제 1.  : 리스트와 함께 사용하는 람다 함수 
## map 함수와 함께 사용 

numbers = [1, 2, 3, 4, 5]

# 람다 함수를 사용하여 각 숫자의 제곱 계산
var_numbers = list(map(lambda i : i **2,numbers))
print(var_numbers)

## 람다 함수 예제 2 : 다중 iterable 사용 예제 

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 두 리스트의 요소를 더함
sum_list = list(map(lambda x,y : x + y,list1,list2))
print(sum_list)

# filter()
## 람다 함수 예제 3. : filter() 와 함께 사용하는 람다 함수 

# 짝수 필터링 
numbers = [1, 2, 3, 4, 5]
even_number = list(filter(lambda x : x % 2 == 0, numbers))

print(even_number)

## 람다 함수 예제 4. : filter() 와 함께 사용하는 람다 함수 

# 문자열 길이 조건 필터링 
words = ["apple", "banana", "kiwi", "pear"] 

# 문자열 길이가 5 이상인 단어만 추출
len_words = list(filter(lambda x : len(x) >= 5, words))
print(len_words)

## 람다 함수 예제 5. 조건부 표현식과 함께 사용
# 두 숫자 중 더 큰 값을 반환하는 간단한 함수 

max_min = lambda a, b: a if a > b else b
# print(type(max_min))
print(max_min(10, 20))  # 출력: 20

## 9.4 람다와 reduce 를 활용한 누적 계산 

## reduce는 리스트의 모든 요소를 누적하여 하나의 값으로 줄이는데 사용 
## functools 모듈을 임포트해야 한다. 
from functools import reduce

numbers = [1, 2, 3, 4, 5]
# iterable 객체의 첫번째 두개의 요소를 x, y 에 대입한다. 
# 이 결과값은 다음 단계에서 "누적값(accumulator)"로 사용 
# 이전 단계에서 계산된 누적값과 다음 요소를 fuction에 전달하여 다시 계산한다. 
# x+y가 x가 된다 그렇게 계속해서 누적해서 저장한다
product = reduce(lambda x, y : x * y, numbers)
print(product)

# 재귀함수
## 재귀 함수 예제 1: 리스트의 합 구하기 
def list_sum(lst):
    if not lst:
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4, 5]))  # 출력: 15