# week_01 test

# 프로그래밍이란:
# - 프로그래밍 언어를 사용하여 프로그램을 개발하는 것
# - 논리적인 사고를 가질 수 있다.

# Programming language
# - 프로그램을 개발할 때 사용하는 도구
# - 인간이 원하는 것을 컴퓨터에게 명령할 때 사용하는 컴퓨터가 이해할 수 있는 언어

# < 파이썬 >
# - 간결하고 쉽다.
# - 라이브러리가 많다.


# < Chapter 2. Data: Types, Values, Variables, and Names >

# - 변수(variable): 특정 값을 저장하는 공간  ex) a
# - 값(value) ex) 2
# - 할당하다(assign) : 변수에 값을 넣는 과정 
#   a = 2 <-> a == 2
# - 자료형(type): 데이터의 형태  ex) boolean, integer, float

a = 2
type(a)
type(a==2)

# < Type >
# integer (정수) : 1,2,3 ...
# floating point number (부동소수점) : 1.0, 2.0
# string (문자열): "1", "apple"
# bool (부울): True/False

# apple <-> "apple"

# < 할당 >
# = 이 기호를 사용한다.
# 수학에서 '같다'라는 사용되지만, 프로그래밍에서는 '할당하다'라는 의미를 가진다.
# "오른쪽의 값을 왼쪽에 할당한다"
# 오른쪽에 있는 모든 것은 값을 가져야 한다. (초기화를 해야 한다.)
# 같은 변수에 다른 값을 넣을 수 있다.

x = 4 # 초기화 (값을 처음 넣어주고 설정하는 과정)
y = x+3
print(x,y)

name = 'kim'
name = 'lee'
name = 'park'
name = 4
print(name) # 변수명을 각각 다르게 설정해야 할 필요성.

# < 변수명 정하기 >
# 나쁜 변수명: a,b,c, a1, b1, ...
# 남이 이해할 수 있는 의미있는 이름으로 선언해야 한다.
# 소문자, 대문자, 숫자, 언더바를 사용한다. 예: name, name2, my_name, Name, NAME

name = 'juliette'
name1 = 'jessica'
my_name = 'laura'
myName = 'arin' #캐멀표기법
print(name,name1,my_name,myName, sep=',')


help("keywords")
# < List of the Python keywords >

# False               break               for                 not
# None                class               from                or
# True                continue            global              pass
# __peg_parser__      def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield

# 위의 것들은 변수명으로 사용할 수 없다.

# 이름을 지을 때 조심해야 하는 이유: 특별한 용도가 있기 때문에
# 1. 언더바로 시작하는 변수명: _name
# 2. 더블 언더바로 시작하는 변수명: name
# 3. 전체 대문자: NAME

# 변수명은 대소문자 구분이 된다.
num = 'number'
Num = 'Number'
print(num == Num)
print(num != Num)
