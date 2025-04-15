# set()
## 셋 예제 1. 셋 정의하기 
## 중복 불허 
my_set = {1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9}
print(my_set,type(my_set))

## set() 활용하기 중복 없어 
food = ['밥','고추장','김','나물','당근','버섯','시금치']
비빔밥 = set(food)
print(비빔밥)

## 빈 셋 생성 
empty_set = set()
print(empty_set,type(empty_set))

## 셋 예제 2. 교집합, 합집합, 차집합 
비빔밥 = {'나물', '당근', '김', '버섯', '고추장', '시금치', '밥'}
김밥 = {'김','밥','시금치','당근','햄','계란','참치'}


# 두 셋의 교집합
print(비빔밥 & 김밥)
print(비빔밥.intersection(김밥))

# 두 셋의 합집합 
print(비빔밥 | 김밥)
print(비빔밥.union(김밥))

# 두 셋의 차집합 
print(김밥 - 비빔밥)
print(김밥.difference(비빔밥))

## 셋 예제 3. 셋 메서드 

김밥 = {"김", "단무지", "시금치", "당근"}

# 요소 추가하기  (순서를 보장하지 않는다.)
김밥.add("맛살")
print(김밥)

김밥.add("계란")
print(김밥)

# 요소 제거하기 
김밥.remove("시금치")
print(김밥)

# 없으면 에러나
#김밥.remove("햄")
# 이거넣으면 안나
김밥.discard("소세지")

# 임의의 요소 제거 
# 셋은 순서를 가지지 않는 자료형이므로, 어떤 요소가 제거될지 예측할 수 없다. 
# 빈 집합이라면 pop() 호출할 경우, KeyError 발생 
remove_item = 김밥.pop()

print(김밥,remove_item)


## 셋 예제 4. 자료 구조 변환하기
order = {"스파게티", "피자", "샐러드", "자몽에이드" } 
print(list(order))
print(tuple(order))
