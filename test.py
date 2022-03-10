# week_01 test

# < Jupyter Notkebook 사용방법>
# 코드 실행: shift + enter

# 특정 문장을 헤딩으로 설정 하고 싶을 때 #을 붙이면 된다.
# 마크다운 과 코드 를 번갈아가면서 사용 가능.
# 삭제하고 싶을 때는 블락을 누르고 D를 2번 누른다.

# ====================================================

# 프로그래밍이란:
# - 프로그래밍 언어를 사용하여 프로그램을 개발하는 것
# - 논리적인 사고를 가질 수 있다.

# Programming language
# - 프로그램을 개발할 때 사용하는 도구
#   ex) C, C++, C#, Python, Ruby, Java etc
# - 인간이 원하는 것을 컴퓨터에게 명령할 때 사용하는 컴퓨터가 이해할 수 있는 언어

# 파이썬의 장점은 쉽고 간결하다는 것과 다양한 라이브러리를 사용할 수 있다는 것이다.


# < Chapter 2. Data: Types, Values, Variables, and Names >

# - 변수(variable): 특정 값을 저장하는 공간 | a
# - cf) 값을 담는 상자

# - 값(value) | 2

# - 할당하다(assign) : 변수에 값을 넣는 과정 
#   a = 2와 a == 2는 다르다.
#   a = 2는 a에 2를 할당하는 것이지만, a == 2 는 값이 동일한지 비교를 하는 것이다.

# - 자료형(type): 데이터의 형태  ex) boolean, integer, float

a = 2
type(a)         # integer
type(a==2)      # boolean


# < Type >
# integer (정수) : 1,2,3 ...
# floating point number (부동소수점) : 1.0, 2.0

# string (문자열): "1", "apple"
# "1"은 string, 1은 integer이다.

# bool (부울): True/False

# apple <-> "apple"

# < 할당 >
# = 이 기호를 사용한다.
# 수학에서 '같다'라는 사용되지만, 프로그래밍에서는 '할당하다'라는 의미를 가진다.
# "오른쪽의 값을 왼쪽에 할당한다"

# ex) playerHealth = 100         #playerHealth라는 변수에 100이라는 값을 할당한다.

# 오른쪽에 있는 모든 것은 값을 가져야 한다. (초기화를 해야 한다.)
# 할당을 안하고 쓸 경우 에러가 날 수 있다.
# ex) print(a+3)  -> a에 값을 초기화시키지 않으면 어떤 결과값을 반환해야하는지 컴퓨터는 모른다.

# 같은 변수에 다른 값을 넣을 수 있다.
# ex) a = 3
#     a = 'santa'
#     print(a)    -> 결과값: 'santa'

x = 1 # 초기화 (값을 처음 넣어주고 설정하는 과정)
y = x*2
print(x,y)

name = 'harry'
name = 'potter'
name = 4
print(name) # 변수명을 각각 다르게 설정하지 않으면 name에는 4라는 값이 최종적으로 할당이 된다.

# < 변수명 정하기 >
# 나쁜 변수명: a,b,c, a1, b1, ... -> 변수가 쓰이는 의미를 파악하기 힘들기 때문이다.
# 남이 코드를 볼 경우를 고려해서 서로 이해할 수 있는 의미있는 이름으로 선언해야 한다.
# 소문자, 대문자, 숫자, 언더바를 사용한다. 예: name, name2, my_name, Name, NAME

name = 'elf'
name1 = 'dwarf'
my_name = 'hobbit'
myName = 'gandalf' #캐멀표기법
print(name,name1,my_name,myName, sep=',')     # 결과값: elf,dwarf,hobbit,gandalf


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
# 1. 언더바로 시작하는 변수명: _name (클래스 내부 변수 지칭할 때, private 변수/함수 표현할 때) 
# private으로 사용할 것이므로 외부에서 접근하지 말라는 의미를 지닌다고 한다.

# 2. 더블 언더바로 시작하는 변수명: __name__
# 3. 대문자로 시작하는 변수명: Name
# 4. 전체 대문자: NAME

# 위 종류의 변수명들은 특정한 용도로 정해져 있기 때문에 변수명을 지을 때 조심한다.


# 변수명은 대소문자 구분이 된다.
num = 'Twelve'
Num = 'twelve'
print(num == Num)     # False
print(num != Num)     # True
