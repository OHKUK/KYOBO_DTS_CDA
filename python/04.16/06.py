# if 문
### 조건에 맞지 않을 때 
menu = "김밥"
if menu == "피자" :
    print("도미노피자로 가자")
elif menu == "햄버거" :
    print("버거킹으로 가자")
elif menu == "마라탕" :
    print("신촌마라탕으로 가자")
else :
    print("김밥천국으로 가자")

## 리스트에서 특정 값 찾기 
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits :
    print("바나나 있어요")

## 논리연산자를 활용해서 

# or : 둘 중 하나라도 참일 경우 True 
# and : 둘다 참일 경우 True요?
# 0 ~ 12 면 good morning
# 13 ~ 18 : good afternoon
# 18 ~ good evening
hour = int(input("지금 시간은 몇시 인가요?"))
if hour > 0 and hour < 12 :
    print("good morning")
elif hour >= 12 and hour < 18 :
    print("good afternonn")
elif hour >= 18 and hour <= 24 :
    print("good evening")
else :
    print("잘못 입력했습니다.")

# for문
## 예제 1. 리스트 순회 -> 반복
for 변수 in [1,2,3,4,5] :
    print(변수, end=" ")

## 예제 2. 리스트 순회
fruits = ["apple", "banana", "cherry"]
for f in fruits :
    print(f)

## 예제 3. 문자열 순회 
word = "Python"
for char in word :
    print(char)

for i in "Hello" :
    print(i)

## 예제 4. range() 함수를 통해서 지정한 범위안에 연속한 정수 반환
for i in range(2,10,2) :
    print(i, end=" ")

## 예제 5. 중첩된 for문 
# for 문을 중첩하여 다차원 데이터 구조를 처리하거나 복잡한 작업을 수행 할 수 있다. 

matrix = [[1, 2], [3, 4], [5, 6]]
for i in matrix :
    for j in i :
        print(j, end=" ")

## 예제 5. enumerate() 함수와 함께 사용하기

fruits = ['apple', 'banana', 'cherry']
for index, value in enumerate(fruits) :
    print(index, value)

for index, value in enumerate("Python") :
    print(index,value)

    
## 예제 6. 딕셔너리 순회 

# 키와 값을 동시에 접근할 때 유용 
person = {"name": "Alice", "age": 25, "city": "Seoul"}

for key,value in person.items() :
    print(f"키는 : {key} 값은 : { value}")


## 연속된 숫자를 생성하는 while 구문 (1~10) 
number = 1 
while number <= 10 :
    print(number)
    number += 1

print("끝~!")

## 무한 루프 구문 생성하기  + break 활용하기 
# 조건을 할상 True 로 설정하면 무한 반복되는 구문을 생성
correct_password = "1"
while True :
    user_password = input("0~9사이의 숫자를 입력하세요 : ")
    if user_password == correct_password :
        print("[접근허용] 입장하세요")
        break
    else :
        print("[접근불가] 비밀번호가 틀렸습니다.")
print("완료")

## 무한 루프 구문 생성하기 + continue 활용하기 

print("1부터 10사이의 숫자 중 짝수만 출력하세요. ")
number = 0
while True :
    number += 1
    if number > 10 :
        break
    elif number % 2 != 0 :
        continue
    print(f"짝수 : {number}")
print("종료")

## 리스트 내포를 사용하지 않고 작성하기 
student = [ 1, 2, 3, 4, 5]
print(student)
for i in range(5) :
    student[i] += 100
print(student)


# 위 구문을 한 줄로 작성하는 것을 리스트 내포(comprehension, 이해)
# 반복문과 조건문을 리스트에 포함해, 리스트를 간단히 생성할 수 있다. 

# 리스트 내포 활용하기 
student = [ 1, 2, 3, 4, 5]
학생 = [ i + 100 for i in student]
print(학생)

## 리스트 내포 예제 1. 숫자 리스트 생성 
# 0~10 까지 숫자 리스트 생성
number = [ i for i in range(11)]
print(number)

## 리스트 내포 예제 2. 제곱 값 계산 

numbers = [1, 2, 3, 4, 5]
var = [ numbers[i]**2 for i in range(5)  ]
print(var)

## 리스트 내포 예제 3.  항목의 글자수를 확인

actor = ["Timothy Chalamet", "Louis Partridge", "Robert Pattinson"]
len_actor = [ len(i) for i in actor]
print(len_actor)

## 리스트 내포 예제 4. if-else 조건 사용 1 ~ 10 사이의 숫자 짝수/홀수로 리스트 저장하기
labels = ["짝수" if i % 2 == 0 else "홀수" for i in range(1,11)]
print(labels)

## 리스트 내포 활용 예제 1.  짝수만 추출하기 

numbers = [ 1, 2, 3, 4, 5 ]
labels = [  numbers[i]  for i in range(len(numbers))if numbers[i] % 2 == 0 ]
print(labels)