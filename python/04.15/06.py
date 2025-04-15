# 제어문

# if문
# if 기본 예제 1 :
if 0 :
    print("거짓 입니다")
if "Hello" :
    print("참 입니다")

# 비교연산자
x = 10
y = 20
if x < y and x >= 5 :
    print("x는 y보다 작다")

## input() 함수를 통해서 사용자 입력 받기 
menu = input("오늘 점심메뉴는 뭐가 좋을까?")
print(menu)

## 조건문 예제 1 : 
pizza = input("선호하는 피자 브랜드를 넣어주세요: ")
if pizza == "도미노" :
    print("그럼 도미노 갈까?")

## 조건문 예제 2: 기본값이 문자열로 받는다고 한다다
number = int(input("숫자를 입력해주세요: "))
if number % 2 == 0 :
    print("짝수입니다.")
if number % 2 == 1 :
    print("홀수입니다.")

    ## 조건문 예제 3 : 중첩된 if 구문 
number = int(input("숫자를 입력해주세요: "))
if number >= 0 :
    if number % 2 == 0 :
        print("짝수입니다")
    else :
        print("홀수입니다")
else :
    print("음수를 입력했습니다.")


## 들여쓰기의 중요성 

menu = input("점심메뉴: ")                             
if menu == "pizza": 
    print("점심에 피자헛에 가자")
print("점심에 노모어피자에 가자")