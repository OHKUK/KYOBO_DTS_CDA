# 문자열
# 문자열 포맷팅
print("나는 %d살 입니다." % 20)

print("우리는 %s운영체제를 좋아합니다. " % "linux" )

print("우리는 %s 계열의 배포판인 %s 사용합니다. " % ("Redhat", "Rocky Linux"))  ## 입력값이 여러개 일 경우 


print("우리는 %s 계열의 배포판을 %d 개 알고 있습니다. " % ("Redhat", 3))  ## 입력값이 여러개 일 경우 

# format() 함수
print("나는 {} 살 입니다. ".format(20))
print("redhat 계열의 배포판은 {}와 {} 있습니다.  ".format("Fedora", "Rocky Linux"))


print("redhat 계열의 배포판은 {0}와 {1} 있습니다.  ".format("Fedora", "Rocky Linux"))
print("redhat 계열의 배포판은 {1}와 {0} 있습니다.  ".format("Fedora", "Rocky Linux"))

print("{season}에는 {flower}이 핍니다.".format(season="봄",flower="벗꽃"))
print("{season}에는 {flower}가 핍니다.".format(flower="능소화",season="여름"))

# f-string
home = "제주"
name = "오애순" 

print(f"나는 {name}이고, {home}에 삽니다. ")

age = 20
print(f"내이름은 {name}이고, 나이는{age}살이다. 사는곳은 {home}다")

# 이스캐이프
# print("폭싹
# 속았수다.")

print("폭싹 \n속았수다. ")

print('요즘 나의 최애 드라마는 "폭싹 속았수다." 입니다. ')
print("요즘 나의 최애 드라마는 '폭싹 속았수다.' 입니다. ")

print("요즘 나의 최애 드라마는 \"폭싹 속았수다.\" 입니다. ")

print("C:\\Users\\Daram\\Desktop")


## \r :  커서를 라인의 시작으로 이동 

print("Cloud architecture\rDX Academy")

## \b : 키보드의 백스페이스의 역할

print("Cloud architecture\b\bDX Academy")

## \t : 키보드의 tab 문자 입력 

print("Cloud architecturer\tDX Academy")
