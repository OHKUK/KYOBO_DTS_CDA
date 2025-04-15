# print()
print("Hello, python")
print("즐거운 파이썬 프로그램 시간")

## 여러 단어를 조합해서 출력하기 
print("파이썬","자바","C++")
print("파이썬",",""자바",",""c++")
print("파이썬"+"자바"+"C++")

# 여러 라인 출력하기 
print("여러분")
print("힘드시죠?")
print("네 힘들어요")

# 한 줄에 출력하기 
print("여러분", end=" ")
print("힘드시죠", end=" ")
print("네 힘들어요", end=" ")

# comment 

# 이 프로그램은 간단한 인사말울 출력한다. 

name = "Jenny" # 주석이구나
print(name)    
# print("Hello world") . 
print("~!!")    

'''
이 프로그램은 두 숫자를 더하는 예제입니다.
사용자는 숫자를 입력하고 결과를 확인할 수 있습니다.
'''

# x = int(input("첫 번째 숫자를 입력하세요: "))
# y = int(input("두 번째 숫자를 입력하세요: "))


# print(f"결과: {x + y}")

# help()
#help(print)

# 자료형
# integer
print(5)
print(type(5))
print("5")
print(type("5"))
print(-10)
print(type(-10))

# float
print(3.14)
print(type(3.14))

## print() 내에서 산술 연산식 만들기
print(3+10)
print("3+10")
print(15-3)
print(3*9)
print(2**3)
print(9/3)
print(8/3)
print(8//3)
print(16&3)

# String
print("Hello, python")
print(type("Hello, python"))

#bool
print(type(True))
print(type(False))

# print() 내에서 평가문 판단
print(5 < 10)
print(5 > 10)
print(not True)
print(not False)
print(10 == 10)
print(10 != 10)

# 변수
## 변수 이름 예제 
my_variable = 10 
variabel = 20 
variable = 10 
# 1variable = 20 

my_variable_name = "Python"
my_error_code = 404
# my.error.code = 500

name = "Alice"
Name = "Bob"
print(name)
print(Name)

#type()
## integer
my_int = 100
print(my_int,type(my_int))

## float
pi = 3.14
print(pi, type(pi))

## string
home = "jeju"
print(home, type(home))

## bool 
my_bool = True
print(my_bool,type(my_bool))
print(True+True+True+False+True)

## 예약어(keywords) 확인 
#help("keywords")
#for = 12

# 문자열과 변수 함께 출력
name = "김철수"
hobby = "영화 보기"
age = 24
print("이름은" , name , "취미는" , hobby,"나이는" , age , "입니다")
# 이름은 김철수 취미는 영화 보기 나이는 24 입니다

#print("a"+"b"+"c")
#이름은 김철수 취미는 영화 보기 나이는 24 입니다
print("이름은 " + name + " 취미는 " + hobby + " 나이는 " + str(age) + "살입니다.")

#형변환
print("나이는 " + str(3))

print(int(3.14))   ## 3으로 표시 
#str() 형식
print(str(25) + "살 입니다." )
print(str(30.8) + "살 입니다.")

#print(int("123.4")) -> 숫자형끼리는 문제없지만 문자열은 변환은 안될수 있음
print(int(123.4))
# 실수형태의 문자열은 float()로 형변환이 가능하다. 
print(float("123.4")) # 실수형이라면  변환 가능

#eval()
print("1 + 2 + 3")
print(1 + 2 + 3)

# 문자열로 받아서 파싱을 통해 표현식으로 실행하고 결과를 반환한다. 
eval("1 + 2 + 3")
x = 10
y = 15
print("x + y")
z = eval("x + y")
print(z)