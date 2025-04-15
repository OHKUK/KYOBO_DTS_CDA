# 자료구조 튜플
## 튜플 생성하기  
서울시 = ("서대문구", "동작구", "마포구")

print(서울시[0])
print(서울시)

## 여러 개의 값을 가지는 변수를 통해 튜플 생성 
t1 = 'red', 5, 'apple'
print(t1, type(t1))

## 튜플을 통해 변수 지정 
name = "오애순"
age = 17 
home = "제주"
print(name, age, home)

## 변수를 여러 줄에 따로 정의 하는 대신  튜플의 형태로 한 줄에 여러 변수의 값을 정의 할 수 있다.
test = (name, age, home) = ('김민규', 16, '서울')
print(test,type(test))

## tuple() 함수를 통해서 문자열로 튜플 생성하기 
t2 = tuple("abcdefg")
print(t2)
## 리스트로
t3 = list("abcder")
print(t3)

## 튜플 예제 (출발지IP , 도착지IP)

(출발지_IP, 도착지_IP) = ("192.168.10.100", "192.168.10.101")
print(f"출발지 IP: {출발지_IP} ---> 도착지 IP{도착지_IP}")

(출발지_IP, 도착지_IP) = (도착지_IP, 출발지_IP)
print(f"출발지 IP: {출발지_IP} ---> 도착지 IP{도착지_IP}")

## 튜플 인덱싱과 슬라이싱 

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[-1])
print(numbers[-1:-4:-1])

## 튜플 element 추가 할수가 없따!@@@@@@@@!
#numbers.append(10)

## 튜플 element 변경 할수가 없따!@@@@@@@@@!
# numbers[3] = 30

## 변수 할당시 튜플 element 참조 
(a, b) = [1, 2]
print(a, b)
# 수가 안맞아도 할수가 없따!!!@@
# (c, d) = (1,2,3,)

## 원소가 하나인 경우에는 문자열로 저장 변수로 저장
t1 = ('one')
print(t1, type(t1))
## 튜플로 인식될 수 있도록 ","를 뒤에 붙여준다. 
t2 = ('one',)
print(t2,type(t2))

## 여러 개 튜플을 하나로 통합 
color = ('red', 'blue', 'green')
numbers = (1, 2, 3)

# 새로 지정해줘야한다
t3 = color + numbers
print(t3,type(t3))

# zip()
## zip 예제 1 : 기본 사용법
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
 
# zip 객체 생성
zipped = zip(numbers, letters)
print(zipped)

# zip 객체를 리스트로 변환하여 출력
print(list(zipped))

## zip 예제 2: 여러 iterable 병렬처리
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
symbols = ['!', '@', '#']

result = zip(numbers, letters, symbols)
print(result)
print(list(result))

## zip 예제 4 : unzip 데이터 분리 
# "*"는 iterable 객체의 요소를 풀어서 개별 인자로 전달 

pairs = [(1, 'A'), (2, 'B'), (3, 'C')]

# zip을 사용해 분리하기
numbers, letters = zip(*pairs)
print(numbers, letters)
print(pairs)
