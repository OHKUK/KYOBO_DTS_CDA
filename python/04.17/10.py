# 예외처리
## try-except 예제 1 : ZeroDivisonError 처리 
# 0으로 나눌 때 발생하는 오류를 처리하는 방법 
try:
    result = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")

print("Good job")

#### tryp-excpet 예제 2 : IndexError 처리 
#### 리스트에서 잘못된 인덱스를 참조했을 때 발생하는 오류를 처리
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("잘못된 인덱스입니다. 인덱스 범위를 확인하세요.")

print("Good job")

#### try-excpet 예제 3 : KeyError 처리 
#### 딕셔너리에 존재하지 않는 키를 참조했을 때 발생하는 오류를 처리 
try:
    my_dict = {"apple": 5000, "banana": 4000}
    print(my_dict["tomato"])
except KeyError:
    print("키가 존재하지 않습니다! 딕셔너리를 확인하세요.")

## try-excpet 예제 4 : FileNotFound 처리 
# 존재하지 않는 파일을 열려고 할 때 발생하는 오류를 처리합니다.
try:
    with open('DoNotExist.csv') as file:
        data = file.read()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다. 파일 경로를 확인하세요.")

## try-excpet 예제 5 : 여러 예외 처리 
# 여러 종류의 예외를 가각 다르게 처리할 수 있다. 
# 입력값이 숫자가 아니면: 숫자를 입력해야 합니다. 
# 입력값이 "0"이면 : 0으로 나눌 수 없습니다. 

try:
    value = int(input("숫자를 입력하세요: "))
    result = 10 / value
except ValueError:
    print("숫자를 입력해야 합니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과는 {result}입니다.")            ## 정상적인 실행 결과 
finally:
    print("프로그램 종료")


#### try-except-as 예제 1 : 기본 사용 
try:
    result = 10 / 0  # ZeroDivisionError 발생
except ZeroDivisionError as e :
    print(f"Error occurred: {e}")

#### try-except-as 예제 2 : 특정 예외 처리 
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError as e:
    print(f"Invalid input! Error: {e}")
except ZeroDivisionError as e:
    print(f"You cannot divide by zero! Error: {e}")

#### try-except-as 예제 3 : 여러 예외를 한 번에 처리
#### 하나의 except 블록에서 여러 예외를 처리하려면 튜플을 사용할 수 있다. 
try:
    result = 10 / int("abc")
except (ValueError, ZeroDivisionError) as e:
    print(f"Handled error: {e}")

#### try-except-as 예제 4 : 모든 예외 처리 
#### 특정 예외 유형을 지정하지 않으면, 모든 종류의 예외를 처리할 수 있다. 
try:
    result = 10 / int("abc")  # ValueError 발생
except Exception as e:          
    print(f"An error occurred: {e}")

#### try-except-else 예제 1 : 기본 사용법 

try:
    number = int(input("숫자를 입력하세요: "))       
except ValueError:
    print("유효하지 않은 숫자입니다.")          
else:
    print(f"입력한 숫자는 {number}입니다.")     

## try-except-else 예제 32 : 나눗셈 계산기 
try:
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    result = num1 / num2  
except ValueError:
    print("숫자를 올바르게 입력해주세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"나눗셈 결과: {result}")

##  try-except-finally 예제 1 : 기본 사용 
## 오류 발생 

print("오류 발생")
try:
    result = 10 / 0  # ZeroDivisionError 발생
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
finally:
    print("Execution complete.")

print("정상 실행")
#### 정상 실행 
try:
    result = 10 / 2  # 정상 실행
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
finally:
    print("Execution complete.")

# raise

## raise 예제 1: 기본 사용법 
# raise 키워드를 사용하며 Exception 을 발생
x = -1
if x < 0:
    raise Exception("x는 음수일 수 없습니다.")

print(x) ## 오류가 발생하고 프로그램이 중단되기 때문에 실행되지 않는다. 

#### raise 예제 2 : 특정 예외 발생 
#### isinstance() : 객체가 특정 클래스(또는 자료형)의 인스턴스인지 확인할 때 사용하는 내장 함수 
#### 구문: isinstance(object, classinfo)
####    - object: 검사 대상 객체 
####    - classinfo: 클래스 또는 자료형(타입). 튜플의 형태로 여러 클래스나 자료형을 전달할 수 있다. 

#### x = 10
#### print(isinstance(x, int))  # True
#### print(isinstance(x, float))  # False

x = "hello"
if not isinstance(x, int):
    raise TypeError("x는 정수여야 합니다.")

## raise 예제 3 : try-except 와 함께 사용 
# try-except 블록과 함께 사용하여 발생한 오류를 처리한다. 
try:
    x = int(input("숫자를 입력하세요: "))
    if x < 0:
        raise ValueError("음수는 허용되지 않습니다.")
except ValueError as e:
    print(f"오류 발생: {e}")
