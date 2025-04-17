"""
import mymodule

print(mymodule.greeting("John"))  # 출력: Hello, John!
print(mymodule.person["age"])     # 출력: 25
import theater_module

theater_module.price(3)
theater_module.price_morning(5)
theater_module.price_student(2)
from theater_module import price, price_morning

price(3)
price_morning(5)
price_student(2)    ## 오류 
#### 4. 모듈에 별칭 주기
import theater_module as ym

ym.price(3)
ym.price_morning(5)
ym.price_student(2)
"""
import mypackage.math_operations as math_ops
import mypackage.string_operations as str_ops
from mypackage.subpackage import advanced_math
import sys
sys.path.append("C:/Users/3-15/Desktop/python_lab")


print(math_ops.add(10, 5))                 
print(math_ops.multiply(10, 5))            

print(str_ops.to_uppercase("hello"))       
print(str_ops.to_lowercase("WORLD"))      

print(advanced_math.power(2, 3))  
print(advanced_math.factorial(5))  


print(math_ops.add(10, 20))        
print(str_ops.to_uppercase("hi")) 
