#### 2-1 숫자 자료형 ####
print(5)
print(-10)
print(3.14)
print(5+3) # 8
print(2*8) # 16
print(2*(1+5))

#### 2-2 문자열 자료형 ####
print('hello')
print("hello")
print("a"*5)

#### 2-3 boolean 자료형 ####
# 참/거짓
print(5 > 10)
print(True)
print(False)
print(not True) # False
print(not (5 > 10)) # True

#### 2-4.변수 ####
name = "순돌이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요") # 정수는 str()로 묶어서 표현하기
print(name + "는 어른일까요?" + str(is_adult))
print(name, age) # + 대신 , 로 문장만들 때에는 정수에 str()함수 쓰지 않아도 됨.
# 단 , 를 쓰는 경우 띄어쓰기 한 칸 자동으로 포함됨

#### 2-5.주석 ####

'''주석은
이렇게
합니다'''

# 직접 치거나

# 범위 지정 후 ctrl + /
# 주석 해제 시에도 동일 

#### 2-6.퀴즈 #1 ####
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

#### 3-1.연산자 ####
print(2**3) # 2^3 = 8
print(5%3) # 나머지 구하기 = 2
print(5//3) # 몫

print(3 == 3) # 같으면 True, 다르면 False

print(1 != 3) # True 출력
print(not(1 != 3)) # False 

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 < 5)) # or 대신 | 가능

#### 3-2.간단한수식 ####
number = 2
print(number)
number = number + 3

# 이렇게 줄여서도 가능
number += 2
number *= 2
number /= 2
number -= 2
number %= 2 # 나머지

#### 3-3.숫자처리함수 ####
print(abs(-5))
print(pow(4,3)) # 4^3 = 64
print(max(5,1,2))
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) # 내림
print(ceil(3.01)) # 올림
print(sqrt(16)) # 제곱근

# 20220104
#### 3-4.랜덤함수 ####
from random import * 
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 정수 생성
print(randrange(1, 10)) # 1이상 10미만의 임의의 정수 생성
print(randint(1, 10)) # 1이상 10이하의 임의의 정수 생성

#### 3-5.퀴즈 #2 ####
number = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월", number, "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 " + str(number) + " 일로 선정되었습니다.")

#### 4-1.문자열 ####
sentence = "나는 소년입니다"
print(sentence)

sentence2 = """
나는,
소년입니다
"""
print(sentence2)

#### 4-2.슬라이싱 ####
jumin = "990120-1234567"
print('성별: ' + jumin[7])
print('연: ' + jumin[0:2]) # 0부터 2직전까지. 즉 0부터 1번째자리까지
print('생년월일: ' + jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리: ' + jumin[-7:]) # 뒤에서 7번째자리부터 맨 끝까지

#### 4-3.문자열처리함수 ####
python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index + 1) # 찾기시작하는 스타트지점

print(python.find("Java")) # 원하는 값이 없으면 -1 출력
# print(python.index("Java")) # 없으면 에러뜸
#### 4-4.문자열포맷 ####
print('나는 %d살입니다.' % 20) # %d 정수
print('나는 %s을 좋아해요.' % '파이썬') # %s 문자열. 정수도 가능함
print('Apple은 %c로 시작해요.' % 'A') # %c 문자1개

print('나는 %s색과 %s색을 좋아해요.' % ('파랑', '빨강'))

print('나는 {}살입니다.' .format(20))
print('나는 {}색과 {}색을 좋아해요.' .format('파랑', '빨강'))

print('나는 {1}색과 {0}색을 좋아해요.' .format('파랑', '빨강')) # 순서 지정

print('나는 {age}살이며, {color}색을 좋아해요.' .format(age = 20, color ='빨강'))

age = 20
color = "빨강"
print(f'나는 {age}살이며, {color}색을 좋아해요.') # f로 시작하기

