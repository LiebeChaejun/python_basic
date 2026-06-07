# Chapter 02-03
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
print('선언')
n = 700

# 출력
print(n)
# 타입 함수(type())
print(type(n))
print()

# 동시 선언
print('동시 선언')
x = y = z = 700
print(x, y, z)
print()

# 선언과 재선언
print('재선언')
# 선언
var = 70

# 재선언
var = "Change Value"

print(var)
print(type(var))
# 마지막에 할당한 값이 덮어씌어진다.
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성(str, int ...)
# 2. 값 생성
# 3. 콘솔 출력

# ex1)
print(300)
print(int(300))

# ex2)
# n -> 777
n = 777

print(n, type(n))
print()

# m = n 
m = n
# m -> 777 <- 777

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인: 객체의 고유값 확인
m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()
# 파이썬 엔진이 같은 값을 가진 변수를 알아서 효율적으로 할당해준다.
# 어차피 같은 값을 할당할거면 파이썬 엔진이 알아서 같은 주소에 할당해준다. 값이 달라졌을때 비로소 별도로 할당해준다.

# 다양한 변수 선언
# CamelCase : numberOfCollegeGraduate -> 메서드를 선언할때 사용
# PascalCase : NumberOfCOllegeGraduate -> 클래스를 선언할때 사용
# ⭐️Snake Case : number_of_college_graduate -> 파이썬에서 변수를 사용할때 사용 

student_grade = 3
print(student_grade)

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 특수 문자로 시작하거나 숫자로 시작하는 변수는 X
# 예약어는 변수명으로 불가능하다. (for, import, as, class)
# https://www.w3schools.com/python/python_ref_keywords.asp