# 자료구조_리스트
## list 생성

학생 = ["양관식", "오애순", "학씨"]
print(학생)

학생 = ["양금명", "박영범", "박충섭"]
print(학생)

# index()
print(학생.index("박충섭"))
print(학생[2])

## list 항목 추가
print(학생)

## append() 붙여넣기 맨뒤에 삽입
학생.append("양은명")
print(학생)

## insert() 삽입 바뀌는건 아니고 사이에 삽입
학생.insert(2, '부현숙')
print(학생)

## list 특정 인덱스의 값을 삭제하고 반환
## pop() 마지막 인덱스 삭제하기전에 문자열로 반환하고 삭제 지정안하면 마지막 지정하면 지정한 위치
print(학생)
반장 = 학생.pop()
부반장 = 학생.pop(2)
print(학생)
print(반장)
print(부반장)

## list 특정 값 삭제 
## remove()
print(학생)
학생.remove("부현숙")
print(학생)

# list 모든 값 삭제 
학생 = ["양관식", "오애순", "학씨"]
print(학생)
학생.clear()
print(학생)

## list 특정 인덱스나 범위 삭제 
학생 = ["양관식", "오애순", "학씨"]
del 학생[2:] #슬라이싱과 같음
print(학생)

## 중복값 확인
학생 = ["양금명", "박영범", "박충섭"]
학생.append("양금명")
학생.append("양금명")
print(학생)
print("양금명 :",학생.count("양금명"))

## sort() 정렬하기 
number = [45, 119, 87, 24, 17, 75]


## 오른 차순 정렬 
print(number)
number.sort()
print(number)

## 내림 차순 정렬 
number.sort(reverse=True)
print(number)

## reverse() 현재상태의 역순
number.reverse()
print(number)

## 정렬과 함께 리스트의 내용도 같이 변경된다. 리스트가 변경되길 원치 않으면 sorted() 함수 사용 
number = [45, 119, 87, 24, 17, 75]
now_number = sorted(number)  #now_numboer에게 정렬상태가 저장
print(number)
print(sorted(number))
print(now_number)

## list 내부 연산 

x = 10 
y = 15 

result = [x+y, x-y, x*y, x/y]
print(result)


## 리스트의 특정 요소 업데이트하기 
fruits = ["apple", "banana", "cherry", "grape"]

fruits[3] = "strawberry"
print(fruits)

# 역순도 가능
fruits[-1] = "melon"
print(fruits)

## 리스트 인덱싱 예제 
fruits = ["apple", "banana", "cherry", "date"]

## 첫번째 요소 출력 
print(fruits[0])
## 마지막 요소 출력 
print(fruits[-1])
## 리스트 마지막 요소 출력 
print(fruits[3])

number = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[0:4])
print(number[2:8:3])
print(number[-3::-1])
print(number[-6::-2])
print(number[-6:9:])

## 슬라이싱 범위를 벗어난 경우 
number = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 슬라이싱은 리스트의 특정 부분을 추출하려는 시도
# 리스트 범위가 벗어나더라도 파이썬이 자동으로 유효한 범위로 조정 
print(number[1:100])
print(number[-100:100])

## 인덱싱은 특정 위치의 요소에 직접 접근하려는 시도 
# 유효한 범위를 벗어나면 IndexError 발생 범위안에 값이 아니면 에러가 난다 
#print(number[100])

# 리스트 확장
number = [45, 119, 87, 24, 17, 75]
drama = ["폭싹 속았수다.", 16, True, ["양금명", "박영범", "박충섭"] , [ "양관식", "오애순", "학씨"]]
menu = ["자장면","부대찌개","햄버거","떡볶이"]

##  리스트의 항목을 개별적으로 추가
## extend()
menu.extend(number)
print(menu)

color = ["빨강", "주황", "노랑"]

## 리스트 전체를 하나의 항목으로 추가 
color.append(number)
print(color)

# 중첩 리스트
nested_list = [[1, 2], 
               [3, [4, 5]], 
               [6]]

# 첫 번째 중첩 리스트 접근
print(nested_list[0])
# 중첩된 요소 접근 (두 번째 내부 리스트의 첫 번째 값)
print(nested_list[1][0])

# 더 깊은 중첩된 요소 접근 (네 번째 값)
print(nested_list[1][1][0])


# 가변 객체의 메모리 참조 동일 메모리에 저장되기때문에(심볼릭 링크같은것)
a = [1, 2]
b = a
b.append(3)
print(a)
print(b)

# 독립적인 복사본 생성하기 (copy())
print(a)
c = a.copy()
print(c)
c.append(4)
print(a)
print(c)