#### 4-5.탈출문자 ####
print('백문이 불여일견\n백견이 불여일타') # \n : 줄바꿈
print("나는 'python'을 공부중입니다.")
print("나는 \"python\"을 공부중이다.")
print("문장내에서 슬러시를 표시하려면 이렇게 \\")
print("Red dd Apple\rPine")

# \b : 백스페이스
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

#### 4-6.퀴즈 #3 ####
url = "http://naver.com"
answer1 = url.replace("http://", "")
answer2 = answer1[:answer1.index(".")]
answer3 = answer2[:3]
cnt_e = answer2.count("e")

print(answer3 + str(len(answer2)) + str(cnt_e) + "!")

#### 5-1.리스트 ####
subway = [10, 20, 30]
print(subway)

print(subway.index(30))

subway.append(40) # append하면 맨 뒤에 추가됨
print(subway)

subway.insert(2, 25) #insert(index, 객체)

print(subway.pop()) # pop: 맨 뒤의 객체 하나를 꺼냄
print(subway)

print(subway.count(10))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
num_list.reverse()

# 모두 지우기
num_list.clear()

# 다양한 자료형 함께 사용 가능
mix_list = ["string", 20]

mix_list.extend(num_list)
print(mix_list)


#### 5-2.사전 ####
cabinet = {3:'a', 5:'b', 6:'c'}
print(cabinet[3])
print(cabinet.get(3))
print(cabinet.get(3, "없음"))
print(3 in cabinet)

cabinet[8] = 'd'
print(cabinet)

del cabinet[8]

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())


#### 5-3.튜플 ####
menu = ("돈까스", "아이스크림")
print(menu[0])

# tuple은 add 기능 제공 안함
menu.add("생선까스") # -> 오류발생

name, age, hobby = "김", 20, "코"
print(name)
(name, age, hobby) = ("김", 20, "코")


#### 5-4.세트 ####
# 집합(set)
# : 중복 안됨, 순서 없음
my_set = {1, 1, 2, 2, 2, 3, 3, 3, 3, 3}
print(my_set)

my_set2 = set([1, 2])

# 교집합
print(my_set & my_set2)
print(my_set.intersection(my_set2))

# 합집합
print(my_set | my_set2)
print(my_set.union(my_set2))

# 차집합
print(my_set - my_set2)
print(my_set.difference(my_set2))

# set에 값 추가
my_set.add(5)
print(my_set)

# set에서 값 제거
my_set.remove(3)


#### 5-5.자료구조의 변경 ####
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

print(list(menu), type(list(menu)))
print(tuple(menu), tuple(list(menu)))


#### 5-6.퀴즈 #4 ####
from random import *
lst = list(range(1, 21))
print(type(lst))
shuffle(lst)
print(lst)

winners = sample(lst, 4)
print("-- 당첨자 발표 -- ")
print("{0}".format(winners[0]))


#### 6-1.if ####
weather = input("message")
if weather == "rain":
    print("umbrella")
elif weather == "sun":
    print("good day")
else:
    print("hi")
    
    
#### 6-2.for ####
for waiting_no in range(1, 6):
    print("대기번호 : {0}".format(waiting_no))
    
    
