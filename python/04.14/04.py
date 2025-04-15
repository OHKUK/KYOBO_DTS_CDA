# 문자열
s1 = '나는 김철수 입니다.' 


s2 = "나는 이영희입니다."

s3 = """
나는 김철수 친구,
이영희입니다.
"""  
print(s1)
print(s2)
print(s3)

## strings immutable 확인 
str1 = "python"
print(type(str1))
#str1[2] = "T"

# 문자열 연산 +
string1 = "Hello, "
string2 = "World!"
print(string1 + string2)

## 문자열과 숫자형의 연결
string1 = "Hello" + str(3)
print(string1)

# 문자열 반복
string = "Hello! " * 3
print(string)

# 문자열 길이 확인 
string = "Hello, World!"
print(len(string))

# 문자열 인덱싱 
string1 = "Hello, World!"
print(string1)
print(string1[12])
print(string1[-1])
print(string1[-6])

## 문자열 슬라이싱 예제 1
greet = "HelloWorld"

print(greet[:])
print(greet[5:])
print(greet[:-6])
print(greet[-9:])

## 문자열 슬라이싱 예제 2 
#string1 = "Python programming easy and fun"
greet="HelloWorld"
print(greet[::2])
print(greet[1:8:3])
print(greet[-1:-9:-2])
print(greet[::-1])


# 문자열 함수처리
# upper(), lower(), title()
kyobo = "Cloud Architecture DX Academy"

print(kyobo.lower())
print(kyobo.upper())
print(kyobo.title())

greet = "hello world"
print(greet.upper())
print(greet.title())

# islower(), isupper() 
kyobo = "Cloud Architecture DX Academy"
print(kyobo[0].islower())
print(kyobo[0].isupper())

# replace () 
kyobo = "Cloud Architecture DX Academy"
print(kyobo.replace("Architecture", "Infra"))
print(kyobo)

## 특정 객체에 포함된 메서드와 속성을 확인 하는 방법 
string1 = "Hello"
print(dir(string1))
print(hasattr(string1,"upper"))

# 문자열 위치 찾기
# find() 
kyobo = "Cloud Architecture DX Academy"
f1 = kyobo.find("t")
print(f1)

f2 = kyobo.find("t", f1 + 1)
print(f2)

f3 = kyobo.find("infra")
print(f3)                   # 존재 안하면 -1

# index() 

kyobo = "Cloud Architecture DX Academy"

print(kyobo)

a = kyobo.index("A")
print(a)

b = kyobo.index("A", a + 1)
print(b)

#print(kyobo.index("infra")) #  없으면 에러가 나온다