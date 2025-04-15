#  딕셔너리
## 딕셔너리 예제 1 .  딕셔너리 생성하고 조회하기 
학생 = {3: "제니", 1: "리사", 4: "로제", 2: "지수"}
print(학생,type(학생))

## 디렉토리 조회하기 
print(학생[1])
print(학생[2])
print(학생[3])

## 딕셔너리 예제 2.   빈 디렉토리 생성하기 
empty_dir = { }
print(empty_dir)

## 딕셔너리 예제 3.  get() 함수 사용하기 
학생 = {1: "제니", 2: "리사", 3: "로제", 4: "지수"}

print(학생[4])
print(학생.get(4))

# get으로 하면 에러 안나 none 없다고 해 근데 none말고 지정할수 있어
print(학생.get(5))
print(학생.get(4, "정의되지 않은 키입니다."))
print(학생.get(5, "정의되지 않은 키입니다."))

## 딕셔너리 예제 4. key에 문자열 사용하기 

food = {"봄": "산채비빔밥", "여름": "냉면", "가을": "전어회", "겨울": "호빵"}
print(food["여름"])
print(food.get('봄'))

## 딕셔너리 예제 5. dict() 내장 함수를 사용해서 딕셔너리 생성 
person = dict(name="Alice", age=30, city="seoul")
print(person)
print(person["age"])

## 딕셔너리 예제 6.  리스트나 튜플을 이용해서 딕셔너리 생성
pairs = [("name", "Bob"), ("age", 25), ("city", "Busan")]
dict1 = dict(pairs)
print(dict1)
print(dict1['age'])

## 딕셔너리 예제 7. 딕셔너리 값 변경하기 
food = {"봄": "산채비빔밥", "여름": "냉면", "가을": "전어회", "겨울": "호빵"}

food["봄"] = "술"
print(food["봄"])
food["가을"] = "막걸리"
print(food["가을"])
food["환절기"] = "소주"
print(food)

## 딕셔너리 값 삭제하기 
del food["여름"]
print(food)

## 딕셔너리 예제 8. 다양한 메소드 적용하기 
학생 = { 1: "제니", 2: "로제", 3: "리사", 4: "지수"}

## 딕셔너리 값 출력하기 
print(학생)

## 딕셔너리 키만 출력 keys() 
print(학생.keys())

## 딕셔너리 값만 출력 values()
print(학생.values())
new_student = list(학생.values())
print(new_student,type(new_student))

## 딕셔너리 키와 값 모두 출력 items()
print(학생.items())
전학생 = list(학생.items())
print(전학생)
print(전학생[2][1])

## 딕셔너리 값을 한번에 삭제 
학생.clear()
print(학생)

## 딕셔너리 연습 1.  키와 값을 포함한 딕셔너리
fruit_prices = {"apple": 3.5, "banana": 2.0, "cherry": 5.0}

# 값 조회
print(fruit_prices["apple"])

# 값 수정
fruit_prices["apple"] = 5
print(fruit_prices["apple"])

# 새 키-값 추가
fruit_prices["durian"] = 10.5
print(fruit_prices["durian"])

# 키를 참조해서 요소 삭제
del fruit_prices["banana"]
print(fruit_prices)

## 딕셔너리 예제 9. 추가 메서드 사용하기 
fruit_prices = {"apple": 3.5, "banana": 2.0, "cherry": 5.0}

# get() 메서드로 값 가져오기 (기본값 설정 가능)
print(fruit_prices.get("melon", "not found"))

# update()로 여러 값 업데이트
fruit_prices.update({"apple": 4.5, "malon": 7.3})
print(fruit_prices)

# pop()으로 특정 키 제거 및 반환
remove_item = fruit_prices.pop("cherry")
print(fruit_prices)
print(remove_item)

## 딕셔너리 예제 10. 딕셔너리에 key 존재 확인 

dict1 = {'a': 'apple', 'b': 'banana' , 'c': 'cherry'}
print("a" in dict1)
print("d" in dict1)

## 딕셔너리 활용 2. : 리스트를 딕셔너리로 변환 

# zip() 함수는 여러 개의 순회 가능한(iterable) 객체(예: 리스트, 튜플, 문자열 등)를 인덱스별로 묶어서 
# 각 위치에 있는 요소들을 하나의 튜플로 만들어주는 내장 함수
keys = ["name", "age", "city"]
values = ["John", 25, "New York"]

zipped = zip(keys,values)
dict_zip = dict(zipped)
print(dict_zip)
print(dict_zip["name"])
print(dict_zip["city"])

## 딕셔너리 활용 3. : 중첩 딕셔너리 활용 
students = {
    "student1": {"name": "Alice", "age": 24},
    "student2": {"name": "Bob", "age": 22},
}

print(students["student1"]["name"])
print(students["student2"]["age"])