#### 6-3.while ####
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 님의 커피가 준비될 때 까지 {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 나왔습니다")
        
        
#### 6-4.continue 와 break ####
absent = [2, 5]
no_book = [7]
for student in range (1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("수업종료. {0}".format(student))
        break
    print("{0}".format(student))
    
    
#### 6-5.한 줄 for ####
absent = [i+100 for i in absent]


#### 6-6.퀴즈 #5 ####
cnt = 0
for customer in range (1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        ox = "O"
        print("[{0}] {1}번째 손님 (소요시간) : {2}분".format(ox, customer, time))
        cnt += 1
    else:
        ox = "x"
        print("[{0}] {1}번째 손님 (소요시간) : {2}분".format(ox, customer, time))
print(cnt)   


#### 7-1.함수 ####
def open_account():
    print("deff")

open_account()


#### 7-2.전달값과 반환값 ####
def deposit(balance, money):
    print("잔액은 {0}원입니다.".format(balance + money))
    return(balance + money)

balance = 5
balance = deposit(balance, 2)


#### 7-3.기본값 ####
def profile(name, age, main_lang):

    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))


profile("유재석", 20, "파이썬") # 유재석씨(20세)의 주 사용 언어는 파이썬
profile("김태호", 25, "자바") # 김태호씨(25세)의 주 사용 언어는 자바


#### 7-4.키워드값 ####
def profile(name, age, main_lang): # 키워드 인자 : name, age, main_lang
    print(name, age, main_lang)

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

profile("유재석", age=20, main_lang="파이썬") # (O) 올바른 함수 호출 방법 (일반 전달값을 먼저 작성)
# profile("김태호", age=25, "파이썬") # (X) 잘못된 함수 호출 방법 (키워드 인자 먼저 작성 후 일반 전달값 작성)


#### 7-5.가변인자 ####
def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능    
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    
    # print(type(language)) # tuple
    for lang in language:
        print(lang, end=" ") # 언어들을 모두 한 줄에 표시
    print() # 줄바꿈 목적
    
profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")


#### 7-6.지역변수와 전역변수 ####
# 전역변수ver
gun = 10
def checkpoint(soldiers):
    global gun
    gun -= soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

checkpoint(3)

# 전역변수 없는 ver
gun = 10
def checkpoint_ret(gun, soldiers):
    gun -= soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

gun = checkpoint_ret(gun, 3)


#### 7-7.퀴즈 #6 ####
def std_weight(height, gender):
    if gender == "남자":
        tmp = 22
    elif gender == "여자":
        tmp = 21
    weight = round(pow(height/100, 2)*tmp, 2)
    print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

std_weight(175, "남자")


#### 8-1.표준입출력 ####
print("a", "b")
print("a" + "b")
print("a", "b", sep="/", end="?")
print("ab")


import sys # sys 모듈을 가져와서 사용하겠다는 의미
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러
# 보통 프로그램 수행 과정에서 몇 시에 어떤 작업을 어떤 식으로 수행하고 있으며
# 그 결과는 어떠한지 등의 정보를 가지는 로그를 남길 때
# stdout 은 일반적인 내용을,
# stderr 는 에러 발생 시 관련 내용을 출력하기 위해 사용

# ljust, rjust 정렬은 문자열형태만 받을 수 있음!
scores = {"math":0, "english":50, "coding":100}
for subject, score in scores.items():
    print(subject.ljust(12), str(score).rjust(4), sep=":")

# zfill: 함께 전달해주는 숫자만큼의 공간을 확보하고, 그 공간을 0(zero)으로 채워줌(fill)
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))

# 표준입력
anwser = input("아무 값이나 입력하세요: ")
print("입력값은" + anwser + "입니다.")


#### 8-2.다양한 출력포맷 ####
print("{0:a>+10}".format(500))

