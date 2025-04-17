# 입출력
# 표준 입력 받기 
name = input("이름이 무엇입니까? ")
print("안녕하세요 " + name + "님!")

## 데이터 타입 변환 
# 입력값은 기본적으로 문자열(string) 로 반환되므로, 숫자나 다른 타입으로 변환하려면 추가 작업이 필요하다. 
age = int(input("나이는?"))
print("10년 뒤에는", age + 10, "살입니다." )
#### print() 함수 예제 1.  sep, end 응용 
print("Hello", "World", sep=", ", end="!")
print("Python")
#### split() 예제 1. 기본 사용법 
text = "Hello World Python"
result = text.split()
print(result)

#### split() 예제 2. 특정 구분자를 사용하여 나누기 
#### 구분자를 지정하면 해당 구분자를 기준으로 문자열을 나눈다. 
text = "apple,banana,cherry"
text = "apple,banana,cherry"
result = text.split(",")
print(result)  # 출력: ['apple', 'banana', 'cherry']

#### split() 활용 1.  사용자 입력을 받은 값을 처리할 때 
values = input("Enter numbers separated by spaces: ").split()
print("Values:", values)
print(type(values))     ## 사용자에게 입력받은 정보는 split() 매서드에 의해 list로 반환된다. 
print(type(values[0]))  ## values list 의 각 요소는 str 타입

#### split() 활용 2 .  map() 함께 사용하기 
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
                    # 사용자 입력 받은 내용을 str 을 int 로 변환한 결과들을 list 형태로 반환 
print(numbers)
print(type(numbers))
print(type(numbers[0]))
print("Sum:", sum(numbers))

#### file 키워드 예제 1.  기본 사용법 
#### print() 함수의 file 키워드는 파일 객체를 지정하여 출력 결과를 해당 파일에 기록한다. 
#### 파일 열기
file = open("output.txt", "w")

print("Hello, Python!", file=file)
print("This is a test.", file=file)

#### 파일 닫기 열었으면 닫아야지
file.close()

#### file 키워드 예제 2. 여러 줄 저장하기 
#### 반복문과 함께  file 키워드를 사용하여 여러 줄을 파일에 저장할 수 있다.  자동 닫기

lines = ["Line 1", "Line 2", "Line 3"]

with open('output.txt','w') as file:
    for line in lines:
        print(line,  file=file)

#### file 키워드 예제 3. sys.stdout을 변경하여 출력 리다이렉션 
#### 모든 출력이 파일로 리디렉션 되도록 표준 출력 스트림(sys.stout)을 변경할 수 있다. 
import sys

original_stdout = sys.stdout  # 기존 stdout 저장

with open("output.txt", "w") as file:
    sys.stdout = file                              # stdout을 파일로 변경
    print("Redirecting output to a file.")
    print("All print statements will go to the file.")
    sys.stdout = original_stdout                   # stdout 복원

print("This message will appear on the console.")  # 콘솔로 출력

## ljust() 예제 1.   기본 공백으로 채우기

text = "Python"   # 6글자 
print(text.ljust(10))  

## ljust() 예제 2. 특정 문자로 채우기
print(text.ljust(10, '*'))  

## rjust() 예제 1. 기본 공백으로 채우기
text = "Python"
print(text.rjust(10))  

## rjust() 예제 2.  특정 문자로 채우기

print(text.rjust(10, '#')) 

## ljust()와 rjust() 활용 예제 1. 테이블 형식 데이터 정렬
# ljust()와 rjust()를 사용하여 데이터를 보기 좋게 정렬한다. 

data = {"Name": "Alice", "Age": "25", "Country": "USA"}

for key, value in data.items():
    print(key.ljust(10), value.rjust(10))
    print(value.rjust(10),key.ljust(10))

#### zfile() 예제 1. 기본 사용법 
#### 실습 전 자겅ㅂ 디렉토리에 "file1.txt, file2.txt " 생성 후 작업 할 것!
import zipfile

