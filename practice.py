print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(6*7)
print(3*(3+7))
print(2**3) #2의 3승
print(10%3) #나머지
print(5//3) #몫
print(3==3) # ==는 =
print(1 != 4) #!는 같지 않다
print(not(1 !=1))
print((3>0)and(3<5)) #& 같음
print((3>0)or(3>5)) # |같음


print('풍선')
print('wow'*7)

# 참 / 거짓
print(5>10)
print(5<10)
print(not True)
print(not (5>10))

# 애완동물을 소개해 주세요~
name = "연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age>=3


print("우리집 "+animal+"의 이름은 "+name+"예요")
print(name+"는"+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
print(name+"는 어른일까요?" +str(is_adult))

station = "사당"
print(station, "행 열차가 들어오고 있습니다")

# number = number * 5 <이거랑 같음> number *= 5

print(abs(-5)) # 절댓값
print(pow(4, 2)) # 4의 2승
print(max(5, 10)) # 최댓값
print(min(5, 10)) # 최솟값
print(round(3.14)) #반올림

from math import*
print(floor(4.99)) #내림
print(ceil(3.41)) #올림
print(sqrt(16)) # 제곱근

#랜덤함수
from random import *
print(random()) # 0.0~1.0 미만의 임의의 값을 생성 
print(int(random())) # int넣으면 소숫점 사라짐

print(int(random()*45) +1 )
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정되었습니다.")

#슬라이싱
jumin = "020629-4123456"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " +jumin[7:]) # 7 부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # -1 출력 후 진행
# print(python.index("Java")) # 오류나면서 진행X
print(python.count("n"))

# 문자열 포맷
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살 입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))

age = 20
color = "삘긴"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
#\n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" , \' : 문장 내에서 따옴표
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\" 입니다.")

# \\ : 문장 내에서 \
# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 (한 글자 삭제)
# \t : tap

url = "http://naver.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))