print("{0}".format(500)) # {0} 위치에 500 값 출력
print("{0: >10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, 10 칸의 공간 확보
print("{0: >+10}".format(500)) # 빈 자리는 비워두기, 우측 정렬, + 기호, 10 칸의 공간 확보
print("{0: >+10}".format(-500))
print("{0:_<10}".format(500)) # 빈 자리는 _ 로, 좌측 정렬, 10 칸의 공간 확보

print("{0:,}".format(100000000000)) # 3자리 마다 콤마 찍어주기
print("{0:+,}".format(100000000000)) # + 기호, 3자리 마다 콤마 찍어주기
print("{0:+,}".format(-100000000000))

print("{0:f}".format(5/3)) # 실수 값 출력
print("{0:.2f}".format(5/3)) 
# {인덱스:[[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}


#### 8-3.파일입출력 ####
# open("파일명", "열기 모드", encoding="인코딩")
# 열기모드: 읽기(read, "r"), 쓰기(write, "w"), 이어쓰기(append, "a")
score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기("w") 모드로 열기
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close() # score.txt 파일 닫기

score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일을 쓰기("a") 모드로 열기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
print(score_file.read()) # 파일 전체 읽어오기
score_file.close()


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄바꿈 중복을 방지하기 위해 end="" 처리
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 반복문 readline
score_file = open("score.txt", "r", encoding="utf8")

while True:
    line = score_file.readline()
    if not line: # 더 이상 읽어올 내용이 없으면?
        break # 반복문 탈출
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()

# readliens 도 가능
score_file = open("score.txt", "r", encoding="utf8")

lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
score_file.close()
lines


#### 8-4.pickle ####
# pickle 을 이용해서 저장되는 파일은 텍스트(text)가 아닌 바이너리(binary) 형태
# 텍스트 파일: 일반적인 한글, 영어, 숫자 등의 내용을 담고 있음
# 바이너리 파일: .jpg, .png 와 같은 이미지나 .mp3 와 같은 음악, 또는 .exe 와 같은 실행 파일 

# pickle로 저장하는 파일도 바이너리 파일임 -> open() 함수를 이용할 때 "wb" 라고 해야 올바르게 저장이 됨
# 또한 데이터 내에 한글이 포함되어 있다 하더라도 별도의 encoding 은 지정할 필요 없음

import pickle # pickle 모듈 가져다 쓰기

profile_file = open("profile.pickle", "wb") # 바이너리(binary) 형태로 저장
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)

pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
profile_file.close()

# 읽기
profile_file = open("profile.pickle", "rb") # 읽을 때에도 바이너리(binary) 명시
profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장

print(profile)
profile_file.close()

#### 8-5.with ####
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


#### 8-6.퀴즈 #7 ####
for this_week in range(1, 51):
    with open("{0}주차.txt".format(this_week), "w", encoding="utf8") as weekly_file:
        weekly_file.write("- {0} 주차 주간보고 -\n부서: \n이름: \n업무 요약:".format(this_week))

# 나도코딩 해설
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")


#### 9-1.클래스 ####
class gen_Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))

marine1 = gen_Unit("마린", 40, 5)


#### 9-2._init_ ####
# 클래스 객체를 생성할 때는 __init__() 생성자에 정의된 갯수만큼 전달값을 넘겨주어야한다.
# 단, self 는 제외하고


#### 9-3.멤버변수 ####
# 멤버변수: 클래스 내에서 정의된 변수

#### 9-4.메소드 ####
class AttackUnit: # 공격 유닛
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, location): # 공격 방향
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage)) # 공간이 좁아서 2줄에 걸쳐 출력

    def damaged(self, damage): # damage 만큼 유닛 피해
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage)) # 데미지 정보 출력
        self.hp -= damage # 유닛의 체력에서 전달받은 damage 만큼 감소
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp)) # 남은 체력 출력
        if self.hp <= 0: # 남은 체력이 0 이하이면?
            print("{0} : 파괴되었습니다.".format(self.name)) # 유닛 파괴 처리

# 파이어뱃 : 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 채력 0


#### 9-5.상속 ####
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기. 
firebat1 = AttackUnit("파이어뱃", 50, 16) # 체력 50, 공격력 16
firebat1.attack("5시") # 5시 방향으로 공격 명령

# 공격 2번 받는다고 가정
firebat1.damaged(25) # 남은 체력 25
firebat1.damaged(25) # 남은 채력 0


#### 9-6.다중상속 ####
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed

    def fly(self, name, location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed): # 이름, 체력, 공격력, 공중 이동 속도
        AttackUnit.__init__(self, name, hp, damage) # 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed) # 공중 이동 속도

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5) # 이름, 체력, 공격력, 공중 이동 속도
valkyrie.fly(valkyrie.name, "3시") # 3시 방향으로 발키리를 이동


#### 9-7.메소드 오버라이딩 ####
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self, location): # 이동 함수 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가
        self.damage = damage

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