#### ZIP 파일 생성
with zipfile.ZipFile("example.zip", "w") as zf:
    zf.write("file1.txt")                     # 파일 추가  (file1.txt + file2.txt 로 example.zip 파일 생성 )
    zf.write("file2.txt")

# ZIP 파일 읽기
with zipfile.ZipFile("example.zip", "r") as zf:
    print(zf.namelist())                     # ZIP 파일 내의 파일 목록 출력
    print(type(zf.namelist()))               # 목록을 list로 출력 

# ZIP 파일 해제 
# import zipfile
with zipfile.ZipFile('example.zip','r') as zf:
    zf.extractall('output_folder') # 모든 파일을 지정된 폴더에 해제

#### format() 예제 6 : 포맷 지정자(Format Specifiers) 
#### format() 메서드는 문자열 내에서 값을 정렬하거나 숫자 형식을 지정하는 데 유용한 포맷 지정자를 지원한다. 
#### 1.  정렬 
#### - :<     : 왼쪽 정렬 
#### - :>     : 오른쪽 정렬 
#### - :^     : 가운데 정렬 

#### 정렬 예제
print("{:<10}".format("left"))   
print("{:>10}".format("right"))  
print("{:^10}".format("center")) 


## format() 활용 1 : 테이블 정렬 
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# 테이블 형식으로 출력
for person in data:
    print("{:<10} {:>3}".format(person["name"], person["age"]))

## format() 활용 2 : 금액 표시 
sales = 1234567.89

# 금액 형식화
formatted_sales = "{:,.2f}".format(sales)
print(f"Total Sales: ${formatted_sales}")

#### 텍스트 파일 열기/닫기 예제 1. 파일 읽기
f = open('file1.txt','r')

content = f.read()
print(content)
f.close()

#### 텍스트 파일 열기/닫기 예제  2. 텍스트 파일 쓰기 
f = open('file2.txt', 'w')

f.write('Hello, python!')

f.close()

