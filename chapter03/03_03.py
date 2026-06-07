# Chapter 03-02
# 문자형
# 문자형 중요⭐️

# 개요
# 문자형 중요성
# 문자형 출력
# 이스케이프
# 멀티 라인
# 문자형 연산
# 문자형 형 변환
# 인덱싱
# 문자형 함수
# 슬라이싱

# 문자형 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))

# 문자열의 길이를 구하는 함수
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열을 생성하는 법
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자열 사용
# I'm Boy

print("I'm Boy")
# print('I'm Boy) # ❗️오류발생
print('I\'m Boy')

print('a \tb')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
tab_str1 = "Click \t Start!"
tab_str2 = "New Line \n Check!"

print(tab_str1)
print(tab_str2)
print()

# Raw String 출력하기
raw_s = r'D:\python\test'
print(raw_s)

# 멀티라인 입력
# 역슬래쉬 활용
multi_str = \
"""
문자열
멀티 라인
테스트
"""
print(multi_str)

adsf = \
'asdfasdf'\
'asdf'

print(adsf)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Daegu Busan"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1) # 파이썬의 문자열 하나하나하나를 원소로 가지는 리스트
print('z' in str_o1)
print('P' not in str_o2)
print('A' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1), type(str(10.1)))
print(str(True), type(str(True)))
# print(True, type(True))
print()

# 문자열 함수(upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith('s'))
print("replace: ", str_o1.replace("thon", 'Good'))
print('sorted: ', sorted(str_o1)) # 리스트 형태로 반환된다. (알파벳 순서대로 정렬된 형태로)
print('split: ', str_o4.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 라는게 있다. -> 시퀀스 즉, 반복할 수 있다.
print()

for i in im_str:
  print(i)
print()

# 슬라이싱
str_sl = "Nice Python"

print(len(str_sl))
# 슬라이싱 연습
print(str_sl[0:3]) # 3 - 1 까지 출력 0, 1, 2 번 인덱스까지 출력
print(str_sl[5:]) # [5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl)-1]) # str_Sl[:10]
print(str_sl[:])
print(str_sl[1:9:2]) # 3번째 인수는 몇 개 단위로 가져올지 정해줌

print(str_sl[-2:])
print(str_sl[-5:])

print(str_sl[1: -2])
print(str_sl[::2])
print(str_sl[::-1])
print()

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a))
print(ord('a'))
print(chr(122))
print(chr(97))