vulture = AttackUnit("벌쳐", 80, 10, 20) # 지상 speed 10
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit 클래스의 move() 메소드를 새롭게 정의 (오버라이딩)
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시") # 오버라이딩된 move() 호출


#### 9-8.pass ####
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

# 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") # 체력 500, 생성 위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()


#### 9-9.super ####
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 순서 변경
    def __init__(self):
        # super().__init__()
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출

# 드랍쉽
dropship = FlyableUnit()


#### 9-10.스타크래프트 프로젝트 전반전 ####
# 분량 너무 많아,,,,,
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name)) # 출력문 추가

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage): # AttackUnit 에서 Unit 으로 이동
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return

        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)

    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True
            
            
#### 9-11.스타크래프트 프로젝트 후반전 ####
from random import *

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5) # 이름, 체력, 이동속도, 공격력

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    siege_developed = False # 시즈모드 개발여부 (클래스 변수)

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35) # 이름, 체력, 이동속도, 공격력
        self.siege_mode = False # 시즈모드 (해제 상태)
    
    # 시즈모드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return

        # 현재 시즈모드가 아닐 때
        if self.siege_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2 # 공격력 2배로 증가
            self.siege_mode = True # 시즈 모드 설정
        # 현재 시즈모드일 때
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2 # 공격력 절반으로 감소
            self.siege_mode = False # 시즈 모드 해제

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5) # 체력, 공격력, 공중 이동 속도
        self.cloaked = False # 클로킹 모드 (해제 상태)

    # 클로킹 모드
    def cloaking(self):
        # 현재 클로킹 모드일 때
        if self.cloaked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.cloaked = False
        # 현재 클로킹 모드가 아닐 때
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.cloaked = True

# 게임 시작
def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

# 게임 종료
def game_over():
    print("Player : gg") # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t1)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.siege_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # Marine 의 인스턴스이면 스팀팩
        unit.stimpack()
    elif isinstance(unit, Tank): # Tank 의 인스턴스이면 시즈모드
        unit.set_siege_mode()
    elif isinstance(unit, Wraith): # Wraith 의 인스턴스이면 클로킹
        unit.cloaking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()


#### 9-12.퀴즈 #8 ####
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, 
        self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()


#--------------------------------------------------------------------------------#

#### 10-1.예외처리 ####
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)


#### 10-2.에러 발생시키기 ####
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")


#### 10-3.사용자 정의 예외처리 ####
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return "[에러코드 001] " + self.msg # 에러 메시지 가공


#### 10-4.finally ####
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 에러 발생 여부 상관 없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")


#### 10-5.퀴즈 #9 ####
chicken = 10 # 남은 치킨 수
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

while(True):
    print("[남은 치킨 : {0}]".format(chicken))
    order = int(input("치킨 몇 마리 주문하시겠습니까?"))
    if order > chicken: # 남은 치킨보다 주문량이 많을 때
        print("재료가 부족합니다.")
    else:
        print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
        waiting += 1 # 대기번호 증가
        chicken -= order # 주문 수 만큼 남은 치킨 감소


#### 11-1.모듈 ####
from theater_module import price, price_morning # 모듈에서 일부만 가져다가 사용
price(5) # 이번에는 5명
price_morning(6)
price_soldier(7) # import 하지 않았으므로 사용 불가

#### 11-2.패키지 ####
#### 11-3._all_ ####
__all__ = ["vietnam", "thailand"] # vietnam, thailand 모듈 공개


#### 11-4.모듈 직접 실행 ####

#### 11-5.패키지, 모듈 위치 ####
#### 11-6.pip install ####
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

#### 11-7.내장함수 ####
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())


#### 11-8.외장함수 ####
import os

folder = "sample_dir"

if os.path.exists(folder): # 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
else: # 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")

import time
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초


#### 11-9.퀴즈 #10 ####
def sign():
    print("이 프로그램은 나도코딩에 의해 만들어졌습니다.")
    print("유튜브 : http://youtube.com")
    print("이메일 : nadocoding@gmail.com")