#### 텍스트 파일 열기/닫기 예제  3. with 문을 사용한 파일 처리 
#### with문을 사용하면 파일을 자동으로 닫아주므로 더 안전하고 간결한 코드를 작성할 수 있다. 
#### 텍스트 파일 읽기
with open("file1.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)


## write() 예제 1: 텍스트 파일 쓰기 / 문자 수 반환 확인 
with open("file1.txt", "w") as file:
    chars_written = file.write("Hello, Python!") ## write() 메서드 반환값은 기록된 문자수 "14" 
    print(f"{chars_written} characters written.")  # 출력: 13 characters written


## write() 예제 2 : 여러 줄 쓰기  
# "w", "a" 모드로 열면 파일이 없을 경우 자동으로 생성 
with open("example.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

## write() 예제 3 : 데이터 추가(Append)
# 기존 파일에 내용 추가
with open("example.txt", "a") as file:
    file.write("\nThis is an appended line.")  ## 출력앞에 "\n"을 넣어서 한 줄 띄어쓰기 
## write() 예제 4 : 읽기 / 쓰기 모드 사용(r+)

# 기존 내용을 덮어쓰기
# "Overwrite" 문자열이 내용의 첫부분을 덮어쓰게 된다. 
with open("example.txt", "r+") as file:
    content = file.read()
    print(content)
    file.write("Overwrite")                             

#### write() 주의 사항 1 : write()는 문자열만 허용된다. 숫자나 다른 데이터 타입은 문자열로 변환 
with open("example.txt", "w") as file:
    file.write(str(123))  # 숫자를 문자열로 변환하여 기록

#### write() 주의 사항 2 :  메서드는 데이터를 버퍼에 저장하므로, 
#### 변경 사항을 즉시 반영하려면 Flush() 를 호출하거나 파일을 닫아야 한다.
with open("example.txt", "w") as file:
    file.write("Buffered write")
    file.flush()  # 즉시 디스크에 기록 버퍼에 안가고

#### read() 예제 1 : 특정 사이즈(바이트)만 읽기

with open("example.txt", "r") as file:
    content = file.read(5)  # 처음 5바이트5만 읽기     
    print(content)  # 출력 : Line ' 

#### readline() 예제 1. 
with open("example.txt", "r") as file:
    line1 = file.readline()  # 첫 번째 줄 읽기
    line2 = file.readline()  # 두 번째 줄 읽기
    print(line1, end="")     # 개행 문자 제거 후 출력
    print(line2, end="")

## readline() 예제 2. 
## 반복문으로 모든 줄 읽기 
with open("example.txt", "r") as file:
    while line := file.readline():    # 빈 내용이 입력되면 False 평가  / 내용이 할당되면 True
        print(line, end="")


        ## := (Walrus operator, 바다코끼리 연산자 )  : 할당과 반환을 동시에 진행 
#### readlines() 예제 1. 
with open("example.txt", "r") as file:
    lines = file.readlines()  # 모든 줄을 리스트로 반환
    print(lines)

#### readlines() 예제 2.  리스트를 활용한 반복문 
with open("example.txt", "r") as file:
    for line in file.readlines():
        print(line.strip())  # 개행 문자 제거 후 출력

## strip() 예제 1 : 공백 제거 
# 문자열의 시작과 끝에 있는 모든 공백을 제거 
text = "   Hello, World!   "
print(text.strip())  # 결과: "Hello, World!"

## strip() 예제 2 : 특정 문자 제거 
# 문자열의 시작과 끝에 지정된 문자를 제거한다. 
# 일치하는 문자열이 없는경우 원래 문자열이 그대로 반환된다. 
text = "***Hello, World!***"
print(text.strip("*"))  # 결과: "Hello, World!"

text = "**!!Python!!**"
print(text.strip("*!"))  # 결과: "Python

## strip() 예제 3: 왼쪽 또는 오른쪽만 제거 (lstrip, rstrip)
# 왼쪽만 제거 
text = "  Hello  "
print(text.lstrip())  # 결과: "Hello"

# 오른쪽만 제거 
text = "  Hello  "
print(text.rstrip())  # 결과: "Hello"

## strip() 예제 4: 원본 문자열 유지 
# 원본 문자열을 변경하지 않고 새로운 문자열을 반환한다. 

text = "    Hello     "
stripped_text = text.strip()
print(text)  # 결과: " Hello "
print(stripped_text)  # 결과: "Hello"

##  strip() 활용 1 : 사용자 입력 처리 
# 표준 입력뒤에 공백이 반복되는 경우 제거 
user_input = input("Enter your name: ").strip()
print(f"{user_input}!, Hello")

## strip() 활용 2 : 파일 경로 처리 
# 절대 경로를 상대 경로로 표현 
path = "/home/user/docs"
clean_path = path.lstrip("/")
print(clean_path)  # 결과: "home/user/docs"

## pickle 예제 1. 직렬화 (pickling) 

import pickle

data = {"name": "Alice", "age": 25, "city": "New York"}

# 파일에 저장
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  # 직렬화하여 파일에 저장

## pickle 예제 2.  역직렬화 (unpickling)
import pickle

# 파일에서 읽기
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)  # 역직렬화하여 객체 복원

print(loaded_data)  # 출력: {'name': 'Alice', 'age': 25, 'city': 'New York'}


## pickle 예제 3. 사용자 정의 클래스 객체 직렬화 

import pickle

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 22)

# 객체를 파일에 저장
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)

# 파일에서 객체 읽기
with open("student.pkl", "rb") as file:
    loaded_student = pickle.load(file)

print(loaded_student.name)  # 출력: Alice
print(loaded_student.age)   # 출력: 22

## pickle 예제  4. pickle을 사용한 데이터 입력 및 저장 
# 사용자 입력 데이터 저장하기 
import pickle

data = []
num_entries = int(input("Enter the number of entries: "))
for i in range(num_entries):
    entry = input(f"Enter entry {i+1}: ")
    data.append(entry)

# 데이터를 파일에 저장
with open("user_data.pkl", "wb") as file:
    pickle.dump(data, file)       ## data list 를 pickle 모듈을 사용해서 파일에 저장 

print("Data saved successfully!")