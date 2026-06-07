# Chapter02-1
# 파이썬 완전 기초
# print 기초 사용법

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print() # 개행이 된다.

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')
print('010', '1111', '2222', sep='-')
print('example', 'gmail.com', sep='@')

# end 옵션
print('welcome to', end='    ')
print('it News', end='   ')
print('Web Site')
print()

# file 옵션
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d: 3, s: 'python, f: 3.14)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
# print('{0} {1}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

#  %s
print('%10s' % ('nice1111'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice1111'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:$>10}'.format('nice'))

print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonStudy'))
print('{:10.5}'.format('pythonStudy'))

print()

# %d
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))

print('%4d' % (42))
print('{:4d}'.format(42))

# %f
print('%f' % (3.13131434214))
print('%1.8f' % (3.13131434214))

print('{:f}'.format(3.13131434214))

print('%06.2f' % (3.141592653589793))