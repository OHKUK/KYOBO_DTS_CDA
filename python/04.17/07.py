# 함수
## 활용 1: 데이터 검증 함수

# 입력받은 email 주소가 유효한지 검증한다 .
def validate_email(email) :
    if "@" not in email or "." not in email:
        return False
    return True
email = "example@domain.com"
email = input("이메일 주소를 입력하세요")
if validate_email(email):
    print("유효한메일입니다.")
else:
    print("유효하지않은 메일입니다.") 

# 지역변수
#### 지역 변수 예제 1. 
def greet():
    massage = "안녕하세요"
    print("함수 내부 메세지 :",massage)

greet()
#print(massage) 정의 되어있지 않다고 에러
#### 함수 외부에서 지역 변수에 접근하려고 하면 에러 발생
#### 지역 변수 예제 2. 함수마다 같은 이름의 지역 변수
def func1():
    x =10
    print("func1의 x :",x)
def func2():
    x =20
    print("func1의 x :",x)

func1()  # 출력: func1의 x: 10
func2()  # 출력: func2의 x: 20
## 전역 변수 예제 1. 

message = "안녕하세요!"  # 전역 변수
def greet():
    print("함수내부:",message)
greet()
print("함수외부:",message)
#### 전역 변수 예제 2.  global 키워드 사용 안하면 에러나서 안된다~
count = 0  # 전역 변수
def increment():
    count += 1
    print(count)
increment()

#### 전역 변수 예제 3 : global 키워드 없이 수정 시 에러 발생 그래서 넣고하면 에러 안난다~

count = 0  # 전역 변수
def increment():
    global count
    count += 1
increment()
increment()
print("count:",count)

#### 전역 변수 예제 4.  동일한 이름의 지역 및 전역 변수 

x = '전역'
def myfunc():
    x ='지역'
    print('함수 내부:',x)
myfunc()
print('함수 외부:',x)


#### nonlocal 예제 1. 
x = "global"         ## 전역함수 

def outer():
    x = 'outer'
    print('내부 함수1:',x)
    
    def inner():
        nonlocal x
        print('내부내부 함수1:',x)
        x = 'inner'
        print('내부내부 함수2:',x)
    inner()
    print('내부 함수2:',x)
outer()
print('외부함수:',x)

#### nonlocal 예제 2.

def outer_function():
    x = 10                  
    def inner_function():
        nonlocal x         
        x += 5            
        print(x)            
    inner_function()
    print(x)        
    
outer_function()